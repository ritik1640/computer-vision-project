import cv2

img = cv2.imread("07_Gaussian_Filter/image.jpg")

gaussian_filtered = cv2.GaussianBlur(img, (5, 5), 6)


cv2.imwrite("output_gaussian_filter.jpg", gaussian_filtered)


cv2.imshow("Gaussian Filtered", gaussian_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()