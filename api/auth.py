from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from models.user import User
from db.session import SessionLocal
from core.security import create_token

router = APIRouter()
pwd = CryptContext(schemes=["bcrypt"])

@router.post("/register")
def register(user):
    db = SessionLocal()
    hashed = pwd.hash(user.password)
    new_user = User(username=user.username, password=hashed, role=user.role)
    db.add(new_user)
    db.commit()
    return {"msg": "Registered"}

@router.post("/login")
def login(user):
    db = SessionLocal()
    db_user = db.query(User).filter(User.username == user.username).first()
    if not pwd.verify(user.password, db_user.password):
        raise HTTPException(401)
    token = create_token({"sub": user.username, "role": db_user.role}, 30)
    return {"access_token": token}
