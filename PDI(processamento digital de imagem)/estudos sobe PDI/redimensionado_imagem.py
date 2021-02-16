import cv2
import numpy as np

img = cv2.imread("imagens/estrada.jpg")
cv2.imshow("imagem_original", img)

largura = img.shape[1]
altura = img.shape[0]
proporcao = float(altura/largura)
largura_nova = 230
altura_nova = int(largura_nova * proporcao)

tamanho_novo = (largura_nova, altura_nova)

img_redimensionada = cv2.resize(
    img, tamanho_novo, interpolation=cv2.INTER_AREA)


img_redimensionada2 = img[::2, ::2]
cv2.imshow("imagem_redimensionada", img_redimensionada)
cv2.waitKey()
cv2.imwrite("jose_novo.jpg", img_redimensionada)
