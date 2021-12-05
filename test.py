import cv2
import numpy as np
from time import sleep


width = 80
height = 80

offset = 6

position = 550

delay = 60

detec = []
carros = 0


def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture('video.mp4')
subtract_bg = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    ret, frame1 = cap.read()
    temp = float(1/delay)
    sleep(temp)
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtract_bg.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2. MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2. MORPH_CLOSE, kernel)
    contours, h = cv2.findContours(
        dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, position), (1200, position), (255, 127, 0), 3)
    for(i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        validContours = (w >= width) and (h >= height)
        if not validContours:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, 'vehicle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0, 255), -1)

        for (x, y) in detec:
            if y < (position+offset) and y > (position-offset):
                carros += 1
                cv2.line(frame1, (25, position),
                         (1200, position), (0, 127, 255), 3)
                detec.remove((x, y))
                print("car is detected : "+str(carros))

    cv2.putText(frame1, "VEHICLE COUNT : "+str(carros), (0, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.imshow("Video Original", frame1)
    #cv2.imshow("Detectar", dilatada)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
