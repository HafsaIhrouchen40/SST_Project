import cv2
import mediapipe as mp

# Function to detect pose landmarks from webcam
def detect_pose_landmarks():
    # Initialize MediaPipe Pose
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    # Initialize webcam
    cap = cv2.VideoCapture(1)  # Use 0 for default camera, or change to the appropriate camera index

    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame horizontally for a later selfie-view display
        frame = cv2.flip(frame, 1)

        # Convert the BGR image to RGB
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image
        results = pose.process(image_rgb)

        # Draw landmarks on the image
        if results.pose_landmarks:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Display the image with landmarks
        cv2.imshow('Pose Landmarks', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to detect pose landmarks from the webcam
detect_pose_landmarks()
