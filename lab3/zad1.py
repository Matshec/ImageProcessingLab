from  PIL import Image
import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np
import bisect
from lab3 import utils


#src: stackoverflow

def lenas_hist(lenas):
    subv = 241
    ppl.figure(1)
    for x in lenas:
        ppl.subplot(subv)
        ppl.imshow(x, cmap="gray")
        subv = subv + 1
        ppl.subplot(subv)
        ppl.hist(x.flatten(), bins=256, range=(0, 255))
        subv = subv + 1
    ppl.show()


hist_im = mpimg.imread("Histogram/hist1.bmp")
lena1 = mpimg.imread("Histogram/lena1.bmp")
lena2 = mpimg.imread("Histogram/lena2.bmp")
lena3 = mpimg.imread("Histogram/lena3.bmp")
lena4 = mpimg.imread("Histogram/lena4.bmp")

ppl.hist(hist_im.flatten(),bins=256,range=(0,255))
aq = utils.imadjust(hist_im)
ppl.figure(2)
ppl.imshow(aq,cmap="gray")
ppl.show()

#zad 1
lenas_hist([lena1,lena2,lena3,lena4])