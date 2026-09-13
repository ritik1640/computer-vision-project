import cv2
import numpy as np

img = cv2.imread("10_Sharpening/image.jpg")

# Sharpening kernel
kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)


cv2.imwrite("output_sharpened.jpg", sharpened)


cv2.imshow("Sharpened", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()