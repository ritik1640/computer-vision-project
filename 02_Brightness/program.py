import cv2

img = cv2.imread("image.jpg")

brightness = 40
bright_img = cv2.convertScaleAbs(img, alpha=1, beta=brightness)

cv2.imwrite("output_bright.jpg", bright_img)

cv2.imshow("Bright Image", bright_img)
cv2.waitKey(0)
cv2.destroyAllWindows()