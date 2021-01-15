from fastapi import Depends, APIRouter, status, Header
from sqlalchemy.orm import Session
from app.models.user import User
from app.database import get_db_session
from typing import List, Optional
from app.schemas.user import UserQueryParams, UserUpdateModel, UserResponseModel, UserCreateModel
from app.util import oauth2_scheme, pwd_context

router = APIRouter(dependencies=[Depends(oauth2_scheme)])


@router.get('/{user_id}')
async def get_user(user_id: int, db_session: Session = Depends(get_db_session),
                   content_type: Optional[str] = Header(None),
                   user_agent: Optional[str] = Header(None),
                   host: Optional[str] = Header(None)):
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


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserResponseModel)
async def create_user(user: UserCreateModel, db_session: Session = Depends(get_db_session)):
    user_dict = dict(user)
    user_dict['hashed_password'] = pwd_context.hash(user_dict['password'])
    user_dict.pop('password')
    new_user = User(**user_dict)
    db_session.add(new_user)
    db_session.commit()
    return user
