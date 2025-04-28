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

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)
