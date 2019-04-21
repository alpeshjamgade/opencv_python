import cv2
import matplotlib
import numpy as np

img1 = cv2.imread('images/dexter.jpg', cv2.IMREAD_ANYCOLOR)
img2 = cv2.imread('images/dexter.jpg',cv2.IMREAD_ANYDEPTH)
img3 = cv2.imread('images/dexter.jpg',cv2.IMREAD_COLOR)
img4 = cv2.imread('images/dexter.jpg',cv2.IMREAD_GRAYSCALE)
img5 = cv2.imread('images/dexter.jpg',cv2.IMREAD_IGNORE_ORIENTATION)
img6 = cv2.imread('images/dexter.jpg',cv2.IMREAD_LOAD_GDAL)
img7 = cv2.imread('images/dexter.jpg',cv2.IMREAD_REDUCED_COLOR_2)
img8 = cv2.imread('images/dexter.jpg',cv2.IMREAD_REDUCED_COLOR_4)
img9 = cv2.imread('images/dexter.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_2)
img10 = cv2.imread('images/dexter.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_4)
img11 = cv2.imread('images/dexter.jpg',cv2.IMREAD_REDUCED_GRAYSCALE_8)
img12 = cv2.imread('images/dexter.jpg',cv2.IMREAD_UNCHANGED)
##
##
##
##cv2.namedWindow('anycolor',cv2.WINDOW_NORMAL)
##cv2.namedWindow('anYDEPTH',cv2.WINDOW_NORMAL)
##cv2.namedWindow('COLOR',cv2.WINDOW_NORMAL)
##cv2.namedWindow('GRAYSCALE',cv2.WINDOW_NORMAL)
##cv2.namedWindow('ORIENTATION',cv2.WINDOW_NORMAL)
##cv2.namedWindow('LOAD_GDAL',cv2.WINDOW_NORMAL)
##cv2.namedWindow('REDUCED_COLOR2',cv2.WINDOW_NORMAL)
##cv2.namedWindow('REDUCED_COLOR4',cv2.WINDOW_NORMAL)
##cv2.namedWindow('REDUCED_GRAYSCALE2',cv2.WINDOW_NORMAL)
##cv2.namedWindow('REDUCED_GRAYSCALE4',cv2.WINDOW_NORMAL)
##cv2.namedWindow('REDUCED_GRAYSCALE8',cv2.WINDOW_NORMAL)
##cv2.namedWindow('UNCHANGED',cv2.WINDOW_NORMAL)
##
##
##
##
cv2.imshow('anycolor', img1)
cv2.imshow('anYDEPTH', img2)
cv2.imshow('COLOR', img3)
cv2.imshow('GRAYSCALE', img4)
cv2.imshow('ORIENTATION', img5)
cv2.imshow('LOAD_GDAL', img6)
cv2.imshow('REDUCED_COLOR2', img7)
cv2.imshow('REDUCED_COLOR4', img8)
cv2.imshow('REDUCED_GRAYSCALE2', img9)
cv2.imshow('REDUCED_GRAYSCALE4', img10)
cv2.imshow('REDUCED_GRAYSCALE8', img11)
cv2.imshow('UNCHANGED', img12)

img  =  cv2.imread('highlight-girl-hawaii.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('myimage', img)
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('fav.jpg', img)
    cv2.destroyAllWindows()

else:
    cv2.destroyAllWindows()

    



