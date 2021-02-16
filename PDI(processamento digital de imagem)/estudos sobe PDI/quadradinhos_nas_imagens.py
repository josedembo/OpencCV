import cv2

imagem = cv2.imread("imagens/estrada.jpg")

for y in range(0, imagem.shape[0], 10):
    for x in range(0, imagem.shape[1], 10):
        imagem[y:y+5, x:x+5] = (255, 0, 0)

cv2.imshow("estrada_com_quadradinhos", imagem)
cv2.waitKey()
