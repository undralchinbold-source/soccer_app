import os
from pathlib import Path
from typing import Dict, Any
import cv2
import requests
import numpy as np
from ultralytics import YOLO

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best.pt"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

model = YOLO(str(MODEL_PATH))

def process_results(image, results):
    if not results or len(results[0].boxes) == 0:
        return {"detected": False, "message": "Бөмбөг олдсонгүй."}

    result = results[0]
    best_box = None
    best_conf = -1

    for box in result.boxes:
        conf = float(box.conf[0].item())
        if conf > best_conf:
            best_conf = conf
            best_box = box

    if best_box is not None:
        x1, y1, x2, y2 = map(int, best_box.xyxy[0].tolist())
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 4)
        cv2.putText(image, f"ball {best_conf:.2f}", (x1, y1-10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        
        output_path = OUTPUT_DIR / "detected.jpg"
        cv2.imwrite(str(output_path), image)

        return {
            "detected": True,
            "confidence": round(best_conf, 2),
            "coordinates": {"x1": x1, "y1": y1, "x2": x2, "y2": y2}
        }
    return {"detected": False, "message": "Объект олдсонгүй."}

def detect_soccer_ball(image_url: str) -> Dict[str, Any]:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(image_url, headers=headers, timeout=30)
    image_array = np.frombuffer(response.content, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    results = model.predict(source=image, conf=0.05, imgsz=640, verbose=False)
    return process_results(image, results)

def detect_from_file(filepath: str) -> Dict[str, Any]:
    image = cv2.imread(filepath)
    results = model.predict(source=image, conf=0.05, imgsz=640, verbose=False)
    return process_results(image, results)