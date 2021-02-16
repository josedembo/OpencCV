import numpy as np
import cv2

img = cv2.imread("imagens/estrada.jpg")
vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)
cv2.line(img, (0, 0), (100, 200), verde)
cv2.line(img, (300, 200), (150, 150), vermelho, 5)
cv2.rectangle(img, (20, 20), (120, 120), azul, 10)
cv2.rectangle(img, (200, 50), (225, 125), verde, -1)

(x, y) = (img.shape[0]//2, img.shape[0]//2)

for raio in range(0, 175, 15):
    cv2.circle(img, (x, y), raio, vermelho)

cv2.imshow("imagem alterada", img)
cv2.waitKey()
