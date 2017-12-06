import cv2
import matplotlib.pyplot as ppl
import numpy as np

base_mask = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
base_mask = base_mask / 9

lena = cv2.imread("PrzetWst/moon.bmp", cv2.IMREAD_GRAYSCALE)
lena_pap_lap = cv2.filter2D(lena, -1, base_mask)

# scaling
scl_add = lena_pap_lap + 128
scl_abs = np.abs(lena_pap_lap)
ppl.figure(1)
ppl.subplot(221)
ppl.imshow(lena, cmap="gray")
ppl.subplot(222)
ppl.imshow(lena_pap_lap, cmap="gray")
ppl.subplot(223)
ppl.imshow(scl_add, cmap="gray")
ppl.subplot(224)
ppl.imshow(scl_abs, cmap="gray")
ppl.show()

# normalizacje są chyba wbudowane w metody

ppl.figure(2)
ppl.subplot(221)
lena_lap = cv2.Laplacian(lena, -1)
im_sum = lena_lap + lena
ppl.imshow(lena, cmap="gray")
ppl.subplot(222)
ppl.imshow(lena_lap, cmap="gray")
ppl.subplot(223)
ppl.imshow(im_sum, cmap="gray")
ppl.show()
