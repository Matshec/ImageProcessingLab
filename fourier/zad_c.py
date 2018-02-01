import cv2
import matplotlib.pyplot as plt
import numpy as np

def imshow(img, title='', sub1=0, sub2=0, sub3=0):
    if sub1 != 0:
        plt.subplot(sub1, sub2, sub3)
    if title != '':
        plt.title(title)
    plt.imshow(img, cmap='gray')

kolo = cv2.imread('5_Fourier/kolo.bmp', cv2.IMREAD_GRAYSCALE)

kolo_f = np.fft.fft2(kolo)
kolo_shift = np.fft.fftshift(kolo_f)
kolo_rshift = np.fft.ifftshift(kolo_shift)
kolo_rf = np.fft.ifft2(kolo_rshift)

imshow(kolo, 'original', 1, 2, 1)
imshow(kolo_rf.astype(np.float), 'after ifft', 1, 2, 2)
plt.show()