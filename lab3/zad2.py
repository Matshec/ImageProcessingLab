import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np
from lab3 import utils



hist_im = mpimg.imread("Histogram/hist1.bmp")

#hold  depricated
ppl.hold(True)
v = ppl.hist(hist_im.flatten(),bins=256,range=(0,255))
hq = utils.cum_hist(v)
ppl.plot(hq)
ppl.hold(False)
ppl.show()
