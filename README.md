# Face-and-Object-Detection
> A lightweight hybrid vision system combining OpenCV and YOLO11 for real-time face and object detection.

<br>

This project demonstrates a hybrid detection system built with OpenCV and Ultralytics YOLO11 in Python.
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
- [Face Detection Evaluation](#face-detection-evaluation)

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

### 2. Download the Project Folder
Download the `CV Project` folder, then open it in your preferred IDE (Integrated Development Environment) or editor (e.g., VS Code).

### 3. Install Required Packages
Open a terminal inside the project folder and run:
```bash
pip install opencv-python numpy ultralytics
```
<br>

<a name="required-downloads"></a>
## 📁 Required Downloads
No additional downloads are required.
The Haar Cascade Classifier is included in OpenCV by default, and the YOLO11n model weights (`yolo11n.pt`) will be automatically downloaded by Ultralytics the first time you run the script.

### File Structure
```
CV Project/
├── detection.py          # Main Detection System
├── yolo/
│   └── yolo11n.pt
│
├── face_evaluation/      # Evaluation Folder
│   ├── evaluate.py
│   ├── labels.csv
│   └── images/
│
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
<br><br>
**Results:**
- The webcam feed is flipped horizontally for a natural mirror-like view.
- The system first detects faces through your webcam (using the Haar Cascade Classifier).
- **If faces are detected:**
    - Displays red bounding box around each detected face.
    - Shows a "Face Detected" label in the top right corner of the frame.
- **If faces are NOT detected:**
    - YOLO11 automatically activates for object detection.
    - Displays green bounding boxes, object names, and confidence scores around each detected object.
    - Shows an "Object Detection Activate" label in the top right corner of the frame.
<br>

<a name="face-detection-evaluation"></a>
## 🧪 Face Detection Evaluation
A separate evaluation script was developed to test the accuracy of the Haar Cascade face detection model on a subset of 28 labeled images from the WIDER Face dataset.
This test produced a confusion matrix and metrics (precision, recall, F1-score, accuracy) to evaluate how well the Haar Cascade performs before YOLO11 is triggered.


### To run the evaluation:
**1. Install Required Packages**<br>
Open a terminal in the project folder and run:
```bash
pip install opencv-python pandas scikit-learn
```
**2. Run the program**<br>
Open a terminal in the project folder and run:
```bash
cd face_evaluation
python evaluate.py
```
<br>

### Sample Results:
The following should appear in the terminal:
```bash
=== Face Detection Evaluation Results ===
Confusion Matrix:
[[ 1  3]
 [ 6 18]]
Precision: 0.86
Recall: 0.75
F1-Score: 0.80
Accuracy: 0.68
```
These results confirm that Haar Cascade performs reliably for frontal faces, serving effectively as a fast gatekeeper before invoking YOLO11 for deeper detection.

