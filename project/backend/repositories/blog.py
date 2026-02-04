from sqlalchemy.orm import session
from schemas.blog import BlogCreateSchema
class BlogRepository:
    def __init__(self,db:session)->None:
        self.db = db

    def create_blog(self,data:BlogCreateSchema):
        print(data)

def provider_blog_reporitory(db:session)->BlogRepository:
    return BlogRepository