import cv2
import matplotlib.pyplot as ppl
import numpy as np

image = cv2.imread("Binaryzacja/rice.png", cv2.IMREAD_GRAYSCALE)


def basic_adaptive_thresh(im, window_size):

    im_height, im_width = im.shape
    image_cpy = im.copy()

    w_size = window_size // 2   # polowa rozmiaru okna

# efektywna iteracja - mozliwy brak koleności
    imIt = np.nditer(im, flags=["multi_index"])
    while not imIt.finished:
        #pobranie indeksow z iteratora
        cur_y, cur_x = imIt.multi_index
        x_beg = cur_x - w_size
        x_end = cur_x + w_size
        y_beg = cur_y - w_size
        y_end = cur_y + w_size
        if x_beg <= 0:
            x_beg = 0
        if y_beg <= 0:
            y_beg = 0
        if x_end >= im_width - 1:
            x_end = im_width - 1
        if y_end >= im_height - 1:
            y_end = im_height - 1

        rect = im[y_beg:y_end, x_beg:x_end]
        thresh = rect.mean()

        # przypisanie wart, imIt[0] - pobranie wart. z iteratora
        if imIt[0] > thresh:
            image_cpy[cur_y, cur_x] = 1
        else:
            image_cpy[cur_y, cur_x] = 0
        imIt.iternext()
    return  image_cpy




def suav_adaptive_thres(im, window_size,k=-0.15,R=128):
    im_height, im_width = im.shape
    image_cpy = im.copy()

    w_size = window_size // 2  # polowa rozmiaru okna

    # efektywna iteracja - mozliwy brak koleności
    imIt = np.nditer(im, flags=["multi_index"])
    while not imIt.finished:
        cur_y, cur_x = imIt.multi_index
        x_beg = cur_x - w_size
        x_end = cur_x + w_size
        y_beg = cur_y - w_size
        y_end = cur_y + w_size
        if x_beg <= 0:
            x_beg = 0
        if y_beg <= 0:
            y_beg = 0
        if x_end >= im_width - 1:
            x_end = im_width - 1
        if y_end >= im_height - 1:
            y_end = im_height - 1

        rect = im[y_beg:y_end, x_beg:x_end]
        mean = rect.mean()
        std_dev = rect.std()
        thresh = mean * (1 + k * ( (std_dev / R) - 1))

        # przypisanie wart
        if imIt[0] > thresh:
            image_cpy[cur_y, cur_x] = 1
        else:
            image_cpy[cur_y, cur_x] = 0
        imIt.iternext()
    return image_cpy


ppl.imshow(image, cmap="gray")
ppl.title("bez bin")
ppl.figure(2)
std_bin_im = basic_adaptive_thresh(image,16)
ppl.imshow(std_bin_im, cmap="gray")
ppl.title("standardowa")
ppl.figure(3)
sav_im = suav_adaptive_thres(image,16)
ppl.imshow(sav_im,cmap="gray")
ppl.title("savioli")
ppl.show()
