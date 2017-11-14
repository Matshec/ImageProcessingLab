from  PIL import Image
import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np


# from lab2.recode import append_to_pyplot


def cum_hist(hs):
    x, y, z = hs
    base_max = np.amax(x)
    cum = np.cumsum(x)
    cum_max = np.amax(cum)
    k = cum_max / base_max
    return np.divide(cum, k)


def get_lut_t(cum_hist):
    def distrib(n, chst):
        return chst[n] / chst[len(chst) - 1]

    lt = []
    non_zer_min = np.min(cum_hist[np.nonzero(cum_hist)])
    k = len(cum_hist)
    for x in range(len(cum_hist)):
        val = ((distrib(x, cum_hist) - non_zer_min) / (1 - non_zer_min)) * (k - 1)
        lt.append(val)
    return lt


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


lena1 = mpimg.imread("Histogram/lena1.bmp")
lena2 = mpimg.imread("Histogram/lena2.bmp")
lena3 = mpimg.imread("Histogram/lena3.bmp")
lena4 = mpimg.imread("Histogram/lena4.bmp")
hist_im = mpimg.imread("Histogram/hist1.bmp")
lenaRGB = mpimg.imread("Histogram/lenaRGB.bmp")

# zad 1
# lenas_hist([lena1,lena2,lena3,lena4])

# zad 2

# #wywala błedy bo hold depricated
# ppl.hold(True)
# v = ppl.hist(hist_im.flatten(),bins=256,range=(0,255))
# hq = cum_hist(v)
# ppl.plot(hq)
# ppl.hold(False)
# ppl.show()

# #skum
# v = ppl.hist(lena1.flatten(),bins=256,range=(0,255))
# chs = cum_hist(v)
# ln = Image.fromarray(lena1)
# lut = get_lut_t(chs)
# rec = ln.point(lut)
# ppl.figure(2)
# qp = ppl.hist(np.asarray(rec).flatten(),bins=256,range=(0,255))
# ppl.show()
# ln.show()
# rec.show()


##rgb 1
lenaR = lenaRGB[:, :, 0]
lenaG = lenaRGB[:, :, 1]
lenaB = lenaRGB[:, :, 2]

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

cum_lrh = cum_hist(lrh)
cum_lgh = cum_hist(lgh)
cum_lbh = cum_hist(lbh)

r_lut = get_lut_t(cum_lrh)
g_lut = get_lut_t(cum_lgh)
b_lut = get_lut_t(cum_lbh)


rec_r = Image.fromarray(lenaR).point(r_lut)
rec_g = Image.fromarray(lenaG).point(g_lut)
rec_b = Image.fromarray(lenaB).point(b_lut)

ret = Image.merge("RGB",(rec_r,rec_g,rec_b))
ret.show()

# #HSV
ppl.figure(2)
HSV_lena = Image.fromarray(lenaRGB,mode="HSV")
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

cum_V = cum_hist(V_hist)
lut_v = get_lut_t(cum_V)
rec_V = Image.fromarray(lenaV).point(lut_v)

rec_lenaHSV = Image.merge("HSV",(Image.fromarray(lenaH),Image.fromarray(lenaS),rec_V))
ppl.figure(3)
ppl.imshow(rec_lenaHSV)
ppl.figure(4)
ppl.imshow(HSV_lena)


ppl.show()
