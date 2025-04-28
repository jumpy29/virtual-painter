import cv2
import numpy as np
import time
import os
from cvzone import HandTrackingModule as htm

folderPath = "Header"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f"{folderPath}/{imPath}")
    overlayList.append(image)
print(len(overlayList))

header = overlayList[0]
cap = cv2.VideoCapture(0)
cap.set(3, 1280)    #width
cap.set(4, 720)     #height
start_x = 640-148

detector = htm.HandDetector(detectionCon=0.85)

while True:
    #1. import image
    success, img = cap.read()
    img = cv2.flip(img, 1)

    #2. Find hand landmarks
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        
        #tip of index and middle fingers
        x_index, y_index = lmList[8][0:2]
        x_middle, y_middle = lmList[12][0:2]
        print(x_index, y_index)

    #3. Check which fingers are up

    #4. If selection mode - two fingers are up

    #5. If Drawing mode - index finger is up

    # setting the header image
    img[0:100, start_x:start_x+296] = header    

    cv2.imshow("Image", img)
    cv2.waitKey(1)
