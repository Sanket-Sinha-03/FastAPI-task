from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = "sqlite:///./users.db"
item = "sqlite:///./items.db"
engine = create_engine(
    user, connect_args={"check_same_thread": False}
)
engine = create_engine(
    item, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()