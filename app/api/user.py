from fastapi import APIRouter, HTTPException
from app.db.database import user_collection
from app.schemas import schemas
from app.db.models import UserUpdate

router = APIRouter()

@router.get("/all/")
async def fetch_wall_of_fame():
    users = schemas.list_users_serial(user_collection.find())
    return users

@router.get("/one/{username}")
async def get_user_details(username: str):
    user_cursor = schemas.list_users_serial(user_collection.find({"username": username}))
    
    if user_cursor:
        return user_cursor[0]
    else:
        raise HTTPException(status_code=404, detail=f"User with username {username} not found")

@router.put("/update-bio")
async def update_bio(request: UserUpdate):
    result = user_collection.update_one(
        {"username": request.username},
        {"$set": {"bio": request.bio}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"User with username {request.username} not found")
    return {"res": "Bio updated successfully"}

@router.delete("/delete/{username}")
async def delete_user(username: str):
    deleted_user = user_collection.find_one_and_delete({'username': username})

    if deleted_user:
        return {"res": "User deleted successfully"}
    else:
        return {"res": "User not found"}