import cv2
import numpy as np

img = cv2.imread("09_Filter_Comparison/image.jpg")


img = cv2.resize(img, (400, 400))

mean_filtered = cv2.blur(img, (5, 5))
gaussian_filtered = cv2.GaussianBlur(img, (5, 5), 0)
median_filtered = cv2.medianBlur(img, 5)

cv2.imwrite("output_original.jpg", img)
cv2.imwrite("output_mean.jpg", mean_filtered)
cv2.imwrite("output_gaussian.jpg", gaussian_filtered)
cv2.imwrite("output_median.jpg", median_filtered)

combined = np.hstack((img, mean_filtered, gaussian_filtered, median_filtered))
cv2.imwrite("output_comparison.jpg", combined)

cv2.imshow("Original | Mean | Gaussian | Median", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()