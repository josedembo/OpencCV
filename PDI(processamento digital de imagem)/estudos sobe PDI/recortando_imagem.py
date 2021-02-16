import cv2
img = cv2.imread("imagens/estrada.jpg")

recorte = img[100:200, 100:200]
cv2.imshow("imagem recortada", img)
cv2.waitKey()
cv2.imwrite("estrada_recortada.jpg", recorte)
