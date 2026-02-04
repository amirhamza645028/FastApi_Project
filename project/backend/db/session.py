from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException,status

from core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL is ",SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush=False,
    bind=engine
)

# if settings.DB_MODE == 'sqlite':
#     engine = create_engine(
#         SQLALCHEMY_DATABASE_URL,
#         connect_args={"check_same_thread": False},
#     )
# else:
#     engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db():
    db = SessionLocal()
    try:
        db = SessionLocal()
        yield db
    except Exception as e :
        print(e)
        db.rollback()
        raise HTTPException(
            status = "Database connection errror "
        )from e 
    finally:
        db.close()


