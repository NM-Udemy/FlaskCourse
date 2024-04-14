from models import app, db, Book, Author, BookAuthor

with app.app_context():
    author_id = 1
    author = db.session.get(Author, author_id)
    
    if author:
        if author.book_authors:
            author.book_authors[0].book.book_name = "Updated Book name"
            db.session.commit()
    