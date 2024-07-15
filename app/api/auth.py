from fastapi import APIRouter, HTTPException, status, Depends
from app.db.models import Token, User
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.db.database import user_collection
from app.core import passwordSSH
from app.services import auth_service
from app.schemas import schemas

router = APIRouter()

@router.get("/", response_model = User)
async def read_root(current_user: Annotated[User, Depends(auth_service.get_current_user)]):
	return schemas.each_user_serial(current_user)

@router.post('/login')
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = user_collection.find_one({"username": form_data.username})

    if not user:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not passwordSSH.verify_password(user["password"], form_data.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    access_token = auth_service.create_access_token(data={"sub": user["username"]})

    return Token(access_token=access_token, token_type="bearer")

@router.post('/register')
async def create_user(request: User):
    hashed_pass = passwordSSH.hash_password(request.password)
    user_object = dict(request)
    user_object["password"] = hashed_pass
    user_collection.insert_one(user_object)

    return {"res": "Account created successfully"}