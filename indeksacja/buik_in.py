import cv2
import matplotlib.pyplot as ppl

img = cv2.imread("ccl/shapes.png",cv2.IMREAD_GRAYSCALE)


# input image is thresholded
ret,labels = cv2.connectedComponents(img)

ppl.imshow(labels,cmap="gray")
ppl.show()