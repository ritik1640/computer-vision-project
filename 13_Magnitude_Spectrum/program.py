import cv2
import numpy as np

img = cv2.imread("13_Magnitude_Spectrum/image.jpg", cv2.IMREAD_GRAYSCALE)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])

magnitude_spectrum = 20 * np.log(magnitude + 1)

magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
magnitude_spectrum = np.uint8(magnitude_spectrum)


cv2.imwrite("output_magnitude_spectrum.jpg", magnitude_spectrum)
cv2.imshow("Magnitude Spectrum", magnitude_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()