from fastapi import APIRouter, UploadFile, File
from app.services.yolo_service import detect_frame, detect_video

router = APIRouter()

@router.post("/detect-frame/")
async def detect_frame_api(data: dict):
    return detect_frame(data)

@router.post("/detect-video/")
async def detect_video_api(file: UploadFile = File(...)):
    return await detect_video(file)