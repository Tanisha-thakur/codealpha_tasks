from ultralytics import YOLO
import numpy as np

class ObjectDetector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def detect(self, frame):
        results = self.model(frame, verbose=False)[0]
        detections = []
        for box, conf, cls in zip(results.boxes.xyxy, results.boxes.conf, results.boxes.cls):
            if conf > 0.5:
                x1, y1, x2, y2 = map(int, box.tolist())
                detections.append([x1, y1, x2, y2, conf.item()])
        return np.array(detections), results.plot()
