import cv2
from cvzone.FaceDetectionModule import FaceDetector

video = cv2.VideoCapture(0)

detector = FaceDetector()

key = cv2.waitKey(1) & 0xFF
while True:
    _,img= video.read()
    ##imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img,bboxes = detector.findFaces(img,draw=True)

    cv2.imshow('Resultado',img)
    if cv2.waitKey(1) ==27:
        break
 
