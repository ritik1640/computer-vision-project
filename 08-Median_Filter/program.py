import cv2

img = cv2.imread("08-Median_Filter/image.jpg")

median_filtered = cv2.medianBlur(img, 5)


cv2.imwrite("output_median_filter.jpg", median_filtered)


cv2.imshow("Median Filtered", median_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()