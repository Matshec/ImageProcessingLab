import cv2
import matplotlib.pyplot as ppl
import numpy as np

lena = cv2.imread("PrzetWst/lenaSzum.bmp", cv2.IMREAD_GRAYSCALE)



lena_median = cv2.medianBlur(lena,5)
ppl.figure(1)
ppl.imshow(lena_median,cmap="gray")
ppl.show()
lena_prog = lena


for x in range(10):
    lena_median = cv2.medianBlur(lena_prog,5)
    lena_prog = lena_median

ppl.figure(2)
ppl.imshow(lena,cmap="gray")
ppl.figure("median")
ppl.imshow(lena_prog, cmap="gray")
ppl.show()