import numpy as np
import cv2
import matplotlib.pyplot as ppl


img = cv2.imread("Morfologia/hom.bmp",cv2.IMREAD_GRAYSCALE)
ertka= cv2.imread("Morfologia/ertka.bmp",cv2.IMREAD_GRAYSCALE)
buzka = cv2.imread("Morfologia/buzka.bmp",cv2.IMREAD_GRAYSCALE)

ar = np.array([[0,1,0],
               [1,1,1],
               [0,1,0]])

square = np.array([[1,1,1],
                   [1,0,1],
                   [1,1,1]])


hair = np.array([[0,0,1],
                [0,1,0],
                [1,0,0]])

S1 = np.array([[0,1,0],
                [1,1,1],
                [0,1,0]])

S2 = np.array([[1,0,1],
                [0,0,0],
                [1,0,1]])

#łączona maska - kopiujemu S1 i tam gdzie są 1 w S2 wstawiamy -1 w S3
S3 = np.array([[-1,1,-1],
                [1,1,1],
                [-1,1,-1]],dtype=np.int8)





kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(ertka,kernel,iterations=1)
ppl.figure("erosion")
ppl.subplot(211)
ppl.imshow(ertka,cmap="gray")
ppl.subplot(212)
ppl.imshow(erosion,cmap="gray")
ppl.show()

dilation = cv2.dilate(erosion,kernel,iterations=1)

ppl.figure("dilatation")
ppl.subplot(211)
ppl.imshow(ertka, cmap="gray")
ppl.subplot(212)
ppl.imshow(dilation,cmap="gray")
ppl.show()


output_image = cv2.morphologyEx(img, cv2.MORPH_HITMISS, S3)
# 1 erozja i 3 razy dylatacja
ppl.figure("hitmiss")
ppl.subplot(211)
ppl.imshow(img,cmap="gray")
ppl.subplot(212)
ppl.imshow(output_image,cmap="gray")
ppl.show()



ppl.figure("ertka2")
out1 = cv2.erode(ertka,kernel,iterations=1)
out2 = cv2.dilate(out1,kernel,iterations=3)
ppl.subplot(211)
ppl.imshow(ertka,cmap="gray")
ppl.subplot(212)
ppl.imshow(out2,cmap="gray")
ppl.show()

ppl.figure(2)
buzka_out = cv2.erode(buzka,hair)
ppl.subplot(221)
ppl.imshow(buzka,cmap="gray")
ppl.subplot(212)
ppl.imshow(buzka_out,cmap="gray")
ppl.show()





