from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core.utils import get_db
from . import service
from src.comment.schemas import CommentCreate, CommentUpdate

router = APIRouter()


@router.get("/picture/{picture_id}/comment")
def comment_list(picture_id: int, db: Session = Depends(get_db)):
    return service.get_comment_list_by_picture(db, picture_id)


@router.post("/picture/{picture_id}/comment")
def create_comment(item: CommentCreate, db: Session = Depends(get_db)):
    return service.comment_create(db, item)


@router.get("/picture/{picture_id}/comment/{comment_id}")
def comment_list(picture_id: int, comment_id: int, db: Session = Depends(get_db)):
    return service.get_comment_by_picture(db, picture_id, comment_id)


@router.put("/picture/{picture_id}/comment/{comment_id}")
def comment_put(item: CommentUpdate, picture_id: int, comment_id: int, db: Session = Depends(get_db)):
    return service.put_comment_by_picture(db, picture_id, comment_id, item)


@router.delete("/picture/{picture_id}/comment/{comment_id}")
def comment_delete(picture_id: int, comment_id: int, db: Session = Depends(get_db)):
    return service.delete_comment_by_picture(db, picture_id, comment_id)






