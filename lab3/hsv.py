from  PIL import Image
import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np
from lab3 import  utils



HSV_lena = Image.open("Histogram/lenaRGB.bmp")
HSV_lena  = HSV_lena.convert("HSV")



ppl.figure(2)

np_HSV = np.asarray(HSV_lena)
lenaH = np_HSV[:, :, 0]
lenaS = np_HSV[:, :, 1]
lenaV = np_HSV[:, :, 2]

ppl.subplot(241)
H_hist = ppl.hist(lenaH.flatten(), bins=256, range=(0, 255))
ppl.subplot(242)
S_hist = ppl.hist(lenaS.flatten(), bins=256, range=(0, 255))
ppl.subplot(243)
V_hist = ppl.hist(lenaV.flatten(), bins=256, range=(0, 255))

cum_V = utils.cum_hist(V_hist)
lut_v = utils.get_lut_t(cum_V)
rec_V = Image.fromarray(lenaV).point(lut_v)

rec_lenaHSV = Image.merge("HSV",(Image.fromarray(lenaH),Image.fromarray(lenaS),rec_V))
#rec_lenaHSV = cv2.cvtColor(np.asarray(rec_lenaHSV),cv2.COLOR_HSV2RGB)
rec_lenaHSV = rec_lenaHSV.convert(mode="RGB")
HSV_lena.convert(mode="RGB").show()
rec_lenaHSV.show()