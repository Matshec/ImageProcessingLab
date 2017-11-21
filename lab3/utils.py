from  PIL import Image
import matplotlib.pyplot as ppl
import matplotlib.image as mpimg
import numpy as np
import cv2
import tkinter
import scipy.io as sio
import bisect
import  matplotlib.colors as col


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

