
import cv2
from yolo_model import load_model, detect_objects
from hardware_accelerator import accelerate_postprocessing
import os

model, classes = load_model()

cap = cv2.VideoCapture('data/sample_video.mp4')
frame_id = 0
os.makedirs('output/detected_frames', exist_ok=True)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    detections = detect_objects(model, frame)
    final_boxes = accelerate_postprocessing(detections)

    for (x, y, w, h) in final_boxes:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite(f"output/detected_frames/frame_{frame_id:04d}.jpg", frame)
    frame_id += 1

cap.release()
print("Detection complete. Frames saved to output/detected_frames/")
