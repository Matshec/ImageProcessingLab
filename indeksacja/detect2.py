import numpy as np
import cv2
import matplotlib.pyplot as ppl
img = cv2.imread('ccl/shapes.png',cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

im2, contours,h = cv2.findContours(thresh,1,2)

ppl.imshow(im2,cmap="gray")
ppl.title("from find conturs")
ppl.show()

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==4:
        print("square")
        cv2.drawContours(img,[cnt],0,(0,0,255),2)
    elif len(approx) == 12:
        print("plus")
        cv2.drawContours(img,[cnt],0,(255,255,0),2)
    elif len(approx) > 13:
        print("circle")
        cv2.drawContours(img,[cnt],0,(0,255,255),2)

ppl.figure(3)
ppl.imshow(img)
ppl.show()