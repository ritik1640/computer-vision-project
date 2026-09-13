import cv2
import numpy as np

img = cv2.imread("15_Frequency_HPF/image.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2   # center point


dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)


mask = np.ones((rows, cols, 2), np.uint8)
radius = 30   
cv2.circle(mask, (ccol, crow), radius, (0, 0), -1)


fshift = dft_shift * mask


f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])


img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
img_back = np.uint8(img_back)

cv2.imwrite("output_hpf.jpg", img_back)

cv2.imshow("High Pass Filtered", img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()