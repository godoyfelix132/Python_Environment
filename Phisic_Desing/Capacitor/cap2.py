import cv2
import numpy as np

button = [20,60,50,250]

def nothing(x):
    pass

def process_click(event, x, y,flags, params):
    # check if the click is within the dimensions of the button
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > button[0] and y < button[1] and x > button[2] and x < button[3]:
            print('Clicked on Button!')

blank = np.zeros((1,1,1), np.uint8)
# Create a black image, a window
img = cv2.imread('img//cap.JPG', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#img = np.zeros((300,512,3), np.uint8)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.resizeWindow('image', 700, 400)
cv2.namedWindow('image2')
cv2.namedWindow('image3')

# create trackbars for color change
cv2.createTrackbar('H1','image',0,179,nothing)
cv2.createTrackbar('S1','image',0,255,nothing)
cv2.createTrackbar('V1','image',0,255,nothing)
cv2.createTrackbar('H2','image',0,179,nothing)
cv2.createTrackbar('S2','image',0,255,nothing)
cv2.createTrackbar('V2','image',0,255,nothing)


cv2.setMouseCallback('image',process_click)
control_image = np.zeros((80,300), np.uint8)
control_image[button[0]:button[1],button[2]:button[3]] = 180
cv2.putText(control_image, 'Button',(100,50),cv2.FONT_HERSHEY_PLAIN, 2,(0),3)
cv2.imshow('image', control_image)

while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break


    h1 = cv2.getTrackbarPos('H1','image')
    s1 = cv2.getTrackbarPos('S1','image')
    v1 = cv2.getTrackbarPos('V1','image')
    h2 = cv2.getTrackbarPos('H2', 'image')
    s2 = cv2.getTrackbarPos('S2', 'image')
    v2 = cv2.getTrackbarPos('V2', 'image')


    lower_blue = np.array([h1, s1, v1])
    upper_blue = np.array([h2, s2, v2])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('image2', result)
    cv2.imshow('image3', mask)


cv2.destroyAllWindows()
