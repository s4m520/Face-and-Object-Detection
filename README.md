# Face-and-Object-Detection

This project demonstrates two detection applications built with OpenCV in Python:
- **Face Detection:** Detects faces using the Haar Cascade Classifier.
- **Object Detection:** Identifies and labels up to 80 object classes using YOLOv3 (You Only Look Once) deep learning model.

<br>

## Setup Instructions
### Prerequisites
- Python 3.7+
- OpenCV
- NumPY

### 1. Install Python
Ensure you have **Python 3.7 or higher** installed.

### 2. Install Required Packages
Open a terminal in the project folder and run:
```bash
pip install opencv-python numpy
```
<br>

## Dataset Download
- For **Face Detection:** No additional files needed (uses built-in OpenCV Classifier).
- For **Object Detection:**
  1. Download YOLOv3 weights file from: https://pjreddie.com/media/files/yolov3.weights
  2. Place the downloaded `yolov3.weights` file in the `yolo/` folder.

### File Structure
```
CV Project/
├── face.py
├── object.py
├── yolo/
|   ├── coco.names
│   ├── yolov3.cfg
│   └── yolov3.weights (download separately)
└── README.md
```
<br>

## How to Run
### 1. Face Detection
Open a terminal in the project folder and run:
```bash
python face.py
```
Press 'q' to quit
- **Results:**
  - Detects faces using webcam.
  - Draws red squares around detected faces.
 
### 2. Object Detection
Open a terminal in the project folder and run:
```bash
python object.py
```
Press 'q' to quit
- Make sure `yolov3.weights` file is in the `yolo/` folder before running.
- **Results:**
  - Detects 80 different object categories (listed in the `coco.names` file)
  - Draws green boxes around detected objects with labels and confidence scores.
