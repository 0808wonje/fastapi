from database import Base
from sqlalchemy import Column, Integer, Boolean, String, BLOB, LargeBinary


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    path = Column(String(100))
    # task = Column(String(100))
    # completed = Column(Boolean, default=False)
