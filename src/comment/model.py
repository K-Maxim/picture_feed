from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.core.db import Base

from src.picture.model import Picture


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String)
    comment = Column(String)
    picture = Column(Integer, ForeignKey('picture.id', ondelete="CASCADE"))
    picture_id = relationship(Picture)

