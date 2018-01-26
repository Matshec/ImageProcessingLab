import cv2
import matplotlib.pyplot as ppl
import numpy as np
import skimage.color as col


def nonzero(arr):
    return list(filter(lambda z: z != 0, arr))


def root(index, array):
    tmp = index
    while tmp != array[tmp]:
        tmp = array[tmp]
    return tmp


def union(p, q, array):
    if p <= q:
        array[root(p, array)] = root(q, array)


img = cv2.imread("ccl/ccl1.png", cv2.IMREAD_GRAYSCALE)

##id[i] jest rodzicem i
id = list(range(0, 101))

Y, X = img.shape  # (259,598)

L = 1

for y in range(1, Y):
    for x in range(1, X - 1):
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
                ## robi to samo, ale to rózne przypadki
                if min_res == max_res:  ## przypadek b
                    img[y, x] = min_res
                else:  ## przypadek c
                    img[y, x] = min_res
                    union(min_res, max_res, id)
##drugi przebieg

#
lut = np.zeros(101)

for v in range(1, 100):
    lut[v] = root(v, id)

for y in range(1, Y):
    for x in range(1, X - 1):
        if img[y, x] > 0:
            img[y, x] = lut[img[y, x]]

# print(lut)
# rgb = col.label2rgb(img)
ppl.imshow(img, cmap="gray")
ppl.show()



