# _*_ coding: utf-8 _*_

__author__ = 'Morgan'

'''
python spider -- OpenCV | | Demo
'''
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
