import cv2
import scipy.io as sio
from lab3 import utils

phobos = cv2.imread("Histogram/phobos.bmp",cv2.IMREAD_GRAYSCALE)


eq_phobos = cv2.equalizeHist(phobos)
hist_zad = sio.loadmat("Histogram/histogramZadany.mat")["histogramZadany"].flatten()
cv2.imshow("preEq",phobos)
cv2.imshow("postEq", eq_phobos)

adj_phobos = utils.imadjust(phobos)
cv2.imshow("adjusted",adj_phobos)


clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(phobos)
cv2.imshow("CLahe",cl1)



cv2.waitKey(0)
cv2.destroyAllWindows()