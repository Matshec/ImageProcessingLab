import cv2
import matplotlib.pyplot as ppl
import numpy as np

def imshow_(img, title='', sub1=0, sub2=0, sub3=0):
    if sub1 != 0:
        ppl.subplot(sub1, sub2, sub3)
    if title != '':
        ppl.title(title)
    ppl.imshow(img, cmap='gray')

img = cv2.imread('KrawedzieHough/lab112.png', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, 20, 70)


imshow_(img, 'original', 1, 2, 1)
imshow_(edges, 'edges', 1, 2, 2)
ppl.show()

minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 10, minLineLength, maxLineGap)

ppl.scatter(lines[0][:, 1], lines[0][:, 0])
ppl.show()

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(img, (x1,y1), (x2,y2), (0, 255, 0), 2)

ppl.imshow(img)
ppl.show()