import cv2
import os
import sys
import pathlib
import threading
from deepface import DeepFace

def detect(frame):
    for i in range(1):
        approvedfaces=cv2.imread("Face ID\APPROVEDFACES\\"+str(i)+".jpg")
    approved=False
    try:
        if DeepFace.verify(frame,approvedfaces):
            approved=True
        else:
            approved=False
    except ValueError:
        pass
    return approved

#gets basic video input
def video():
    # defines the video capture object
    vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

    framerate=0

    #This is the while true loop. Basically its gonna read each frame and then display it. If you press the ` key it will break from the loop
    while(True):
        #reads the video each frame
        ret, frame = vid.read()

        #displays the iamge with the detections
        cv2.imshow('raw camera', frame)
        
        if ret:
            if framerate%30==0:
                try:
                    threading.Thread(target=detect, args=(frame.copy(),)).start()
                except ValueError:
                    pass
            framerate+=1
            wtf=detect(frame)
            if wtf:
                cv2.putText(frame,"Open",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
            else:
                cv2.putText(frame,"Lock",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)

        #makes it so you can exit the loop
        if cv2.waitKey(1)==ord("`"):
            break

    #the object is then "released" (it really just makes it empty basically)
    vid.release()

    #closes windows
    cv2.destroyAllWindows()

video()
