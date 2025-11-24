# Face-and-Object-Detection

This project demonstrates two detection applications built with OpenCV in Python:
- **Face Detection:** Detects faces using the Haar Cascade Classifier.
- **Object Detection:** Identifies and labels up to 80 object classes using the YOLOv3 (You Only Look Once) deep learning model.

<br>

## Table of Contents
- [Setup Instructions](#-setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Install Python](#1-install-python)
  - [Install Required Packages](#2-install-required-packages)
- [Required Downloads](#-required-downloads)
  - [File Structure](#file-structure)
- [How to Run](#-how-to-run)
  - [Face Detection](#face-detection)
  - [Object Detection](#object-detection)
<br>

## ⚙️ Setup Instructions
### Prerequisites
- Python 3.7+
- OpenCV
- NumPy

### 1. Install Python
Ensure you have **Python 3.7 or higher** installed.

### 2. Install Required Packages
Open a terminal in the project folder and run:
```bash
pip install opencv-python numpy
```
<br>

## 📁 Required Downloads
- **Face Detection:** No additional files needed (uses built-in OpenCV classifier).
- **Object Detection:**
  1. Download the YOLOv3 weights file from: https://pjreddie.com/media/files/yolov3.weights
  2. Place the downloaded `yolov3.weights` file inside the `yolo/` folder.

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

## 🚀 How to Run
### Face Detection
Open a terminal in the project folder and run:
```bash
python face.py
```
Press '**q**' to quit
- **Results:**
  - Detects faces using your webcam.
  - Draws red squares around detected faces.
<br>
 
### Object Detection
Open a terminal in the project folder and run:
```bash
python object.py
```
Press '**q**' to quit
- **Results:**
  - Detects 80 different object classes (listed in the `coco.names` file) using your webcam.
  - Draws green rectangles around detected objects with labels and confidence scores.
