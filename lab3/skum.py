from  PIL import Image
import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np

from lab3 import utils

lena1 = mpimg.imread("Histogram/lena1.bmp")



ppl.subplot(221)
v = ppl.hist(lena1.flatten(),bins=256,range=(0,255))
chs = utils.cum_hist(v)
ln = Image.fromarray(lena1)
lut = utils.get_lut_t(chs)
rec = ln.point(lut)
ppl.subplot(223)
qp = ppl.hist(np.asarray(rec).flatten(),bins=256,range=(0,255))
ppl.subplot(222)
ppl.imshow(ln,cmap="gray")
ppl.subplot(224)
ppl.imshow(rec,cmap="gray")
ppl.show()