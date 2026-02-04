from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, Boolean, DateTime, ForeignKey
# from sqlalchemy.orm import relationship

from db.base_class import Base

class Blog(Base):
    title = Column(String, nullable=False)
    slug = Column(String,index=True,unique=True, nullable=False)
    content = Column(Text, nullable=True)
    author_id =  Column(Integer,ForeignKey("users.id") , nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)

    
    # author = relationship("User",back_populates="blogs")
