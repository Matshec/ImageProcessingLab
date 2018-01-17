import numpy as np
import cv2
import matplotlib.pyplot as ppl

# configurables:
# DIV_LIMIT = 8
# MAX_DEV = 0.05


img = cv2.imread("segmentation/umbrealla.png", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img = np.asarray(img, dtype=np.double)
H, S, V = cv2.split(img)
print(img.shape)


# globalles
# el


class Divider:
    def __init__(self, img, Division_lim, Max_divs):
        self.img = img
        self.serRes = np.zeros(img.shape, dtype=np.uint8)
        self.MRes = np.zeros(img.shape, dtype=np.uint8)
        self.index = 1
        self.DIV_LIMIT = Division_lim
        self.MAX_DEV = Max_divs

    def split(self, img, co1x, co2x, co3y, co4y):
        ROI = img[co1x:co2x, co3y:co4y]
        mean = np.mean(ROI)
        std = np.std(ROI)
        size = np.abs(co2x - co1x)
        if std > self.MAX_DEV and size > self.DIV_LIMIT:
            # do split
            nco1 = co1x
            nco2 = co2x // 2
            nco3 = co3y
            nco4 = co4y // 2
            self.split(img, nco1, nco2, nco3, nco4)
            self.split(img, nco2, co2x, nco4, co4y)
            self.split(img, nco1, nco2, nco4, co4y)
            self.split(img, nco2, co2x, nco4, co4y)

        else:
            self.serRes[co1x:co2x, co3y:co4y] = self.index
            self.index = self.index + 1
            self.MRes[co1x:co2x, co3y:co4y] = mean



