import cv2
import matplotlib.pyplot as ppl
import numpy as np
import scipy.io as sio

kw_im = cv2.imread("PrzetWst/jet.bmp")
masks = sio.loadmat("PrzetWst/maskiPP.mat")


rob1_im = cv2.filter2D(kw_im,-1,masks["R1"])
rob2_im = cv2.filter2D(kw_im,-1,masks["R2"])


prev1_im = cv2.filter2D(kw_im,-1,masks["P1"])
prev2_im = cv2.filter2D(kw_im,-1,masks["P2"])

sob1_im = cv2.filter2D(kw_im,-1,masks["S1"])
sob2_im = cv2.filter2D(kw_im,-1,masks["S2"])

ppl.figure(1)
ppl.imshow(kw_im)
ppl.show()

ppl.figure(2)
ppl.subplot(331)
ppl.imshow(rob1_im)
ppl.title("rob1")
ppl.subplot(332)
ppl.imshow(rob2_im)
ppl.title("rob2")
ppl.subplot(333)
ppl.imshow(prev1_im)
ppl.title("prev1")
ppl.subplot(334)
ppl.imshow(prev2_im)
ppl.title("prev2")
ppl.subplot(335)
ppl.imshow(sob1_im)
ppl.title("sob1")
ppl.subplot(336)
ppl.imshow(sob2_im)
ppl.title("sob2")
ppl.show()

def comb_fil_square(im,mask1,mask2):
    print(mask1)
    print(mask2)
    proc_1 = cv2.filter2D(im,-1,mask1)
    proc_2 = cv2.filter2D(im,-1,mask2)
    #konieczne rzutowanie na  wiekszą zmienna przed wykonaniem operacji
    proc_1 = proc_1.astype(np.uint32)
    proc_2 = proc_2.astype(np.uint32)
    temp = np.sqrt(np.square(proc_1) + np.square(proc_2))
    return temp.astype(np.uint8)


def comb_fil_abs(im,mask1,mask2):
    proc_1 = cv2.filter2D(im,-1,mask1)
    proc_2 = cv2.filter2D(im,-1,mask2)
    return np.abs(proc_1) + np.abs(proc_2)

cm_sqr_im = comb_fil_square(kw_im,masks["S1"],masks["S2"])
cm_abs_im = comb_fil_abs(kw_im,masks["S1"],masks["S2"])


ppl.figure(3)
ppl.subplot(311)
ppl.imshow(kw_im)
ppl.subplot(312)
ppl.imshow(cm_sqr_im)
ppl.title("kwadrat")
ppl.subplot(313)
ppl.imshow(cm_abs_im)
ppl.title("modul")
ppl.show()