import cv2
import numpy as np
import matplotlib.pyplot as ppl
import skimage.morphology as smorf

img = cv2.imread("Morfologia/fingerprint.bmp", cv2.IMREAD_GRAYSCALE)

original = img.copy()


# dla listy kerneli toworzy ich wszystkie rotacje o 90 st
def get_rotations(kernels):
    ret = []
    for el in kernels:
        for i in range(1, 5):
            ret.append(np.rot90(el, k=i))
    return ret


# def thinning(img, iterations=1):
#     def subtr(img, img2):
#         img2 = cv2.bitwise_not(img2)
#         return cv2.bitwise_and(img, img2)
#
#     kernel = [np.array([[-1, -1, -1], [-1, 1, -1], [1, 1, 1]], dtype=np.int8),
#               np.array([[-1, -1, -1], [1, 1, -1], [-1, 1, -1]], dtype=np.int8)]
#     rotations = get_rotations(kernel)
#     rot_len = len(rotations)
#     kern_iter = 0
#     for i in range(iterations):
#         output_image = cv2.morphologyEx(img, cv2.MORPH_HITMISS, rotations[kern_iter])
#         x = subtr(img, output_image)
#         img = x
#
#         if kern_iter >= rot_len - 1:
#             kern_iter = 0
#         else:
#             kern_iter = kern_iter + 1
#     return img


def img_reconstruct(img_ref, img_mark,ktype=cv2.MORPH_RECT,ksize=(3,3)):
    kern = cv2.getStructuringElement(ktype, ksize)
    img_rec = img_mark.copy()
    while True:
        img_res = img_rec.copy()
        img_dil = cv2.dilate(img_res, kern)
        img_rec = cv2.min(img_dil, img_ref)
        if np.array_equal(img_rec,img_res):
            break
    return img_res

#net
def skel(img):
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)

    ret, img = cv2.threshold(img, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while not done:
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True
    return skel

def imshow_gray(img):
    ppl.imshow(img,cmap="gray")

if __name__ == "__main__":
    # test_kernel = np.array([[0, 0, 0], [-1, 0, 0], [1, 1, 1]], dtype=np.int8)
    #
    # test_kernel2 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], dtype=np.int8)
    #
    # S3 = np.array([[-1, 1, -1],
    #                [1, 1, 1],
    #                [-1, 1, -1]], dtype=np.int8)
    #
    # res = thinning(img, 50)
    #
    # ppl.subplot(211)
    # ppl.imshow(res, cmap="gray")
    # ppl.subplot(212)
    # ppl.imshow(original, cmap="gray")
    # ppl.show()


    #test recostruct
    # img = cv2.imread("Morfologia/text.bmp", cv2.IMREAD_GRAYSCALE)
    # elem = np.ones((51,1),np.int8)
    # marker = cv2.erode(img,elem)
    # res = img_reconstruct(img,marker)
    # ppl.imshow(res,cmap="gray")
    # ppl.show()


    # test skel
    #
    # img_bone = cv2.imread("Morfologia/kosc.bmp", cv2.IMREAD_GRAYSCALE)
    # img_b = np.asarray(img_bone,dtype=np.bool)
    # ret = smorf.skeletonize(img_b)#skel(img)
    # imshow_gray(ret)
    # ppl.show()


    # thinning
    thin = smorf.thin(img)
    imshow_gray(thin)
    ppl.show()






