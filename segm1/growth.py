import cv2
import numpy as np
import matplotlib.pyplot as ppl

img = cv2.imread("segmentation/knee.png", cv2.IMREAD_GRAYSCALE)
Y = 345
X = 152
img = np.asarray(img, dtype=np.double)
im_size = img.shape
visited = np.zeros(im_size)
segm = np.zeros(im_size)
stack = []  # append,  pop

stack.append((X, Y))

segmented_count = 1
avg_brightness = img[X, Y]

visited[X, Y] = 1
segm[X, Y] = img[X, Y]

STEP = 40

while len(stack) > 0:
    main_x, main_y = stack.pop()
    for i in range(-1, 2):
        for j in range(-1, 2):
            currentX, currentY = main_x + i, main_y + j
            avg_brightness = (avg_brightness * (segmented_count - 1) + img[main_x, main_y]) / segmented_count
            if visited[currentX, currentY] != 1 and np.abs(img[currentX, currentY] - avg_brightness) < STEP:
                segm[currentX, currentY] = img[currentX, currentY]
                segmented_count += 1
                stack.append((currentX, currentY))
            visited[currentX, currentY] = 1


gauss_kern = cv2.getGaussianKernel(5, 0.8)
ppl.imshow(cv2.filter2D(segm, -1, gauss_kern), cmap='gray')
ppl.show()
