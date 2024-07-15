from app.db.database import image_collection
from app.schemas import schemas

async def get_wall_of_fame(user_id: str):
    images = image_collection.find({"user_id": user_id}).sort("order", 1)
    return schemas.list_images_serial(images)
