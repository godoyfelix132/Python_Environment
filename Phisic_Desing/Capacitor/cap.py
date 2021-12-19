import cv2
import numpy as np
from matplotlib import pyplot as plt
frame = cv2.imread('img//cap.JPG', 1)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Threshold of blue in HSV space
lower_blue = np.array([60, 35, 140])
upper_blue = np.array([180, 255, 255])


mask = cv2.inRange(hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(frame, frame, mask=mask)

cv2.imshow('frame', frame)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)

