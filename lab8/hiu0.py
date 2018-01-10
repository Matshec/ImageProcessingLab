import numpy as np
import matplotlib.pyplot as ppl
import skimage.transform as trans
import math as m


def y(x, thet, rho):
    y = []
    for v in x:
        val = (rho - v * m.cos(thet)) / m.sin(thet)
        y.append(val)
    return y


img0 = np.zeros((11, 11), dtype=bool)
img0[1][1] = 1
img0[1][3] = 1
img0[4][3] = 1
img0[2][6] = 1
hspace, angles, distances = trans.hough_line(img0)
x = np.arange(0, 10, 0.1)
# max1 (th = 15,ro=3)
y = y(x,angles[15],distances[3])
print(y)
ppl.imshow(img0)
ppl.plot(x,y)
ppl.show()
