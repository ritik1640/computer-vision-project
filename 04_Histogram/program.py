import cv2
import numpy as np

# Image read 
img = cv2.imread("04_Histogram/image.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image load nahi hui, path check karo")
else:
    # Histogram calculate 
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    # Histogram  normalize 
    hist = cv2.normalize(hist, hist, 0, 400, cv2.NORM_MINMAX)

    # Blank white canvas 
    hist_img = np.full((400, 256), 255, dtype=np.uint8)

    for x in range(256):
        cv2.line(hist_img, (x, 400), (x, 400 - int(hist[x])), 0, 1)

    # Save 
    cv2.imwrite("output_gray.jpg", img)
    cv2.imwrite("output_histogram.jpg", hist_img)


    cv2.imshow("Original", img)
    cv2.imshow("Histogram", hist_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()