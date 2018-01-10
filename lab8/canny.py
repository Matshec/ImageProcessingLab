import cv2
import matplotlib.pyplot as ppl


img = cv2.imread("KrawedzieHough/dom.png", cv2.IMREAD_GRAYSCALE)

ret = cv2.Canny(img,100,200)
ppl.imshow(ret,cmap="gray")
ppl.show()