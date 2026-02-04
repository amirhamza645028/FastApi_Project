from email_validator import validate_email, EmailNotValidError
from pydantic import BaseModel, Field,EmailStr
from fastapi import HTTPException, status

#properties required during user creation
class UserCreate(BaseModel):
    email : str
    password : str = Field(..., min_length=4)
def __init__ (self, **data):
    super().__init__(**data)

    if self.email:
        try:
            self.email = self.email.strip().lower()
            emailInfo = validate_email(
                self.email,
                check_deliverability = False)
            self.email = emailInfo.normalized
        except EmailNotValidError as e :
                raise HTTPException (
                    status_code = status.HTTP_400_BAD_REQUEST,
                    details = "Not a valid email"
                )    
class UserView(BaseModel):
     id:int
     email: EmailStr
     is__active : bool

     class Config():
          orm_mode = True
          