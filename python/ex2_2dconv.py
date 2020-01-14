import numpy as np
import scipy.signal as sp
import cv2

def conv2d(img, kernel):
    fr = np.fft.fft2(img)
    fr2 = np.fft.fft2(np.flipud(np.fliplr(kernel)))
    m = fr.shape
    cc = np.real(np.fft.ifft2(fr*fr2))
    cc = np.roll(cc, -m[0]/2+1, axis=0)
    cc = np.roll(cc, -m[1]/2+1, axis=1)
    return cc

im = cv2.imread("apple.png", 0)
print(type(im[:][:][0]))

lpf = np.ones((3, 3))

lpf_image = sp.convolve(im, lpf, 'valid')

cv2.imshow("lpf",lpf_image)
cv2.waitKey(0)
#cv2.destroyAllWindows()
