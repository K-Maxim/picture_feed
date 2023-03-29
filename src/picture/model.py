from sqlalchemy import Column, Integer, String
from src.core.db import Base


class Picture(Base):
    __tablename__ = "picture"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    size = Column(Integer)
    user = Column(String)
