import cv2
import matplotlib.pyplot as ppl
import numpy as np


base_mask = np.array([[0, 1,0],[1,-4,1],[0,1,0]])
base_mask = base_mask / 9

lena = cv2.imread("PrzetWst/moon.bmp", cv2.IMREAD_GRAYSCALE)
lena_pap_lap = cv2.filter2D(lena,-1,base_mask)

ppl.imshow(lena_pap_lap,cmap="gray")

lena_lap = cv2.Laplacian(lena,-1)
im_sum = lena_lap + lena
ppl.imshow(lena, cmap="gray")
ppl.figure(2)
ppl.imshow(lena_lap, cmap="gray")
ppl.figure(3)
ppl.imshow(im_sum,cmap="gray")
ppl.show()