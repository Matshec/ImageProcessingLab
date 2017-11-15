import cv2
import matplotlib.pyplot as ppl
import tkinter

coins_im = cv2.imread("Binaryzacja/coins.png")
ppl.subplot(211)
ppl.imshow(coins_im)
ppl.subplot(212)
ppl.hist(coins_im.flatten(),bins=256)
ppl.show()