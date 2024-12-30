import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode = False, upBody=False, smooth = True, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        #initialize MediaPipe Pose model for detecting human body landmarks(like joints)
        self.mp_pose = mp.solutions.pose
        self.pose = mp.solutions.pose.Pose(
            self.mode, self.upBody, self.smooth, self.detectionCon, self.trackCon)
        
    def findPose(self, frame, draw = True):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.pose.process(frame_rgb)
        if result.pose_landmarks:
            if draw:
                self.mp_drawing = mp.solutions.drawing_utils
                self.mp_drawing.draw_landmarks(frame, result.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        
        return frame
        

def main():
    cap = cv2.VideoCapture('/Users/roshansanjeev/Desktop/AdvancedComputerVision/Videos/FrontSquat.mp4')
    #cTime = time.time()
    #pTime = cTime
    #fps = 1/(cTime-pTime)
    
    detector = poseDetector()
    
    while cap.isOpened():
        frame = detector.findPose(frame)
        success, frame = cap.read()
        if not success:
            break
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = pose.process(frame_rgb)
        
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h,w,c = frame.shape
            print(id, lm)
            cx, cy = int(lm.x*w, lm.y*h)
       
        #play video frame 
        cv2.imshow('MediaPipe Pose', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        

if __name__ == "__main__":
    main()