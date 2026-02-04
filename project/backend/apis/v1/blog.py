from fastapi import APIRouter,Depends
from schemas.blog import BlogCreateSchema
from sqlalchemy.orm import session
from db.session import get_db
from repositories.blog import provider_blog_reporitory

router = APIRouter()

@router.post("")
async def creatfe_blog(
    payload : BlogCreateSchema,
    db:session = Depends(get_db)
    ):
        repo = provider_blog_reporitory(db)
        repo.create_blog(payload )
        return {"d":"m"}