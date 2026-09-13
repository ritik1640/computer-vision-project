import cv2

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image load nahi hui, path check karo")
else:
    # Histogram equalization apply 
    equalized = cv2.equalizeHist(img)

    # Save 
    cv2.imwrite("output_original.jpg", img)
    cv2.imwrite("output_equalized.jpg", equalized)

    print("Dono files save ho gayi: output_original.jpg aur output_equalized.jpg")

    cv2.imshow("Original", img)
    cv2.imshow("Equalized", equalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()