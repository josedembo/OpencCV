import cv2

img = cv2.imread("estrada.jpg")
img = cv2.medianBlur(img, 5)

grayscal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#grayscal = grayscal[::3, ::3]

mat, thesh = cv2.threshold(grayscal, 127, 255, cv2.THRESH_BINARY)

thres1 = cv2.adaptiveThreshold(
    grayscal, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

thresh2 = cv2.adaptiveThreshold(
    grayscal, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('GrayScal of imagem', grayscal)
cv2.imshow("imagem com threshold", thesh)
cv2.imshow("thresholding Gaussian", thres1)
cv2.imshow("thresholding Mean", thresh2)
cv2.waitKey()

cv2.imwrite("imagem com threshold.jpg", thesh)
cv2.imwrite("Adptivethresh_gaussian.jpg", thres1)
cv2.imwrite("adaptiveThresh_mean.jpg", thresh2)
