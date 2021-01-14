from fastapi import Depends, APIRouter, status, Header
from sqlalchemy.orm import Session
from models.user import User
from blog_db import get_db_session
from typing import List, Optional
from schemas.user import UserQueryParams, UserUpdateModel, UserResponseModel, UserCreateModel

router = APIRouter()


@router.get('/{user_id}')
async def get_user(user_id: int, db_session: Session = Depends(get_db_session),
                   content_type: Optional[str] = Header(None),
                   user_agent: Optional[str] = Header(None),
                   host: Optional[str] = Header(None)):
    print(content_type, user_agent, host)
    return db_session.query(User).get(user_id)


@router.put('/{user_id}', response_model=UserResponseModel)
async def get_user(user_id: int, request_body: UserUpdateModel, db_session: Session = Depends(get_db_session)):
    updated_user = db_session.query(User).get(user_id)
    for key, value in request_body.dict().items():
        if value is not None:
            setattr(updated_user, key, value)
    db_session.commit()
    return updated_user


@router.get('/', response_model=List[UserResponseModel])
async def get_users(query_param_values: UserQueryParams = Depends(),
                    db_session: Session = Depends(get_db_session)):
    users = db_session.query(User)
    for key in query_param_values.query_params:
        if getattr(query_param_values, key) is not None:
            users = users.filter(getattr(User, key) == getattr(query_param_values, key))
    return users.all()


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreateModel, db_session: Session = Depends(get_db_session)):
    new_user = User(**dict(user))
    db_session.add(new_user)
    db_session.commit()
    return user
