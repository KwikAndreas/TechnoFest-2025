from flask import Flask, jsonify
from ultralytics import YOLO
import cv2

app = Flask(__name__)

# Load model
model = YOLO("yolov8n.pt")

@app.route('/detect', methods=['GET'])
def detect():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return jsonify({"error": "Camera error"})

    results = model(frame)

    detections = []
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            if conf > 0.5:
                detections.append({
                    "label": model.names[cls],
                    "confidence": conf,
                    "bbox": [x1, y1, x2, y2]
                })

    return jsonify({"detections": detections})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
