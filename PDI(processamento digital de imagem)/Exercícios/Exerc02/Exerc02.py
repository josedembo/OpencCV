import cv2

img = cv2.imread("estrada.jpg")

nivel_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("estrada_cinza", nivel_cinza)
cv2.waitKey()
cv2.imwrite("estrada_cinza.jpg", nivel_cinza)
