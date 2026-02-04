from pydantic import BaseModel , Field

class BlogCreateSchema(BaseModel):
    title: str = Field(...,min_length=4,max_length=50)
    content:str = Field(...,min_length=4)
    is_active:bool