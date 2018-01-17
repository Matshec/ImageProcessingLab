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
    progKolorow = 5 / 255

    def __init__(self, img, Division_lim, Max_dev):
        self.img = img
        self.serRes = np.zeros(img.shape, dtype=np.uint8)
        self.MRes = np.zeros(img.shape, dtype=np.uint8)
        self.index = 1
        self.DIV_LIMIT = Division_lim
        self.MAX_DEV = Max_dev



    def start(self):
        self.split(self.img,0,255,0,255)
        self.join()

        U2 = np.unique(self.segRes)

        for i in  range(0 ,U2.size):
            C = self.segRes == U2[i]
            C = np.asarray(C,dtype=np.uint8)
            self.segRes[C] = i

        ppl.imshow(self.segRes)
        ppl.show()


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



    def join(self):
        i = 0
        IB = self.segRes == i
        IB = np.asarray(IB,dtype=np.uint8)
        while i <= self.index:

            if np.any(IB):
                nonzer = np.nonzero(IB)[0]
                yF = nonzer[0]
                xF = nonzer[1]
                imDil = cv2.dilate(IB,cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)))
                imDiff = cv2.absdiff(imDil,IB)
                IbMult = imDiff * self.serRes
                IBMultNZ = np.nonzero(IbMult)
                IBUnique = np.unique(IBMultNZ)
                joined = 0
                for k in range(0, IBUnique.size):
                    IBS = self.segRes == IBUnique[k]
                    IBS = np.asarray(IBS,dtype=np.uint8)
                    nonzer = np.nonzero(IBS)[0]
                    yFS = nonzer[0]
                    xFS = nonzer[1]


                    rozniczaKolorow = np.abs(self.MRes[yF, xF] - self.MRes[yFS, xFS])
                    if rozniczaKolorow < self.progKolorow:
                        self.segRes[IBS] = i
                        joined = 1
                    if joined == 0:
                        i = + 1
            else:
                i = i +1


newDeivider  = Divider(img,8,00.5)
newDeivider.start()
