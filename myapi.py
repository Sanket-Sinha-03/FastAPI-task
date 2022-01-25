import fastapi
import models
from fastapi import FastAPI, Depends
from typing import Optional
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from database import SessionLocal,engine
from sqlalchemy.orm import sessionmaker,Session
from models import Users, Items
from typing import List
app = FastAPI()

models.Base.metadata.create_all(bind=engine)
items = ['Onion','Farm eggs','Whole Wheat','Rice','Tea']

# classes to describe data in incoming requests
class User(BaseModel):
    Name: str
    Email_Address: str
    Street_Address: str

class Cart(BaseModel):
    data: List[int]
    user_id: int

# get connection to database
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Following are the required {} 

# Create a new user and store  user details (POST)
@app.post("/create-user")
def create_user(user: User,db : Session = Depends(get_db)):
    #  create object to store user for ORM
    user_data = models.Users(name=user.Name,email=user.Email_Address,address=user.Street_Address,login_status=True)
    
    # push and commit changes to db
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data

# Get all possible menu items (GET)
@app.get("/item-data")
def item_data():
    # return 'items' which  is a global variable which holds all possible items
    return items

#  store cart with menu items. (PUT)
@app.put("/cart")
def store_cart(cart: Cart, db : Session = Depends(get_db)):
    # 'cart.data' has the item_ids selected by user to be put in cart
    # looping through these items and adding them to the table Items along with the user_id
    for i in cart.data:
        c = models.Items(item_id =i, owner_id=cart.user_id)
        db.add(c)
        db.commit()
        db.refresh(c)
    return cart.user_id

# delete user (DELETE)
@app.delete("/delete")
def delete_user(user_id: int, db : Session = Depends(get_db)):
    # deleting user with given user_id from Table Users and all items in his shopping cart (table Items)
    user = db.query(models.Users).filter(models.Users.id == user_id).delete(synchronize_session=False)
    cart = db.query(models.Items).filter(models.Items.owner_id == user_id).delete(synchronize_session=False)
    db.commit()
    return 'done'
    