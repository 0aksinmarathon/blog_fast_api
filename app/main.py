from fastapi import FastAPI, APIRouter
from app.routers import article, comment, user
from fastapi_contrib.auth.middlewares import AuthenticationMiddleware
from fastapi_contrib.auth.backends import AuthBackend
# from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware


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


app = FastAPI()
app.include_router(main_router)
# app.add_middleware(HTTPSRedirectMiddleware)


@app.on_event('startup')
async def startup():
    app.add_middleware(AuthenticationMiddleware, backend=AuthBackend())


@app.get('/')
async def hello():
    return {"text": "hello world!"}


