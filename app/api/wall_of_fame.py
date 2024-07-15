from fastapi import APIRouter, HTTPException
from app.services.wall_of_fame_service import get_wall_of_fame
from app.db.database import image_collection
from app.db.models import ImageUpdate
from bson import ObjectId


router = APIRouter()

@router.get("/wall-of-fame/{user_id}")
async def fetch_wall_of_fame(user_id: str):
    images = await get_wall_of_fame(user_id)
    return images

@router.post("/wall-of-fame/update-image-order")
async def update_image_order(images: list[ImageUpdate]):
    for image in images:
        result = image_collection.update_one(
            {"_id": ObjectId(image.id)},
            {"$set": {"order": image.order}}
        )
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail=f"Image with id {image.id} not found")
    return {"res": "Image order updated successfully"}

@router.delete("/wall-of-fame/delete/one/{id}")
async def delete_image(id: str):
    deleted_image = image_collection.find_one_and_delete({"_id": ObjectId(id)})
    if deleted_image:
        return {"message": f"Image with id {id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail=f"Image with id {id} not found")
