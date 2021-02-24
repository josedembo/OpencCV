import cv2

img = cv2.imread("estrada.jpg")
img = cv2.medianBlur(img, 5)

grayscal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

largura = img.shape[1]
altura = img.shape[0]

largura_min = int(largura/2)
altura_min = int(altura/2)

largura_max = largura * 2
altura_max = altura * 2

dimensao_min = (largura_min, altura_min)
dimensao_max = (largura_max, altura_max)

img_menor = cv2.resize(img, dimensao_min, interpolation=cv2.INTER_AREA)
img_maior = cv2.resize(img, dimensao_max, interpolation=cv2.INTER_AREA)

cv2.imshow("imagem original ", img)
cv2.imshow("imagem reduzida", img_menor)
cv2.imshow("imagem ampliada", img_maior)
cv2.waitKey()

cv2.imwrite("imagem_reduzida.jpg", img_menor)
cv2.imwrite("imagem_ampliada.jpg", img_maior)
