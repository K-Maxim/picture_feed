from datetime import datetime
from src.core.db import Base
from sqlalchemy import Column, TIMESTAMP, String, Integer
from fastapi_users.db import SQLAlchemyBaseUserTable


class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
