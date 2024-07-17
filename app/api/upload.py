from fastapi import APIRouter, UploadFile, File, Form
from app.services.upload_service import upload_image

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...), user_id: str = Form(...), tags: str = Form(...)):
    image_id, image_url, image_tags = await upload_image(user_id, tags, file)
    return {"id": image_id, "url": image_url, "tags": image_tags}
