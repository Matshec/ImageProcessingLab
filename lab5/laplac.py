import cv2
import matplotlib.pyplot as ppl
import numpy as np


lena = cv2.imread("PrzetWst/lena.bmp", cv2.IMREAD_GRAYSCALE)
lena_lap = cv2.Laplacian(lena,-1)
im_sum = lena_lap + lena
ppl.imshow(lena, cmap="gray")
ppl.figure(2)
ppl.imshow(lena_lap, cmap="gray")
ppl.figure(3)
ppl.imshow(im_sum,cmap="gray")
ppl.show()