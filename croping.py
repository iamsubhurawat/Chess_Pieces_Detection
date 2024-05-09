import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

image_path = input('Enter the path of the image: ')

results = model(image_path)

for result in results:
    boxes = result.boxes.xyxy.cpu().numpy()
    count = 1
    for box in boxes:
        x_min, y_min, x_max, y_max = box
        img = cv2.imread(image_path)
        img = img[int(y_min):int(y_max),int(x_min):int(x_max)]
        cv2.imwrite(f'cropped images/image{count}.jpeg',img)
        count += 1