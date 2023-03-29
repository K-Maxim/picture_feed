from pydantic import BaseModel


class PictureBase(BaseModel):
    id: int
    title: str
    size: float

    class Config:
        orm_mode = True