from  PIL import Image
import matplotlib.pyplot as ppl
from lab3 import  utils
import matplotlib.image as mpimg


lenaRGB = mpimg.imread("Histogram/lenaRGB.bmp")


ppl.figure(1)
ppl.imshow(lenaRGB)
lenaR = lenaRGB[:, :, 0]
lenaG = lenaRGB[:, :, 1]
lenaB = lenaRGB[:, :, 2]

ppl.figure(2)
ppl.subplot(241)
ppl.imshow(lenaR,cmap="gray")
ppl.title("Red")
ppl.subplot(242)
lrh = ppl.hist(lenaR.flatten(), bins=256, range=(0, 255))
ppl.subplot(243)
ppl.imshow(lenaG,cmap="gray")
ppl.title("green")
ppl.subplot(244)
lgh = ppl.hist(lenaG.flatten(), bins=256, range=(0, 255))
ppl.subplot(245)
ppl.imshow(lenaB,cmap="gray")
ppl.title("blue")
ppl.subplot(246)
lbh = ppl.hist(lenaB.flatten(), bins=256, range=(0, 255))

cum_lrh = utils.cum_hist(lrh)
cum_lgh = utils.cum_hist(lgh)
cum_lbh = utils.cum_hist(lbh)

r_lut = utils.get_lut_t(cum_lrh)
g_lut = utils.get_lut_t(cum_lgh)
b_lut = utils.get_lut_t(cum_lbh)


rec_r = Image.fromarray(lenaR).point(r_lut)
rec_g = Image.fromarray(lenaG).point(g_lut)
rec_b = Image.fromarray(lenaB).point(b_lut)

ret = Image.merge("RGB",(rec_r,rec_g,rec_b))
ppl.figure(3)
ppl.imshow(ret)
ppl.show()