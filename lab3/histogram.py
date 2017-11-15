from  PIL import Image
import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np
import cv2
import tkinter
import scipy.io as sio
import bisect
import  matplotlib.colors as col


def imadjust(src, tol=1, vin=[0,255], vout=(0,255)):
    # src : input one-layer image (numpy array)
    # tol : tolerance, from 0 to 100.
    # vin  : src image bounds
    # vout : dst image bounds
    # return : output img

    dst = src.copy()
    tol = max(0, min(100, tol))

    if tol > 0:
        # Compute in and out limits
        # Histogram
        hist = np.zeros(256, dtype=np.int)
        for r in range(src.shape[0]):
            for c in range(src.shape[1]):
                hist[src[r,c]] += 1
        # Cumulative histogram
        cum = hist.copy()
        for i in range(1, len(hist)):
            cum[i] = cum[i - 1] + hist[i]

        # Compute bounds
        total = src.shape[0] * src.shape[1]
        low_bound = total * tol / 100
        upp_bound = total * (100 - tol) / 100
        vin[0] = bisect.bisect_left(cum, low_bound)
        vin[1] = bisect.bisect_left(cum, upp_bound)

    # Stretching
    scale = (vout[1] - vout[0]) / (vin[1] - vin[0])
    for r in range(dst.shape[0]):
        for c in range(dst.shape[1]):
            vs = max(src[r,c] - vin[0], 0)
            vd = min(int(vs * scale + 0.5) + vout[0], vout[1])
            dst[r,c] = vd
    return dst

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
HSV_lena = Image.fromarray(lenaRGB,mode="HSV")
HSV_lena = Image.open("Histogram/lenaRGB.bmp")
HSV_lena  = HSV_lena.convert("HSV")


phobos = cv2.imread("Histogram/phobos.bmp",cv2.IMREAD_GRAYSCALE)


#
# ppl.hist(hist_im.flatten(),bins=256,range=(0,255))
# aq = imadjust(hist_im)
# ppl.figure(2)
# ppl.imshow(aq,cmap="gray")
# ppl.show()

#zad 1
#lenas_hist([lena1,lena2,lena3,lena4])

# zad 2

##wywala błedy bo hold depricated
# ppl.hold(True)
# v = ppl.hist(hist_im.flatten(),bins=256,range=(0,255))
# hq = cum_hist(v)
# ppl.plot(hq)
# ppl.hold(False)
# ppl.show()

# #skum
# ppl.subplot(221)
# v = ppl.hist(lena1.flatten(),bins=256,range=(0,255))
# chs = cum_hist(v)
# ln = Image.fromarray(lena1)
# lut = get_lut_t(chs)
# rec = ln.point(lut)
# ppl.subplot(223)
# qp = ppl.hist(np.asarray(rec).flatten(),bins=256,range=(0,255))
# ppl.subplot(222)
# ppl.imshow(ln,cmap="gray")
# ppl.subplot(224)
# ppl.imshow(rec,cmap="gray")
# ppl.show()
#

##rgb 1
# ppl.figure(1)
# ppl.imshow(lenaRGB)
# lenaR = lenaRGB[:, :, 0]
# lenaG = lenaRGB[:, :, 1]
# lenaB = lenaRGB[:, :, 2]
#
# ppl.figure(2)
# ppl.subplot(241)
# ppl.imshow(lenaR,cmap="gray")
# ppl.title("Red")
# ppl.subplot(242)
# lrh = ppl.hist(lenaR.flatten(), bins=256, range=(0, 255))
# ppl.subplot(243)
# ppl.imshow(lenaG,cmap="gray")
# ppl.title("green")
# ppl.subplot(244)
# lgh = ppl.hist(lenaG.flatten(), bins=256, range=(0, 255))
# ppl.subplot(245)
# ppl.imshow(lenaB,cmap="gray")
# ppl.title("blue")
# ppl.subplot(246)
# lbh = ppl.hist(lenaB.flatten(), bins=256, range=(0, 255))
#
# cum_lrh = cum_hist(lrh)
# cum_lgh = cum_hist(lgh)
# cum_lbh = cum_hist(lbh)
#
# r_lut = get_lut_t(cum_lrh)
# g_lut = get_lut_t(cum_lgh)
# b_lut = get_lut_t(cum_lbh)
#
#
# rec_r = Image.fromarray(lenaR).point(r_lut)
# rec_g = Image.fromarray(lenaG).point(g_lut)
# rec_b = Image.fromarray(lenaB).point(b_lut)
#
# ret = Image.merge("RGB",(rec_r,rec_g,rec_b))
# ppl.figure(3)
# ppl.imshow(ret)
# ppl.show()


# # #HSV
# ppl.figure(2)
#
# np_HSV = np.asarray(HSV_lena)
# lenaH = np_HSV[:, :, 0]
# lenaS = np_HSV[:, :, 1]
# lenaV = np_HSV[:, :, 2]
#
# ppl.subplot(241)
# H_hist = ppl.hist(lenaH.flatten(), bins=256, range=(0, 255))
# ppl.subplot(242)
# S_hist = ppl.hist(lenaS.flatten(), bins=256, range=(0, 255))
# ppl.subplot(243)
# V_hist = ppl.hist(lenaV.flatten(), bins=256, range=(0, 255))
#
# cum_V = cum_hist(V_hist)
# lut_v = get_lut_t(cum_V)
# rec_V = Image.fromarray(lenaV).point(lut_v)
#
# rec_lenaHSV = Image.merge("HSV",(Image.fromarray(lenaH),Image.fromarray(lenaS),rec_V))
# #rec_lenaHSV = cv2.cvtColor(np.asarray(rec_lenaHSV),cv2.COLOR_HSV2RGB)
# rec_lenaHSV = rec_lenaHSV.convert(mode="RGB")
# HSV_lena.convert(mode="RGB").show()
# rec_lenaHSV.show()

# #B

#
eq_phobos = cv2.equalizeHist(phobos)
hist_zad = sio.loadmat("Histogram/histogramZadany.mat")["histogramZadany"].flatten()
cv2.imshow("preEq",phobos)
cv2.imshow("postEq", eq_phobos)

adj_phobos = imadjust(phobos)
cv2.imshow("adjusted",adj_phobos)


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(phobos)
cv2.imshow("CLahe",cl1)



cv2.waitKey(0)
cv2.destroyAllWindows()

#
