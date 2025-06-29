from ultralytics import YOLO
import cv2
import os

class ObjectDetector:
    def __init__(self, model_path="assets/yolov8n.pt"):
        self.model = YOLO(model_path)
        os.makedirs("output", exist_ok=True)

    def detect(self, image_path, output_path="output/results.jpg"):
        results = self.model(image_path)
        annotated_frame = results[0].plot()
        cv2.imwrite(output_path, annotated_frame)
        return output_path
