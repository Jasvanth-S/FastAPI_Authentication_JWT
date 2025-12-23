from fastapi import Depends, HTTPException, APIRouter
from jose import jwt
from core.config import SECRET_KEY, ALGORITHM

router = APIRouter()

def admin_only(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload["role"] != "admin":
        raise HTTPException(403)
    
@router.delete("/users/{id}")
def delete_user(id: int, token: str = Depends(admin_only)):
    return "User deleted"

