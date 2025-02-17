import cv2
from ultralytics import YOLO
from utils import preprocess_image, display_results
from models.yolo_model import YOLOModel

def main():
    model = YOLOModel("yolov8n.pt")
    #video_path = "path/to/your/video.mp4"  # Update with your video path
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed_frame = preprocess_image(frame)
        results = model.predict(processed_frame)

        frame_with_detections, detections = display_results(frame, results)
        cv2.imshow("Detections", frame_with_detections)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()