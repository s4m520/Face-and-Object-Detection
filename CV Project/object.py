import cv2
from ultralytics import YOLO # Importing the YOLO function from the package

# Load a pretrained YOLO11 model
model = YOLO("yolo/yolo11n.pt")  

camera = cv2.VideoCapture(0)
print("Starting YOLO11 detection. Press 'q' to quit.")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Run inference
    results = model(frame, verbose=False)

    # results is a Results object.
    for r in results:
        boxes = r.boxes  # contains all the detected bounding boxes for an image
        classes = r.names  # dictionary that maps the class ID to the actual label name
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]  # coordinates of the detection : topleft (x1, y1) and bottomright (x2,y2) corners of the box
            conf = box.conf[0] # confidence score
            cls_id = int(box.cls[0]) # which class this detection belongs to
            label = classes[cls_id] # turn that ID into the actual name

            # Draw bounding box & label
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (int(x1), int(y1)-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()