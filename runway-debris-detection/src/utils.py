import cv2
import numpy as np

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at the path: {image_path}")
    return image

def preprocess_image(image, target_size=(640, 640)):
    image_resized = cv2.resize(image, target_size)
    image_normalized = image_resized / 255.0  # Normalize to [0, 1]
    return image_normalized

def display_results(image, results):
    for result in results:
        for box in result.boxes:
            cv2.rectangle(image, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                          (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 0, 0), 2)
            cv2.putText(image, f"{result.names[int(box.cls[0])]}",
                        (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
    cv2.imshow("Detection Results", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()