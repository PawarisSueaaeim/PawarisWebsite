import numpy as np
import cv2

TARGET_SIZE = (640,360)

cap = cv2.VideoCapture(0)

while(True):
    ret,im = cap.read()
    im_resized = cv2.resize(im, TARGET_SIZE)
    im_flipped = cv2.flip(im_resized, 1)

    red = cv2.inRange(im_flipped,(0,0,90),(50,50,255))
    cv2.imshow('red', red)

    blue = cv2.inRange(im_flipped,(90,0,0),(200,50,50))
    cv2.imshow('blue', blue)

    if(np.sum(red/255) > 1000):
        cv2.putText(im_flipped,'This is a red',(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255))

    if(np.sum(blue/255) > 1000):
        cv2.putText(im_flipped,'This is a blue',(50,100),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255))

    cv2.imshow('camera', im_flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
