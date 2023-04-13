from sqlalchemy.orm import Session
from src.comment.model import Comment
from src.picture.model import Picture
from .schemas import CommentCreate, CommentUpdate


def comment_create(db: Session, item: CommentCreate):
    picture = db.query(Picture).filter(Picture.id == item.picture_id).first()
    item.picture_id = picture
    comment = Comment(**item.dict())
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comment_list_by_picture(db: Session, picture_id: int):
    return db.query(Comment).filter_by(picture=picture_id).all()


def get_comment_by_picture(db: Session, picture_id: int, comment_id: int):
    return db.query(Comment).filter_by(picture=picture_id).filter_by(id=comment_id).first()


def put_comment_by_picture(db: Session, picture_id: int, comment_id: int, item: CommentUpdate):
    comment = get_comment_by_picture(db, picture_id, comment_id)
    comment.username = item.username
    comment.comment = item.comment

    db.add(comment)
    db.commit()
    db.refresh(comment)

    return comment


def delete_comment_by_picture(db: Session, picture_id: int, comment_id: int):
    comment = db.query(Comment).filter_by(picture=picture_id).filter_by(id=comment_id).first()
    db.delete(comment)
    db.commit()