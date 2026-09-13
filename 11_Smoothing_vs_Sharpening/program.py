import cv2
import numpy as np

img = cv2.imread("11_Smoothing_vs_Sharpening/image.jpg")

smoothed = cv2.GaussianBlur(img, (5, 5), 0)

kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
sharpened = cv2.filter2D(img, -1, kernel)

combined = np.hstack((smoothed, sharpened))
cv2.imwrite("output_comparison.jpg", combined)

cv2.imshow("Smoothed | Sharpened", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()