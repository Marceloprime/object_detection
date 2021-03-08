import cv2
import numpy as np

def get_filtered_image(imageBase, imagemGoal, action, width, height):
    img = cv2.cvtColor(imageBase, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(imagemGoal, cv2.COLOR_BGR2RGB)

    filtered = None
    filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    res = cv2.matchTemplate(img , img2 , cv2.TM_CCOEFF_NORMED)

    threshold = 0.667 
    #cv2.TM_CCOEFF_NORMED
    #0.667 - 16px
    #0.697 - 10px
    if width <= 16:
        threshold = 0.667 
    elif width <= 10:
        threshold = 0.697
    elif width <= 20:
        threshold = 0.70
    elif width <= 25:
        threshold = 0.75
    elif width <= 35:
        threshold = 0.80
    elif width <= 40:
        threshold = 0.85
    else:
        threshold = 0.9
        
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(imageBase, pt, (pt[0] + width, pt[1] + height), (0,0,255), 2)

    filtered = imageBase

    return filtered