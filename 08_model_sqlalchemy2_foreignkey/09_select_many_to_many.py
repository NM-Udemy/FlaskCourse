from models import app, db, Book, Author, BookAuthor

with app.app_context():
    book = db.session.get(Book, 2)
    for book_author in book.book_authors:
        print(book_author.author.id, book_author.author.author_name)
    
    author = db.session.get(Author, 2)
    for book_author in author.book_authors:
        print(book_author.book.id, book_author.book.book_name)