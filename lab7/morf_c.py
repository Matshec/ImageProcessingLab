import cv2
import matplotlib.pyplot as ppl


img = cv2.imread("Morfologia/ferrari.bmp",cv2.IMREAD_GRAYSCALE)

#opening
# ppl.figure("opening")
# elem = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# dilat_im = cv2.dilate(img,elem)
# open_im = cv2.erode(dilat_im,elem)
# erode_im = cv2.erode(img,elem)
# diff_im = dilat_im - erode_im
# ppl.subplot(221)
# ppl.imshow(img,cmap="gray")
# ppl.title("orginal")
# ppl.subplot(222)
# ppl.imshow(open_im,cmap="gray")
# ppl.title("otwarcie")
# ppl.subplot(223)
# ppl.imshow(diff_im,cmap="gray")
# ppl.title("rożnica")
# ppl.show()

#closing

# ppl.figure("opening")
# elem = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# dilat_im = cv2.dilate(img,elem)
# close_im = cv2.morphologyEx(img,cv2.MORPH_CLOSE,elem)
# erode_im = cv2.erode(img,elem)
# diff_im = dilat_im - erode_im
# ppl.subplot(221)
# ppl.imshow(img,cmap="gray")
# ppl.title("orginal")
# ppl.subplot(222)
# ppl.imshow(close_im,cmap="gray")
# ppl.title("otwarcie")
# ppl.subplot(223)
# ppl.imshow(diff_im,cmap="gray")
# ppl.title("rożnica")
# ppl.show()

#top hat
# top hat  =  src - open
# elem = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# top_hat_im = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,elem)
# ppl.figure("top hat")
# ppl.subplot(211)
# ppl.imshow(img,cmap="gray")
# ppl.title("orig")
# ppl.subplot(212)
# ppl.imshow(top_hat_im,cmap="gray")
# ppl.title("top hat")
# ppl.show()

#bottom hat
#closing  - img
# elem = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# clos_img = cv2.morphologyEx(img,cv2.MORPH_CLOSE,elem)
# bt_hat = img - clos_img
# ppl.figure("bt hat")
# ppl.subplot(211)
# ppl.imshow(img,cmap="gray")
# ppl.title("orig")
# ppl.subplot(212)
# ppl.imshow(bt_hat,cmap="gray")
# ppl.title("top hat")
# ppl.show()


rice_img = cv2.imread("Binaryzacja/rice.png",cv2.IMREAD_GRAYSCALE)
big_elem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
top_rice = cv2.morphologyEx(rice_img,cv2.MORPH_TOPHAT,big_elem)
ppl.figure("rice")
ppl.subplot(211)
ppl.imshow(rice_img,cmap="gray")
ppl.title("org")
ppl.subplot(212)
ppl.imshow(top_rice,cmap="gray")
ppl.title("top hat")
ppl.show()
