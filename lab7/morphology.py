import numpy as np
import  cv2
import matplotlib.pyplot  as ppl


img = cv2.imread("Morfologia/hom.bmp",cv2.IMREAD_GRAYSCALE)

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

S3 = np.array([[-1,1,-1],
                [1,1,1],
                [-1,1,-1]],dtype=np.int8)


kernel = np.ones((3,3),np.uint8)

erosion = cv2.erode(img,kernel,iterations=1)


dilation = cv2.dilate(erosion,kernel,iterations=3)



output_image = cv2.morphologyEx(img, cv2.MORPH_HITMISS, S3)
#11 erozja i 3 razy dylatacja
ppl.subplot(211)
ppl.imshow(img,cmap="gray")
ppl.subplot(212)
ppl.imshow(output_image,cmap="gray")
ppl.show()
