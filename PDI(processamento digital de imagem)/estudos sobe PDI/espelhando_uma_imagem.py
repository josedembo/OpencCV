import cv2

img = cv2.imread("imagens/estrada.jpg")
cv2.imshow("imagem_original", img)

espelhamento_horizontal = img[::-1, :]
#espelhamento_horizontal = cv2.flip(img, 1)

espelhamento_vertical = img[:, ::-1]
#espelhamento_vertical = cv2.flip(img, 0)

espelhamento_hv = img[::-1, ::-1]
#espelhamento_hv = cv2.flip(img, -1)

cv2.imshow("espelhamento_Horizontal", espelhamento_horizontal)
cv2.imshow("espelhamento_Vertical", espelhamento_vertical)
cv2.imshow("espelhamento_HV", espelhamento_hv)

cv2.waitKey()
