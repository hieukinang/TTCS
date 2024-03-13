import cv2
import mediapipe as mp
import time

cap=cv2.VideoCapture("Video/son1.mp4")
pTimes=0

mpFaceDetection=mp.solutions.face_detection
mpDraw=mp.solutions.drawing_utils
faceDetection=mpFaceDetection.FaceDetection()

while True:
    success, img= cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results= faceDetection.process(imgRGB)
    print(results)
    if results.detections:
        for id,detection in enumerate(results.detections):
            print(id, detection)

    cTimes=time.time()
    fps=1/(cTimes-pTimes)
    pTimes= cTimes
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(255,10,10),2)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
