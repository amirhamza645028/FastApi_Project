from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db
from schemas.user import UserCreate,UserView
from repositories.user import userRepository


router = APIRouter()

@router.post("",response_model=UserView)
def create_user(
    payload :UserCreate,
    db: Session = Depends(get_db)
    ):
    repo = userRepository(db)
    new_user=repo.create_user(email=payload.email,password=payload.password)
    return UserView(
        id = new_user.id,
        email =new_user.email,
        is_active = new_user.is_active
    )

@router.get('')
def get_users():
    return {"data":"hello"}