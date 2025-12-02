# Face-and-Object-Detection

This project demonstrates a hybrid real-time detection system built with OpenCV and Ultralytics YOLO11 in Python.
It performs sequential detection, first identifying human faces, and then switching to object detection when no faces are present.
- **Face Detection:** Detects faces using the Haar Cascade Classifier.
- **Object Detection:** Identifies and labels up to 80 object classes using the Ultralytics YOLO11n (You Only Look Once v11) deep-learning model.

<br>

## Table of Contents
- [Setup Instructions](#setup-instructions)
  - [System Requirements](#system-requirements)
  - [Install Python](#1-install-python)
  - [Install Required Packages](#2-install-required-packages)
- [Required Downloads](#required-downloads)
  - [File Structure](#file-structure)
- [How to Run](#how-to-run)
  - [Detection System](#detection-system)

<br>

<a name="setup-instructions"></a>
## ⚙️ Setup Instructions
### System Requirements
- Python 3.8+
- OpenCV
- NumPy
- Ultralytics YOLO

### 1. Install Python
Ensure you have **Python 3.8 or higher** installed.

### 2. Install Required Packages
Open a terminal in the project folder and run:
```bash
pip install opencv-python numpy ultralytics
```
<br>

<a name="required-downloads"></a>
## 📁 Required Downloads
No manual downloads are required.
The Haar Cascade classifier is included in OpenCV by default, and the YOLO11n model weights (`yolo11n.pt`) will be automatically downloaded by Ultralytics the first time you run the script.

### File Structure
```
CV Project/
├── detection.py
├── yolo/
│   └── yolo11n.pt        # downloaded automatically
└── README.md
```
<br>

<a name="how-to-run"></a>
## 🚀 How to Run
### Detection System
Open a terminal in the project folder and run:
```bash
python detection.py
```
Press '**q**' to quit
**Results:**
- The system first detects faces through your webcam (using the Haar Cascade classifier).
- **If faces are detected:**
    - Displays red bounding box around each detected face.
    - Shows a "Face Detected" label in the top right corner.
- **If faces are NOT detected:**
    - YOLO11 automatically activates for object detection.
    - Displays green bounding boxes, object names, and confidence scores around each detected object.
    - Shows an "Object Detection Activated" label in the top right corner.
- The webcam feed is flipped horizontally for a natural mirror-like view.
<br>
