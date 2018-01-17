import cv2
import matplotlib.pyplot as ppl

img = cv2.imread('KrawedzieHough/dom.png', cv2.IMREAD_GRAYSCALE)
gauss = cv2.blur(img, (3, 3))
laplacian = cv2.Laplacian(img, ddepth=-1)
canny = cv2.Canny(img, 100, 200)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


ppl.figure(1)
ppl.subplot(221)
ppl.imshow(laplacian,cmap="gray")
ppl.title("laplacian")

ppl.subplot(222)
ppl.imshow(canny,cmap="gray")
ppl.title("canny")

ppl.subplot(223)
ppl.imshow(sobelx,cmap="gray")
ppl.title("sobelx")


ppl.subplot(224)
ppl.imshow(sobely,cmap="gray")
ppl.title("sobely")


ppl.show()