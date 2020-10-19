import cv2 
import numpy as np

def color_RB(img):
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #RED
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_img, low_red, high_red)
    red = cv2.bitwise_and(img, img, mask=red_mask)
    #GREEN
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_img, low_green, high_green)
    green = cv2.bitwise_and(img, img, mask=green_mask)
    return red, green

