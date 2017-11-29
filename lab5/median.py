import cv2
import matplotlib.pyplot as ppl
import numpy as np

lena = cv2.imread("PrzetWst/lena.bmp", cv2.IMREAD_GRAYSCALE)

lena_prog = lena


for x in range(100):
    lena_median = cv2.medianBlur(lena_prog,5)
    lena_prog = lena_median

ppl.imshow(lena,cmap="gray")
ppl.figure("median")
ppl.imshow(lena_prog, cmap="gray")
ppl.show()