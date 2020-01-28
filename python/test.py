import cv2
import scipy.ndimage as sp
import numpy as np

im = cv2.imread("../gran.jpg", 0)
lpf = np.ones((3, 3))/11
lpf[1][1] = -1
#lpf *= -1
imf = sp.convolve(im, lpf)
imf = 255-imf
cv2.imshow('win', imf)
cv2.imshow('nor', im)
cv2.waitKey()
cv2.destroyAllWindows()
