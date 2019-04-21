import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    hsv =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    yellow_lower = np.array([0, 0, 20], np.uint8)
    yellow_upper = np.array([100, 255, 10], np.uint8)
    yellow =  cv2.inRange(hsv, yellow_lower, yellow_upper)
    kernal = np.ones((5, 5), "uint8")
    blue = cv2.dilate(yellow, kernal)
    res = cv2.bitwise_and(frame, frame, mask = yellow)
    (ret,contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)


    cv2.imshow("Color Tracking", frame)
    img = cv2.flip(frame, 1)
    cv2.imshow("yellow", res)

    
    if cv2.waitKey(1) == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
