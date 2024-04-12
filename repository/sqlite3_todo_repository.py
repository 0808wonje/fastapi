from typing import Optional, List, Type

from sqlalchemy.orm import Session, Query

import database
import models
from models import Todo


# RDB 실행
models.Base.metadata.create_all(bind=database.engine)


class Sqlite3TodoRepository:

    @staticmethod
    def persist_todo(todo: Todo, db: Session) -> int:
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return todo.id

    @staticmethod
    def find_todo_by_id(todo_id: int, db: Session):
        return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

    @staticmethod
    def find_all_todo(db: Session) -> list[Type[Todo]]:
        find_all = db.query(models.Todo).order_by(models.Todo.id.desc())
        return list(find_all)

    @staticmethod
    def update_todo(todo_id: int, db: Session) -> None:
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
        todo.completed = True
        db.commit()

    @staticmethod
    def remove_todo(todo_id: int, db: Session) -> None:
        todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
        db.delete(todo)
        db.commit()

