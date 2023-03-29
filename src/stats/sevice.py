from sqlalchemy.orm import Session
from src.picture.model import Picture
from src.comment.model import Comment


def get_all_quantity_picture(db: Session):
    return len(db.query(Picture).all())


def get_total_size(db: Session):
    pictures = db.query(Picture).all()
    total_size = [i.size for i in pictures]
    return sum(total_size) / 1048576


def get_all_quantity_comment(db: Session):
    return len(db.query(Comment).all())


def get_unique_comment(db: Session):
    all_comment = db.query(Comment).all()
    username_list = [i.username for i in all_comment]
    return len(set(username_list))


def get_unique_picture(db: Session):
    all_comment = db.query(Picture).all()
    user_list = [i.user for i in all_comment]
    return len(set(user_list))
