from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.database import get_db_session
from typing import List
from app.schemas.comment import CommentQueryParams, CommentGetResponseModel, CommentCreateModel
from app.util import oauth2_scheme

router = APIRouter(dependencies=[Depends(oauth2_scheme)])


@router.get('/{comment_id}')
async def get_comment(comment_id: int, db_session: Session = Depends(get_db_session)):
    return db_session.query(Comment).get(comment_id)


@router.get('/', response_model=List[CommentGetResponseModel])
async def get_comments(query_param_values: CommentQueryParams = Depends(),
                       db_session: Session = Depends(get_db_session)):
    comments = db_session.query(Comment)
    for key in query_param_values.query_params:
        if getattr(query_param_values, key) is not None:
            comments = comments.filter(getattr(Comment, key) == getattr(query_param_values, key))
    return comments.all()


@router.post('/')
async def create_comment(comment: CommentCreateModel, db_session: Session = Depends(get_db_session)):
    new_comment = Comment(**dict(comment))
    db_session.add(new_comment)
    db_session.commit()
    return comment
