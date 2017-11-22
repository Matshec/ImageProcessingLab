import cv2
import matplotlib.pyplot as ppl
import numpy as np

plansz_im = cv2.imread("PrzetWst/plansza.bmp")

gaus_kern = cv2.getGaussianKernel(5,0.7)
print(gaus_kern)

raw_pap_mask = np.array([[1, 2, 1], [2, 4, 2],[1, 2 ,1]])
pap_mask = np.divide(raw_pap_mask, np.sum(raw_pap_mask))
#tworzenie kernela/maski
kernel = np.ones((3,3),np.float32)/25
dst = cv2.filter2D(plansz_im,-1,kernel)
dst2 = cv2.filter2D(plansz_im,-1,pap_mask)
diff = cv2.subtract(plansz_im,dst)
ppl.imshow(dst)
ppl.figure("diff")
ppl.imshow(diff)
ppl.figure("pap")
ppl.imshow(dst2)
ppl.show()