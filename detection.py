from ultralytics import YOLO

model = YOLO('runs/detect/model3/weights/best.pt')

def detect_objects(url):
    det = model.predict(f'{url}')
    results = det[0]
    out = results.boxes[0].cls[0].item()
    # for box in results.boxes:
    return out
