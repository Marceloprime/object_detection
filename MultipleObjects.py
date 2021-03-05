import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('./dataset/jogo_01/base_01.jpg')
img_gray =  cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
template = cv2.imread('./dataset/jogo_01/objetos/01.jpeg', 0)
width, height = template.shape[::-1]

print(width, height)
#cv2.TM_CCOEFF_NORMED
#0.667 - 16px
#0.697 - 10px

res = cv2.matchTemplate(img_gray , template , cv2.TM_CCOEFF_NORMED)
ret,thresh1 = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)
th2 = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(th2 )


threshold = 0.667

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)

cv2.imwrite('output.png',img_rgb)