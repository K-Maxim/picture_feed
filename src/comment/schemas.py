from pydantic import BaseModel


class CommentBase(BaseModel):
    username: str
    comment: str

    class Config:
        orm_mode = True


class CommentList(CommentBase):
    id: int
    picture_id: int


class CommentCreate(CommentBase):
    picture_id: int


class CommentUpdate(CommentBase):
    pass

