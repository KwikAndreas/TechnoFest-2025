from ultralytics import YOLO
import cv2

# Load model YOLOv8 pre-trained
model = YOLO("yolov8n.pt")  # Versi YOLOv8 yang kecil dan cepat

# Buka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Deteksi objek di dalam frame
    results = model(frame)

    # Tampilkan hasil deteksi
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Koordinat bounding box
            conf = float(box.conf[0])  # Confidence Score
            cls = int(box.cls[0])  # Kelas objek
            
            # Jika confidence tinggi, tampilkan bounding box
            if conf > 0.5:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{model.names[cls]} {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.imshow("Trash Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
