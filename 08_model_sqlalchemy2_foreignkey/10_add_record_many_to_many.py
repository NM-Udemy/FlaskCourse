from models import app, db, Book, Author, BookAuthor

with app.app_context():
    new_book = Book(book_name="New Book")
    author = db.session.get(Author, 1)
    if author:
        book_author = BookAuthor(book=new_book, author=author)
        db.session.add(new_book)
        db.session.add(book_author)
        db.session.commit()
    