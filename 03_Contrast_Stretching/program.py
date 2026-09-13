import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

# Min aur max pixel value 
min_val = np.min(img)
max_val = np.max(img)

# Contrast stretching formula 
stretched = (img - min_val) * (255 / (max_val - min_val))
stretched = np.uint8(stretched)   # values  convert into 0-255

cv2.imwrite("output_stretched.jpg", stretched)

cv2.imshow("Original", img)
cv2.imshow("Contrast Stretched", stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()