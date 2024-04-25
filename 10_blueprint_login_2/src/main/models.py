from sqlalchemy.orm import Mapped, mapped_column, relationship
from src import db

class Memo(db.Model):
    __tablename__ = 'memo'
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    title: Mapped[str] = mapped_column(db.String(50), nullable=False)
    content: Mapped[str] = mapped_column(db.Text)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'))
    user: Mapped["User"] = relationship(back_populates="memos")
    
    @classmethod
    def get_user_memos(cls, user):
        return db.session.execute(
            db.Select(cls.id, cls.title, cls.content).where(cls.user==user).order_by(cls.id.desc())
        ).all()
    
    @classmethod
    def add_memo(cls, title, content, user):
        new_memo = cls(title=title, content=content, user=user)
        db.session.add(new_memo)
        db.session.commit()
        return new_memo
    
    @classmethod
    def update_memo(cls, memo_id, title, content):
        memo = db.session.get(cls, memo_id)
        if memo:
            memo.title = title
            memo.content = content
            db.session.commit()
    
    @classmethod
    def delete_memo(cls, memo_id):
        memo = db.session.get(cls, memo_id)
        if memo:
            db.session.delete(memo)
            db.session.commit()