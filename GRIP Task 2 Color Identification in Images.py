# Zenab Habib
# GRIP Task 2

import numpy as np
import cv2 as cv

img = cv.imread("sample.jpg")
img = cv.resize(img, (800, 700))


def click(event, x, y, flag, para):
    if event == cv.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        colors = np.zeros((250, 250, 3), np.uint8)
        colors[:] = [blue, green, red]

        cv.imshow("BGR colors: ", colors)


cv.imshow("Image", img)
cv.setMouseCallback("Image", click)
cv.waitKey(0)
cv.destroyAllWindows()
