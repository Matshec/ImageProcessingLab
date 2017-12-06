import cv2
import matplotlib.pyplot as ppl
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.io  as sio

plansz_im = cv2.imread("PrzetWst/lenaSzum.bmp")

paper_mask = np.array([[1,2,1],[2,4,2],[1,2,1]])
paper_mask = paper_mask / np.sum(paper_mask)


def plot_grid(ar):
    nx, ny = ar.shape
    print(ar.shape)
    x = range(nx)
    y = range(ny)
    hf = ppl.figure()
    ha = hf.add_subplot(111,projection='3d')
    X, Y = np.meshgrid(x,y)
    ha.plot_surface(X,Y,ar)
    ppl.show()

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


def my_gaus():
    im1 = cv2.GaussianBlur(plansz_im, (5, 5), 0.5)
    im2 = cv2.GaussianBlur(plansz_im, (5, 5), 0.3)
    im3 = cv2.GaussianBlur(plansz_im, (5, 5), 1.2)
    ppl.subplot(221)
    ppl.imshow(im1)
    ppl.subplot(222)
    ppl.imshow(im2)
    ppl.subplot(223)
    ppl.imshow(im3)
    ppl.show()

#tworzenie kernela/maski n x n
#mask_3 = get_avr_kern(3)
#appl_mask(plansz_im,mask_3)

# mask_5 = get_avr_kern(5)
# appl_mask(plansz_im,mask_5)

#appl_mask(plansz_im,paper_mask)




#my_gaus()



#rozne maski
masks_5(plansz_im)

