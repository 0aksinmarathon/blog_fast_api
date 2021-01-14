from datetime import timedelta
from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserResponseModel
from app.database import get_db_session
from app.schemas.auth import Token
from app.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from app.util import authenticate_user, create_access_token, get_current_user

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(),
                                 db_session: Session = Depends(get_db_session)):
    user = authenticate_user(db_session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=UserResponseModel)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_user)):
    return [{"item_id": "Foo", "owner": current_user.email}]


@router.get("/items/")
async def read_items():
    return {"token": "asdojcnasjkdncjkas"}
