from app.routers import article, comment, user, auth
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models import User


main_router = APIRouter()
main_router.include_router(
    article.router,
    prefix='/api/article',
    tags=['article']
)
main_router.include_router(
    comment.router,
    prefix='/api/comment',
    tags=['comment']
)
main_router.include_router(
    user.router,
    prefix='/api/user',
    tags=['user']
)
main_router.include_router(
    auth.router,
    prefix='/api/auth',
    tags=['auth']
)


app = FastAPI()
app.include_router(main_router)


@app.on_event('startup')
async def startup():
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get('/')
async def hello():
    return {"text": "hello world!"}


