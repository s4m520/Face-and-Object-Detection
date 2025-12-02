import cv2

# 1. Load the face detection classifier
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Loads a pre-trained model from OpenCV that knows how to detect front-facing human faces using a cascade of pattern checks.

# 2. Initialize webcam
camera = cv2.VideoCapture(0) # Opens the computer’s default camera (webcam) so frames can be captured for processing.

print("Starting face detection. Press 'q' to quit.")

while True:
    ret, frame = camera.read() # Captures one frame from the camera; 'ret' is True/False for success, and 'frame' is the actual image.
    if not ret: # If its not successful, stop the loop
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert each frame into grayscale because haar cascade was trained on grayscale images, it does not use color. it only looks for patterns of light and dark (edges, shadows, contrasts), and grayscale is simpler and faster to process because its only 1 channel.
    #frame = cv2.flip(frame, 1)

    # 3. Detect faces
    faces_detected = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)) # Using the face detection model (face_cascade), search in the grayscale image for faces of different sizes, scaling the image by 10% each time, only accepting areas confirmed by at least 5 detections, and ignoring objects smaller than 30×30 pixels.
    
    # Draw rectangles around detected faces
    for (x, y, w, h) in faces_detected:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)  # # Loops through all detected faces and draws a red rectangle on the frame around each one.

    
    cv2.imshow("Face Detection", frame) # Shows the video frame in a window titled "Face Detection"
    
    if cv2.waitKey(1) == ord('q'): # stop the loop as soon as 'q' is pressed
        break

camera.release() # disconnect and free the camera
cv2.destroyAllWindows()