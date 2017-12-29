import cv2
import matplotlib.pyplot as ppl
import lab7.morf_B as B
import numpy as np



img = cv2.imread("Morfologia/calculator.bmp",cv2.IMREAD_GRAYSCALE)

elem = np.ones((1,71))
marker = cv2.erode(img,elem)
recons = B.img_reconstruct(img,marker)
diff = img - recons
class_top_hat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,elem)

elem2 = np.ones((1,11))
marker2 = cv2.erode(diff,elem2)
recons2 = B.img_reconstruct(diff,marker2)

elem3 = np.ones((1,21))
pre_marker3 = cv2.dilate(recons2,elem3)
marker3 = cv2.min(pre_marker3,diff)

res = B.img_reconstruct(diff,marker3)

ppl.subplot(221)
B.imshow_gray(recons)
ppl.subplot(222)
B.imshow_gray(diff)
ppl.subplot(223)
B.imshow_gray(class_top_hat)
ppl.subplot(224)
B.imshow_gray(recons2)
ppl.show()
ppl.figure("res")
B.imshow_gray(res)
ppl.show()

