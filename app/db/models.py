from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(unique=True)
    bio: str = ""
    email: str
    name: str
    password: str

class UserUpdate(BaseModel):
    username: str
    bio: str

class Image(BaseModel):
    user_id: str
    url: str
    tags: str
    order: int = Field(..., description="Order of the image for the user")

class Token(BaseModel):
    access_token: str
    token_type: str

class ImageUpdate(BaseModel):
    id: str
    order: int