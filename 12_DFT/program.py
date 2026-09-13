import cv2
import numpy as np

img = cv2.imread("12_DFT/image.jpg", cv2.IMREAD_GRAYSCALE)

# DFT apply 
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft)

# Magnitude spectrum 
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]) + 1)

# 0-255 range 
magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
magnitude_spectrum = np.uint8(magnitude_spectrum)

# Save 
cv2.imwrite("output_dft.jpg", magnitude_spectrum)

# Display 
cv2.imshow("DFT Magnitude Spectrum", magnitude_spectrum)
cv2.waitKey(0)
cv2.destroyAllWindows()