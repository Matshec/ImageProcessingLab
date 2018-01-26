import cv2
import matplotlib.pyplot as plt
import numpy as np
import skimage.color.colorlabel as color


def imshow(img, title='', sub1=0, sub2=0, sub3=0):
  if sub1 != 0:
    plt.subplot(sub1, sub2, sub3)
  if title != '':
    plt.title(title)
  plt.imshow(img, cmap='gray')


MIN_DIV = 8
MAX_DIFF = 0.05
COLOR_STEP = 5 / 255


class Bottomup:
  def __init__(self, img):
    self.img = img
    # H, S, V = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.double))
    # self.hue = np.asarray(H, np.double)
    self.img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    self.img = np.asarray(img, dtype=np.double)
    H, S, V = cv2.split(self.img)
    self.hue = H
    self.index = 1
    self.seg_res = np.zeros(H.shape, dtype=np.int16)
    self.m_res = np.zeros(H.shape, dtype=np.int16)

  def start(self):
    (Y, X) = self.hue.shape
    self.split((0, 0), (Y - 1, X - 1))

    self.join()

    # unique = np.unique(self.seg_res)
    # for i in range(0, unique.size - 1):
    #   mask = self.seg_res == unique[i]
    #   print i
    #   print np.sum(mask)
    #   if np.sum(mask) < 100:
    #     self.seg_res[mask] = 0

    plt.imshow(self.seg_res,cmap='gray')
    plt.show()

  def split(self, a, b):
    x1, y1 = a
    x2, y2 = b
    my_slice = self.hue[y1:y2, x1:x2]

    mean = np.mean(my_slice)
    std = np.std(my_slice)
    size = np.abs(x2 - x1)

    if std > MAX_DIFF and size >= MIN_DIV * 2:
      mid_x = int((x1 + x2) / 2)
      mid_y = int((y1 + y2) / 2)
      self.split((x1, y1), (mid_x, mid_y))
      self.split((mid_x, y1), (x2, mid_y))
      self.split((x1, mid_y), (mid_x, y2))
      self.split((mid_x, mid_y), (x2, y2))

    else:
      self.seg_res[y1:y2, x1:x2] = self.index
      self.index = self.index + 1
      self.m_res[y1:y2, x1:x2] = mean

  def join(self):
    i = 1

    while i <= self.index:
      ib = self.seg_res == i
      ib = ib.astype(np.uint8)

      if not np.any(ib):
        i = i + 1
        continue

      (y, x) = np.nonzero(ib)
      first = (y[0], x[0])
      dil = cv2.dilate(ib, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
      dif = cv2.absdiff(dil, ib)

      mult = dif * self.seg_res
      mult_nz = filter(lambda x: x != 0, mult.flatten())
      mult_uniq = np.unique(mult_nz)

      joined = False

      for s in range(0, mult_uniq.size):
        ibs = self.seg_res == mult_uniq[s]
        fg = np.asarray(ibs, np.uint8)
        print(fg)
        # print(fg)
        s = np.nonzero(fg)
        print(s)
        ys, xs = np.nonzero(fg)
        first_s = ys[0], xs[0]

        diff_c = np.abs(self.m_res[first] - self.m_res[first_s])

        if diff_c < COLOR_STEP:
          self.seg_res[ibs] = i
          joined = True

      if not joined:
        i = i + 1


img = cv2.imread('/home/matshec/PycharmProjects/ImageProcessing/segmentation/umbrealla.png',cv2.IMREAD_COLOR)
bottomup = Bottomup(img)
bottomup.start()
