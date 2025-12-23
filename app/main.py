from fastapi import FastAPI
from api.auth import router as auth
from api.users import router as users



app = FastAPI()

app.include_router(auth)
app.include_router(users)
