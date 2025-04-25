
import torch

def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.eval()
    return model, model.names

def detect_objects(model, frame):
    frame_rgb = frame[:, :, ::-1]
    results = model(frame_rgb)
    return results.xyxy[0].cpu().numpy()
