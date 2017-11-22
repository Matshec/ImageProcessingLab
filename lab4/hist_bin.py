import cv2
import matplotlib.pyplot as ppl
import numpy as np

#z githuba
def kittler(im):
    """
    The reimplementation of Kittler-Illingworth Thresholding algorithm by Bob Pepin
    Works on 8-bit images only
    Original Matlab code: https://www.mathworks.com/matlabcentral/fileexchange/45685-kittler-illingworth-thresholding
    Paper: Kittler, J. & Illingworth, J. Minimum error thresholding. Pattern Recognit. 19, 41–47 (1986).
    """
    out = im.copy()
    h,g = np.histogram(im.ravel(),256,[0,256])
    h = h.astype(np.float)
    g = g.astype(np.float)
    g = g[:-1]
    c = np.cumsum(h)
    m = np.cumsum(h * g)
    s = np.cumsum(h * g**2)
    sigma_f = np.sqrt(s/c - (m/c)**2)
    cb = c[-1] - c
    mb = m[-1] - m
    sb = s[-1] - s
    sigma_b = np.sqrt(sb/cb - (mb/cb)**2)
    p =  c / c[-1]
    v = p * np.log(sigma_f) + (1-p)*np.log(sigma_b) - p*np.log(p) - (1-p)*np.log(1-p)
    v[~np.isfinite(v)] = np.inf
    idx = np.argmin(v)
    t = g[idx]
    out[:,:] = 0
    out[im >= t] = 255
    return t, out




coins_im = cv2.imread("Binaryzacja/coins.png", cv2.IMREAD_GRAYSCALE)


my_thresh =  80
ret1,bin_coins= cv2.threshold(coins_im,my_thresh,255,cv2.THRESH_BINARY)
#coins 80
#rice 140
#tekst 160
#obiekty 140
#katalog ? 
otsu_thres, otsu_im = cv2.threshold(coins_im,0,255,cv2.THRESH_OTSU)

#kittler_im = coins_im.copy()
kit_th, kittler_im = kittler(coins_im)
print(kit_th)

ppl.figure(231)
ppl.subplot(231)
ppl.imshow(bin_coins,cmap="gray")
ppl.title("my: "+ str(my_thresh))
ppl.subplot(232)
ppl.imshow(otsu_im,cmap="gray")
ppl.title("otsu: "+str(otsu_thres))
ppl.subplot(234)
ppl.imshow(kittler_im,cmap="gray")
ppl.title("kittler: " + str(kit_th))
ppl.subplot(235)
ppl.imshow(coins_im,cmap="gray")
ppl.title("basic")
ppl.subplot(236)
ppl.hist(coins_im.flatten(),bins=256,range=(0,255))
ppl.show()

