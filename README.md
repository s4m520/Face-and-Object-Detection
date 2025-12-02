# Face-and-Object-Detection

This project demonstrates two detection applications built with OpenCV in Python:
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
  - [Face Detection](#face-detection)
  - [Object Detection](#object-detection)

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
- **Face Detection:** No additional files needed (uses built-in OpenCV classifier).
- **Object Detection:** No manual downloads needed (the model weights `yolo11n.pt` is automatically downloaded by Ultralytics the first time you run the script.

### File Structure
```
CV Project/
├── face.py
├── object.py
├── yolo/
│   └── yolo11n.pt        # downloaded automatically
└── README.md
```
<br>

<a name="how-to-run"></a>
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
  - Detects 80 different object classes (trained on the COCO dataset) using your webcam.
  - Draws green rectangles around detected objects with labels and confidence scores.
