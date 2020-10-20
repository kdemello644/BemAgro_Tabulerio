import cv2
import numpy as np 
img = cv2.imread('./image/1.jpeg')
cont=0
co = 0 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, bin = cv2.threshold(gray,90,255,cv2.THRESH_BINARY)

cont, co = cv2.findContours(bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img, cont[50], -1, (0, 255, 0), 2)
for i in range(len(cont)):
    coor = cont[i]
    x,y,w,h = cv2.boundingRect(coor)
    roi = img[y:y+h,x:x+w]
    a = str('./Ret_cutter/im{}.jpg'.format(i))
    cv2.imwrite(a,roi)