import sys 
import os 

from sqlalchemy.ext.declarative import declarative_base


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , DateTime
from sqlalchemy.orm import relationship

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True) 
    name = Column(String(60), nullable=False)
    birthday = Column(DateTime, nullable=False)
    uid = Column(String(100), nullable=False)
    email = Column(String(30), nullable=False)



