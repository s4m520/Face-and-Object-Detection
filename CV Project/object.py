import cv2
import numpy as np # Math library

# Initialize webcam
camera = cv2.VideoCapture(0)

# Build the Object Detector (from YOLO files)
detector = cv2.dnn.readNet('yolo/yolov3.weights', 'yolo/yolov3.cfg') # Read two files: the instruction manual (.cfg) and the trained brain (.weights). dnn = Deep Neural Network

# Read the object names file
file = open('yolo/coco.names', 'r')
classes = []
for line in file:
    classes.append(line.strip())
file.close()

# Find where the detector puts its results (layers that produce results)
output_layers = detector.getUnconnectedOutLayersNames() 

print("Starting object detection. Press 'q' to quit.")

while True:
    ret, frame = camera.read() 
    if not ret:
        break

    height, width, channels = frame.shape 


    # Prepare image for detector
    prepared_image = cv2.dnn.blobFromImage(frame, 1/255, (416, 416))

    # Give image to detector
    detector.setInput(prepared_image) 
    
    # Get detection results
    results = detector.forward(output_layers)


    # Process detections
    class_ids = [] # Type of object
    confidences = [] # How Sure we are
    boxes = [] # Where the object is
    # Process all detected objects
    for obj_group in results: # ( Large, medium, small)
        for obj_info in obj_group: # each individual object inside each group
            # Get what the object might be
            scores = obj_info[5:] # first 5 numbers = WHERE the object is, and everything after = WHAT the object might be
            best_guess = np.argmax(scores) # the highest scrore
            confidence = scores[best_guess]
            
            # Only keep confident detections (confidence threshold = 50%)
            if confidence > 0.5:
                # Convert position to pixels
                h, w = frame.shape[:2]
                center_x = int(obj_info[0] * w)
                center_y = int(obj_info[1] * h)
                obj_w = int(obj_info[2] * w)
                obj_h = int(obj_info[3] * h)
                
                # Get top-left corner
                x = center_x - obj_w // 2
                y = center_y - obj_h // 2
                
                # Save for drawing
                boxes.append([x, y, obj_w, obj_h])
                confidences.append(confidence)
                class_ids.append(best_guess)

    # Non-maximum suppression to remove duplicate boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4) # keep only the best box, 0.5 = confidence threshsold, 0.4 (if objects overlap 40% or more, theyre the same object)

    # Draw boxes
    if len(indexes) > 0: # we found some objects (if len == 0 then no objects were found)
        for i in indexes.flatten(): # simple flat list of numbers ready to use
            x, y, w, h = boxes[i] # where to draw the box (position and size)
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            
            # Draw rectangle
            color = (0, 255, 0)  # Green color
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2) # the box
            cv2.putText(frame, f"{label} {confidence:.2f}", (x, y - 10), # display object name, and confidence with 2 decimal places, (x,y-10) = same X as the box but 10 pixels ABOVE the box, font_hershay_simplex = normal font style, font size = 0.5 (half of normal)
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Object Detection", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()