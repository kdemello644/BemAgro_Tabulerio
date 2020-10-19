import cv2
import numpy as np

def circles_count(img):
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))
    print('Neste tabuleiro temos '+str(circles.shape[1])+' circulos.')
def corte(img):
    roi = img[20:400,20:400]
    cv2.imwrite('Tabuleiro_cortado.jpg',roi)
def tabuleiro(img):
    cont=0
    co = 0 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cont, co = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, cont, -1, (0, 255, 0), 2)
    cv2.imshow('Cont', img)
    cv2.waitKey(0)
    for c in cont:
        perimetro = cv2.arcLength(c,True)
        if perimetro > 300:
            aprox = cv2.approxPolyDP(c,0.03*perimetro,True)
            if len(aprox) == 4:
                (x1,x2,y1,y2)=cv2.boundingRect(c)
                cv2.rectangle(img, (x1,x2),(x1+y1,x2+y2),(0,255,0),2)
                roi = img[x2:x2+y2,x1:x1+y1]
                cv2.imwrite('Tabuleiro.jpg',roi)

img = cv2.imread('./image/1.jpeg')
tabuleiro(img)