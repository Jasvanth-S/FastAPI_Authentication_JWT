from jose import jwt
from datetime import datetime, timedelta
from core.config import SECRET_KEY, ALGORITHM

def create_token(data: dict, minutes: int):
    expire = datetime.utcnow() + timedelta(minutes=minutes)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
