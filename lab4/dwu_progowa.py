import cv2
import matplotlib.pyplot as ppl
import numpy as np


bart = cv2.imread("Binaryzacja/bart.bmp",cv2.IMREAD_GRAYSCALE)

# ok - 203 kolor skory
ppl.imshow(bart,cmap="gray")
ppl.figure(2)
ppl.hist(bart.flatten(),bins=256)


cpy = bart.copy()
low_thr = 180
upp_thr = 210

imIt = np.nditer(bart, flags=["multi_index"])
while not imIt.finished:
    y, x = imIt.multi_index

    if low_thr < imIt[0] < upp_thr:
        cpy[y][x] = 1
    else:
        cpy[y][x] = 0

    imIt.iternext()

ppl.figure(3)
ppl.imshow(cpy,cmap="gray")
ppl.show()


