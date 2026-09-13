import cv2


img = cv2.imread("image.jpg")


gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("output_gray.jpg", gray_img)


cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()