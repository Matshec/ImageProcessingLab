import cv2
import matplotlib.pyplot as plt
import numpy as np
import pymorph as morph

#pymorph działa tylko  z pythonem 2.x
def imshow_gray(img, title='', sub1=0, sub2=0, sub3=0):
    if sub1 != 0 and sub2 != 0 and sub3 != 0:
        plt.subplot(sub1, sub2, sub3)
    elif title != '':
        plt.title(title)
    plt.imshow(img, cmap='gray')


img = cv2.imread('KrawedzieHough/lab112.png', cv2.IMREAD_GRAYSCALE)
ret, threshold = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

kernel = np.ones((1, 100))

dilate = morph.infrec(cv2.bitwise_not(cv2.dilate(threshold, kernel)), img)

edges = cv2.Canny(dilate, 20, 70)

imshow_gray(img, 'org', 1, 2, 1)
imshow_gray(edges, 'kraw', 1, 2, 2)
plt.show()

minLineLength = 100
maxLineGap = 10

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 10, minLineLength, maxLineGap)

#rysuj wykres
plt.scatter(lines[0][:, 1], lines[0][:, 0])
plt.show()

img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

#rysuj linie
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

plt.imshow(img)
plt.show()
