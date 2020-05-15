import cv2 as cv
import numpy as np

sdk = cv.imread("sudoku.png",0)
_, th1 = cv.threshold(sdk, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(sdk, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);
th3 =cv.adaptiveThreshold(sdk,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("sam", sdk)
cv.imshow("thres",th1)
cv.imshow("adap_mean", th2)
cv.imshow("gauss",th3)

k=cv.waitKey(0)
if k==ord('s'):
    cv.imwrite("binary_adapt.jpg",th1)
    cv.imwrite("mean_c.jpg",th2)
    cv.imwrite("gauss.jpg",th3)
cv.destroyAllWindows()
