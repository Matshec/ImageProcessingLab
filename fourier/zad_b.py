import cv2
import matplotlib.pyplot as plt
import numpy as np

def imshow(img, title='', sub1=0, sub2=0, sub3=0):
    if sub1 != 0:
        plt.subplot(sub1, sub2, sub3)
    if title != '':
        plt.title(title)
    plt.imshow(img, cmap='gray')

kwadrat = cv2.imread('5_Fourier/kwadrat.bmp', cv2.IMREAD_GRAYSCALE)
kwadrat45 = cv2.imread('5_Fourier/kwadrat45.bmp', cv2.IMREAD_GRAYSCALE)
kwadratKL = cv2.imread('5_Fourier/kwadratKL.bmp', cv2.IMREAD_GRAYSCALE)
kwadratS = cv2.imread('5_Fourier/kwadratS.bmp', cv2.IMREAD_GRAYSCALE)
kwadratT = cv2.imread('5_Fourier/kwadratT.bmp', cv2.IMREAD_GRAYSCALE)

def compare_furier(img1, img2):
  img1_f = np.fft.fft2(img1)
  img1_shift = np.fft.fftshift(img1_f)
  img1_amp = np.log10(np.abs(img1_shift) + 1)
  img1_phase = np.angle(np.multiply(img1_shift, (img1_amp > 0.0001)))

  img2_f = np.fft.fft2(img2)
  img2_shift = np.fft.fftshift(img2_f)
  img2_amp = np.log10(np.abs(img2_shift) + 1)
  img2_phase = np.angle(np.multiply(img2_shift, (img2_amp > 0.0001)))

  imshow(img1, 'original', 2, 3, 1)
  imshow(img1_amp, 'amp', 2, 3, 2)
  imshow(img1_phase, 'phase', 2, 3, 3)
  imshow(img2, 'original', 2, 3, 4)
  imshow(img2_amp, 'amp', 2, 3, 5)
  imshow(img2_phase, 'phase', 2, 3, 6)
  plt.show()

compare_furier(kwadrat, kwadratT)
compare_furier(kwadrat, kwadrat45)
compare_furier(kwadrat, kwadratS)
compare_furier(kwadrat45, kwadratKL)