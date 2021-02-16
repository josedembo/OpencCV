import cv2

imagem = cv2.imread("imagens/gatos.jpg")
imagem2 = cv2.imread("imagens/Maos.jpg")
imagem3 = cv2.imread("imagens/Jesus.jpg")

for y in range(0, imagem.shape[0]):
    for x in range(0, imagem.shape[1]):
        # Alterando a cor das imagens
        imagem[y, x] = (0, 255, 255)

for y in range(0, imagem2.shape[0]):
    for x in range(0, imagem2.shape[1]):
        imagem2[y, x] = (x % 256, y % 256, x % 256)

for y in range(0, imagem3.shape[0], 6):
    for x in range(0, imagem3.shape[1], 6):
        imagem3[y, x] = (0, (x*y)/256, 0)

largura_imagem2 = imagem2.shape[0]
altura_imagem2 = imagem2.shape[1]
print("imagem2_Largura: ", largura_imagem2)
print("imagem2_altura: ", altura_imagem2)

#cv2.imshow("imagem modificada", imagem)
#cv2.imshow("imagem2 modificada", imagem2)
cv2.imshow("imagem3 modificada", imagem3)
cv2.waitKey()
