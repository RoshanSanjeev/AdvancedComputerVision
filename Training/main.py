import cv2
import mediapipe as mp

#initialize MediaPipe Pose model for detecting human body landmarks(like joints)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

def readWebCam():
    #Open webcam(cap is open an open cv video object) -or- open video file
    cap = cv2.VideoCapture(0)
    #as long as webcam is open
    while cap.isOpened():
        #cap.read captures a single frame from the webcam
        #success is boolean tracking whether frame was read successfully
        #frame is the captured frame
        success, frame = cap.read()
        if not success:
            break

        # Convert OpenCV's BGR to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Analyzes the RGB frame to detect human body landmarks
        #result stores the landmarks(joints like the shoulders or knees)
        result = pose.process(frame_rgb)

        # Draw landmarks
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Show frame
        cv2.imshow('MediaPipe Pose', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

def readDownload():
    cap = cv2.VideoCapture('/Users/roshansanjeev/Desktop/AdvancedComputerVision/Videos/SideAirSquat.mp4')
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        # Show frame
        cv2.imshow('MediaPipe Pose', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        

#readWebCam()
#-or-
readDownload()