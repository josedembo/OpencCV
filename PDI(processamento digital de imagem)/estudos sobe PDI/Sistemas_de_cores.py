import cv2

img = cv2.imread("imagens/estrada.jpg")

GRAY = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

cv2.imshow("imagem_original", img)
cv2.imshow("Gray", GRAY)
cv2.imshow("HSV", HSV)
cv2.imshow("LAb", lab)
cv2.waitKey()
