from sqlalchemy.orm import Session
from model import Book
from schema import BookSchema


def get_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: BookSchema):
    _book = Book(title=book.title, description=book.description)
    db.add(_book)
    db.commit()
    db.refresh(_book)
    return _book


def remove_book(db: Session, book_id: int):
    _book = get_book_by_id(db=db, book_id=book_id)
    db.delete(_book)
    db.commit()


def update_book(db: Session, bok: BookSchema):
    _book = get_book_by_id(db=db, book_id=bok.id)
    _book.title = bok.title
    _book.description = bok.description
    db.commit()
    db.refresh(_book)
    return _book
