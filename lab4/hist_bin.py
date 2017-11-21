import cv2
import matplotlib.pyplot as ppl
import numpy as np

coins_im = cv2.imread("Binaryzacja/katalog.bmp", cv2.IMREAD_GRAYSCALE)

ppl.subplot(211)
ppl.imshow(coins_im,cmap="gray")
ppl.subplot(212)
ppl.hist(coins_im.flatten(),bins=256)

my_thresh = 100
ret1,bin_coins= cv2.threshold(coins_im,my_thresh,255,cv2.THRESH_BINARY)
#coins 120
#rice 140
#tekst 160
#obiekty 140
#katalog ? 
otsu_thres, otsu_im = cv2.threshold(coins_im,0,255,cv2.THRESH_OTSU)
print(otsu_thres)
ppl.figure(2)
ppl.subplot(211)
ppl.imshow(bin_coins,cmap="gray")
ppl.title("my: "+ str(my_thresh))
ppl.subplot(212)
ppl.imshow(otsu_im,cmap="gray")
ppl.title("otsu: "+str(otsu_thres))
ppl.show()

