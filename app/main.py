from fastapi import FastAPI
from app.api import auth, upload, wall_of_fame, user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(upload.router)
app.include_router(wall_of_fame.router)
app.include_router(user.router, prefix="/users")
