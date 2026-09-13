import cv2

img = cv2.imread("06_Mean_Filter/image.jpg")

mean_filtered = cv2.blur(img, (25, 25))

cv2.imwrite("output_mean_filter.jpg", mean_filtered)

cv2.imshow("Original", img)

cv2.imshow("Mean Filtered", mean_filtered)

cv2.waitKey(0)

cv2.destroyAllWindows()