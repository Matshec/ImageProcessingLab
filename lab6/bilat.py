import cv2
from scipy import io
from scipy import signal
import numpy as np

import matplotlib.pyplot as ppl

data = io.loadmat("bila/MR_data.mat")

def get_distance(pix_a,pix_b):
    a_x, a_y = pix_a
    b_x, b_y = pix_b
    return np.sqrt(np.square(b_x - a_x) + np.square(b_y - a_y))

def gauss_func(y,sigma):
    return np.exp(- (y**2) / (2 * sigma ** 2) )




def bilateral_filt(im,diam,sigma1,sigma2):
    hd = diam // 2
    dest = im.copy()
    def my_bilater(x,y):
        if hd % 2 != 0:
            raise Exception("must be odd")
        norm_sum = 0
        dest_val = 0
        for i in range(diam):
            for j in range(diam):
                nei_x = x - (hd - i)
                nei_y = y - (hd - j)
                if nei_x >= len(im):
                    nei_x -= len(im)
                if nei_y >= len(im[0]):
                    nei_y -= len(im[0])
                gaus_one = gauss_func(im[nei_x][nei_y] - im[x][y],sigma1)
                gaus_two = gauss_func(get_distance((nei_x,nei_y),(x,y)),sigma2)

                prod = gaus_one * gaus_two

                dest_val += im[nei_x][nei_y] * prod

                norm_sum += prod

        dest_val /= norm_sum

        return int(round(dest_val))


    h, w= im.shape
    for x in range(w):
        for y in range(h):
            dest[x][y] = my_bilater(x,y)

    return dest


ppl.subplot(1, 2, 1)
ppl.imshow(data["I_noisy1"], cmap='gray')
ppl.subplot(1, 2, 2)
ppl.imshow(bilateral_filt(data["I_noisy1"], 5, 20, 10), cmap='gray')
ppl.show()
