import cv2
import matplotlib.pyplot as ppl
import numpy as np
import skimage.color as col

def nonzero(arr):
   return list(filter(lambda z: z != 0, arr))


img = cv2.imread("ccl/ccl1.png", cv2.IMREAD_GRAYSCALE)

img[258,597]
Y,X = img.shape #(259,598)

L = 1

for y in range(1, Y):
    for x in range(1, X -1):
        if img[y, x] != 0:
            neigbours = [img[y - 1, x - 1], img[y - 1, x], img[y - 1, x + 1], img[y, x - 1]]
            nei_sum = sum(neigbours)
            if nei_sum == 0:
                img[y, x] = L
                L = L + 1
            else:
                nonz_nei = nonzero(neigbours)
                min_res = np.amin(nonz_nei)
                max_res = np.amax(nonz_nei)
                # print(nonz_nei)
                # print(min_res,max_res)
                # robi to samo, ale to rózne przypadki
                if min_res == max_res:
                    img[y, x] = min_res
                else:
                    img[y, x] = min_res


ppl.imshow(img,cmap="gray")
ppl.show()
