from models import app, db, Book, Author, BookAuthor

with app.app_context():
    author_id = 1
    author = db.session.get(Author, author_id)
    
    if author:
        if author.book_authors:
            print(len(author.book_authors))
            book_author_to_delete = author.book_authors[2]
            book_to_delete = book_author_to_delete.book
            db.session.delete(book_author_to_delete)
            db.session.delete(book_to_delete)
            db.session.commit()
            print(book_to_delete.book_name,
                  book_author_to_delete.book_id, book_author_to_delete.author_id
                )
    