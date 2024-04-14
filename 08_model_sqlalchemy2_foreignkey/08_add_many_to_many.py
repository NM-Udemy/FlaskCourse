from models import app, db, Book, Author, BookAuthor

with app.app_context():
    book1 = Book(book_name="Book 1")
    book2 = Book(book_name="Book 2")
    book3 = Book(book_name="Book 3")
    
    author1 = Author(author_name="Author 1")
    author2 = Author(author_name="Author 2")
    
    book_author1 = BookAuthor(book=book1, author=author1)
    book_author2 = BookAuthor(book=book2, author=author1)
    book_author3 = BookAuthor(book=book2, author=author2)
    book_author4 = BookAuthor(book=book3, author=author2)
    
    db.session.add_all([book1, book2, book3, author1, author2,
                        book_author1, book_author2, book_author3, book_author4])
    
    db.session.commit()