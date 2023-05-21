from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import BookSchema, RequestBook, Response
from operation import get_book, get_book_by_id, create_book, remove_book, update_book
import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create')
async def create(request: RequestBook, db: Session=Depends(get_db)):
    create_book(db, book=request.parameter)
    return Response(code=200, status="OK", message="Book created successfully").dict(exclude_none=True)


@router.get('/')
async def get(db: Session=Depends(get_db)):
    _book = get_book(db, 0, 100)
    return Response(code=200, status="OK", message="Successfully fetched all data", result=_book).dict(exclude_none=True)


@router.get("/{id}")
async def get_by_id(id: int, db: Session=Depends(get_db)):
    _book = get_book_by_id(db, id)
    return Response(code=200, status="OK", message="Successfully fetched book data", result=_book).dict(exclude_none=True)


@router.post('/update')
async def update(request: RequestBook, db: Session=Depends(get_db)):
    _book = update_book(db=db, bok=request.parameter)
    return Response(code=200, status="OK", message="Successfully updated book data", result=_book).dict(exclude_none=True)


@router.delete('/{id}')
async def delete(id: int, db: Session=Depends(get_db)):
    _book = remove_book(db, book_id=id)
    return Response(code=200, status="OK", message="Book data deleted successfully", result=_book).dict(exclude_none=True)