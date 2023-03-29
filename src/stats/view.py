from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import sevice
from src.core.utils import get_db


router = APIRouter()


@router.get('/stat', response_model=None)
def stats(db: Session = Depends(get_db)):
    return {
       "Общее количество изображений": sevice.get_all_quantity_picture(db),
       "Количество уникальных изображений": sevice.get_unique_picture(db),
       "Занимаемый размер в мб": round(sevice.get_total_size(db), 1),
       "Общее количество комментариев": sevice.get_all_quantity_comment(db),
       "Количество уникальных комментариев": sevice.get_unique_comment(db)
    }
