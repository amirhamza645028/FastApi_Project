from fastapi import APIRouter


from apis.v1.user import router as base_router

base_router = APIRouter(prefix='/v1')
base_router.include_router(
    base_router, 
    prefix="/users", 
    tags=["users"]
)
