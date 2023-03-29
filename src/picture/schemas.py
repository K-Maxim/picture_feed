from pydantic import BaseModel


class PictureBase(BaseModel):
    title: str
    size: int
    user: str

    class Config:
        orm_mode = True


class ListPicture(PictureBase):
    id: int


class CreatePicture(PictureBase):
    pass
