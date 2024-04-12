import os.path
from typing import List

import fastapi
from fastapi import FastAPI, Depends, Form, status, UploadFile
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

import database
from database import engine
from repository.memory_item_repository import *
from repository.sqlite3_todo_repository import Sqlite3TodoRepository

from sqlalchemy.orm import Session
import models


# FastAPI 인스턴스 생성
app = FastAPI()

# repository 생성
repository = Sqlite3TodoRepository()

# 동적 템플릿 경로 지정
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


# db 연결 메서드
def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# RDB 실행
models.Base.metadata.create_all(bind=engine)

img_link = './static/images/apple.png'
file_directory = './static/images'


# todos 전체 출력
@app.get("/")
def find_all_todo(request: fastapi.Request, db: Session = Depends(get_db)):
    todos = repository.find_all_todo(db)
    return templates.TemplateResponse('index.html', {'request': request, 'img_link': img_link, 'todos': todos})


# todos 등록
@app.post('/items/new')
async def add_todo(video: Optional[UploadFile] = Form(None), db: Session = Depends(get_db)) -> RedirectResponse:
    if not video.filename:
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    os.makedirs(file_directory, exist_ok=True)
    file_path = os.path.join(file_directory, video.filename)
    with open(file_path, 'wb') as buffer:
        buffer.write(video.file.read())
    repository.persist_todo(models.Todo(path=file_path, name=video.filename), db)
    return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)


# todos 수정
@app.get('/items/edit/{todo_id}')
async def update_todo(todo_id: int, db: Session = Depends(get_db)) -> RedirectResponse:
    repository.update_todo(todo_id, db)
    return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)


# todos 삭제
@app.get('/items/delete/{todo_id}')
async def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> RedirectResponse:
    repository.remove_todo(todo_id, db)
    return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)


# todos 검색
@app.get('/items')
async def find_todo(request: fastapi.Request, todo_id: Optional[str] = None, db: Session = Depends(get_db)):
    try:
        find = repository.find_todo_by_id(int(todo_id), db)
        todo = list()
        todo.append(find)
        return templates.TemplateResponse('index.html', {'request': request, 'img_link': img_link, 'todos': todo})
    except Exception:
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)


# videos 페이지
@app.get('/videos/{todo_id}')
async def get_video_page(request: fastapi.Request, todo_id: int, db: Session = Depends(get_db)):
    video = repository.find_todo_by_id(todo_id, db)
    return templates.TemplateResponse('videos.html', {'request': request, 'video_path': video.path[1:]})



