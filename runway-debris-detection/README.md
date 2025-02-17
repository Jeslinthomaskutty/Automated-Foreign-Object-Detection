# Runway Debris Detection

This project utilizes YOLOv8 for detecting foreign debris on runways. The goal is to enhance runway safety by identifying potential hazards that could affect aircraft operations.

## Project Structure

```
runway-debris-detection
├── src
│   ├── main.py          # Entry point of the application
│   ├── utils.py         # Utility functions for image processing
│   └── models
│       └── yolo_model.py # YOLO model wrapper
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd runway-debris-detection
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

Make sure to place your images in the appropriate directory or modify the code to load images from your desired location.

## Model Information

This project uses the YOLOv8 model, which is known for its speed and accuracy in object detection tasks. The model has been trained to recognize various types of foreign debris that may be found on runways.

## Performance

The performance of the model can vary based on the quality of the input images and the specific types of debris present. Continuous training and fine-tuning may be required to improve detection rates for specific scenarios.