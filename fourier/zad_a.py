import cv2
import matplotlib.pyplot as plt
import numpy as np

def imshow(img, title='', sub1=0, sub2=0, sub3=0):
    if sub1 != 0:
        plt.subplot(sub1, sub2, sub3)
    if title != '':
        plt.title(title)
    plt.imshow(img, cmap='gray')

dwieFale = cv2.imread('5_Fourier/dwieFale.bmp', cv2.IMREAD_GRAYSCALE)
kolo = cv2.imread('5_Fourier/kolo.bmp', cv2.IMREAD_GRAYSCALE)
kwadrat = cv2.imread('5_Fourier/kwadrat.bmp', cv2.IMREAD_GRAYSCALE)
kwadrat45 = cv2.imread('5_Fourier/kwadrat45.bmp', cv2.IMREAD_GRAYSCALE)
kwadratKL = cv2.imread('5_Fourier/kwadratKL.bmp', cv2.IMREAD_GRAYSCALE)
kwadratS = cv2.imread('5_Fourier/kwadratS.bmp', cv2.IMREAD_GRAYSCALE)
kwadratT = cv2.imread('5_Fourier/kwadratT.bmp', cv2.IMREAD_GRAYSCALE)
trojkat = cv2.imread('5_Fourier/trojkat.bmp', cv2.IMREAD_GRAYSCALE)

def go_go_power_furier(img):
  img_f = np.fft.fft2(img)
  img_shift = np.fft.fftshift(img_f)
  img_amp = np.log10(np.abs(img_shift) + 1)
  img_phase = np.angle(np.multiply(img_shift, (img_amp > 0.0001)))

  imshow(img, 'original', 1, 3, 1)
  imshow(img_amp, 'amp', 1, 3, 2)
  imshow(img_phase, 'phase', 1, 3, 3)
  plt.show()

go_go_power_furier(dwieFale)

# porownanie 2d f z 2x 1d f

f11 = np.fft.fft(dwieFale, axis=0)
f12 = np.fft.fft(f11, axis=1)
fshift = np.fft.fftshift(f12)
famp = np.log10(np.abs(fshift) + 1)

f2 = np.fft.fft2(dwieFale)
sshift = np.fft.fftshift(f2)
samp = np.log10(np.abs(sshift) + 1)

imshow(famp, '', 1, 2, 1)
imshow(samp, '', 1, 2, 2)
plt.show()
