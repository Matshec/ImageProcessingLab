import numpy as np
import matplotlib.pyplot as ppl
import skimage.transform as trans
import math as m
import cv2


# def y(x, thet, rho):
#     y = []
#     for v in x:
#         val = (rho - v * m.cos(thet)) / m.sin(thet)
#         y.append(val)
#     return y

def y(v: float, th: float, rho: float) -> float:
    v = float(v)
    th = float(th)
    rho = float(rho)
    return (rho - v * m.cos(th)) / m.sin(th)


img0 = np.zeros((11, 11), dtype=np.uint8)
img0[1][1] = 1
img0[1][3] = 1
img0[4][3] = 1
img0[2][6] = 1
# tylko dla przestreni
hspace, angles, distances = trans.hough_line(img0)
edges = cv2.Laplacian(img0, ddepth=-1)
# do narysowania linii
lines = cv2.HoughLines(edges, 20, np.pi / 180.0, 70, np.array([]), 0, 0)

x = np.arange(0, 10, 0.1)

ppl.figure(1)
ppl.plot(hspace)
ppl.show()
ppl.figure(2)
# max1 (th = 15,ro=3)
print(y(x[0], 15, 3))
# y = y(x, angles[15], distances[3])
x0 = int(x[0])
xe = int(x[len(x) - 1])
y0 = int(y(x0, 15, 3))
ye = int(y(xe, 15, 3))
print(x0, xe)
lineStart = (x0, y0)
lineEnd = (xe, ye)
ppl.imshow(img0, cmap="gray")
ppl.show()
cv2.line(img0, lineStart,lineEnd, (255, 0, 0), 1)
ppl.figure("x")
ppl.imshow(img0)
ppl.show()
# height, width = img0.shape

# for rho, theta in lines[0]:
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + height * (-b))
#     y1 = int(y0 + height * (a))
#     x2 = int(x0 - height * (-b))
#     y2 = int(y0 - height * (a))
#
#     cv2.line(img0, (x1,y1), (x2,y2), (0, 255, 0), 1)
#
# cv2.imwrite('kwadraty1.jpg', img0)
