from ultralytics import YOLO

class YOLOModel:
    def __init__(self, weights='yolov8n.pt'):
        self.model = YOLO(weights)

    def predict(self, img, classes=[], conf=0.5):
        if classes:
            results = self.model.predict(img, classes=classes, conf=conf)
        else:
            results = self.model.predict(img, conf=conf)
        return results

    def predict_and_detect(self, img, classes=[], conf=0.5):
        results = self.predict(img, classes, conf=conf)
        return results