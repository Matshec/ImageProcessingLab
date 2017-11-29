import cv2
import matplotlib.pyplot as ppl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plansz_im = cv2.imread("PrzetWst/lena.bmp")

paper_mask = np.array([[1,2,1],[2,4,2],[1,2,1]])
paper_mask = paper_mask / np.sum(paper_mask)


def get_avr_kern(size):
    return np.ones((size,size),np.float32) / size**2

def appl_mask(im, kern):
    dst = cv2.filter2D(im, -1, kern)
    diff = cv2.absdiff(im, dst)
    ppl.subplot(221)
    ppl.imshow(im)
    ppl.subplot(222)
    ppl.imshow(dst)
    ppl.subplot(223)
    ppl.imshow(diff)
    ppl.show()



def dif_win(im,kern,subpl):
    rt = cv2.filter2D(im, -1, kern)
    ppl.subplot(subpl)
    ppl.imshow(rt)

def masks_5(im):
    ppl.figure(2)
    dif_win(im,get_avr_kern(3),231)
    dif_win(im, get_avr_kern(5),232)
    dif_win(im, get_avr_kern(9),233)
    dif_win(im, get_avr_kern(15),234)
    dif_win(im, get_avr_kern(35),235)
    ppl.show()



#tworzenie kernela/maski n x n
# mask_3 = get_avr_kern(3)
# appl_mask(plansz_im,mask_3)


#appl_mask(plansz_im,paper_mask)

# mask_5 = get_avr_kern(5)
# appl_mask(plansz_im,mask_5)

# gauss_kern1 = cv2.getGaussianKernel(5, 0.5)
# gauss_kern2 = cv2.getGaussianKernel(5, 0.3)
# gauss_kern3 = cv2.getGaussianKernel(5, 0.7)
# ppl.figure(1)
# im1 = cv2.filter2D(plansz_im, -1,gauss_kern1)
# im2 = cv2.filter2D(plansz_im, -1,gauss_kern2)
# im3 = cv2.filter2D(plansz_im, -1,gauss_kern3)
# ppl.subplot(221)
# ppl.imshow(im1)
# ppl.subplot(222)
# ppl.imshow(im2)
# ppl.subplot(223)
# ppl.imshow(im3)
# ppl.show()







#rozne maski
# masks_5(plansz_im)
