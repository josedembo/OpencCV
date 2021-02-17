import cv2

img = cv2.imread("estrada.jpg")

HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

(canal_azul, canal_verde, canal_vermelho) = cv2.split(HSV)
cv2.imshow("estrada_HSV", HSV)
cv2.imshow("canal_Azul", canal_azul)
cv2.imshow("canal_verde", canal_verde)
cv2.imshow("canal_vermelho", canal_vermelho)
cv2.waitKey()

cv2.imwrite("canal_Azul.jpg", canal_azul)
cv2.imwrite("canal_verde.jpg", canal_verde)
cv2.imwrite("canal_vermelho.jpg", canal_vermelho)
