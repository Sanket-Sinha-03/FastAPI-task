from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    address = Column(String, unique=False, index=True)
    login_status = Column(Boolean, default=True)
    


class Items(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer,index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    