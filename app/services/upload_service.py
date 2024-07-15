import cloudinary
import cloudinary.uploader
from fastapi import UploadFile
from app.core.config import settings
from app.db.database import image_collection
from app.db.models import Image
from app.schemas import schemas

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET
)

async def upload_image(user_id: str, tags: str, picture: UploadFile):
    # Calculate the next order for the user's images
    images = image_collection.find({"user_id": user_id})
    image_list = schemas.list_images_serial(images)
    next_order = len(image_list) + 1
    
    # Upload image to Cloudinary
    result = cloudinary.uploader.upload(picture.file)
    image_url = result['secure_url']
    
    # Create Image object and save to database
    image = Image(user_id=user_id, tags=tags, url=image_url, order=next_order)
    result = image_collection.insert_one(image.dict())
    
    return str(result.inserted_id), image_url, tags
