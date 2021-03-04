import numpy as np
import cv2 as cv

face_classifier = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv.imread("gestao-pessoas.jpg")


def redimensiona(imagem):
    (altura, largura, canais) = imagem.shape
    if(largura > 390 or altura > 210):
        nova_largura = 390
        nova_altura = 210
        novo_tamanho = (nova_largura, nova_altura)
        imagem_redimensionada = cv.resize(
            imagem, novo_tamanho, interpolation=cv.INTER_AREA)
        nova_imagem = imagem_redimensionada
        return nova_imagem
    else:
        return imagem


img = redimensiona(img)

img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

faces = face_classifier.detectMultiScale(img_gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('imagem', img)
cv.waitKey()
cv.destroyAllWindows()
