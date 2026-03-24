from fastapi import FastAPI, UploadFile, File
import base64
import numpy as np
import cv2
from ultralytics import YOLO
import tempfile

app = FastAPI()

model = YOLO("best.pt")

# -------- IMAGE / FRAME DETECTION --------
@app.post("/detect-frame/")
async def detect_frame(data: dict):
    image_bytes = base64.b64decode(data["image"])
    np_arr = np.frombuffer(image_bytes, np.uint8)
    frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    results = model(frame)

    boxes = []
    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        boxes.append({
            "x1": x1,
            "y1": y1,
            "x2": x2,
            "y2": y2
        })

    return {"boxes": boxes}


# -------- VIDEO DETECTION --------
@app.post("/detect-video/")
async def detect_video(file: UploadFile = File(...)):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(await file.read())

    cap = cv2.VideoCapture(temp.name)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_id = 0
    results_data = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        timestamp = frame_id / fps
        results = model(frame)

        boxes = []
        for box in results[0].boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()
            boxes.append({
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2
            })

        results_data.append({
            "time": timestamp,
            "boxes": boxes
        })

        frame_id += 1

    cap.release()

    return {"detections": results_data}