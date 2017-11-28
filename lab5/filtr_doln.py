import cv2
import matplotlib.pyplot as ppl
import numpy as np

plansz_im = cv2.imread("PrzetWst/plansza.bmp")

paper_mask = np.array([[1,2,1],[2,4,2],[1,2,1]])
paper_mask = paper_mask / np.sum(paper_mask)

def get_avr_kern(size):
    return np.ones((size,size),np.float32) / size**2

def appl_mask(im, kern):
    dst = cv2.filter2D(im, -1, kern)
    diff = cv2.absdiff(im, dst)
    #ppl.subplot(221)
    ppl.figure(2)
    ppl.imshow(im)
    ppl.figure(3)
    #ppl.subplot(222)
    ppl.imshow(dst)
    #ppl.subplot(223)
    ppl.figure(4)
    ppl.imshow(diff)
    ppl.show()


#tworzenie kernela/maski n x n
# mask_3 = get_avr_kern(3)
# appl_mask(plansz_im,mask_3)
# mask_5 = get_avr_kern(5)
# appl_mask(plansz_im,mask_5)
gauss_kern = cv2.getGaussianKernel(5, 0.5)
ppl.figure(1)
ppl.plot(gauss_kern)
ppl.figure(2)
appl_mask(plansz_im,paper_mask)


