from Func_1 import circles_count, corte, tabuleiro
from Func_2 import color_RB
import cv2
img = cv2.imread('./image/1.jpeg')

r,b = color_RB(img)
circles_count(r)
circles_count(b)
corte(img)
tabuleiro(img)