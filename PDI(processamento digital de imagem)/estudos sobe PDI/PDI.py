import cv2


imagem = cv2.imread("imagens\cidade.jpg")
print('largura em pixeis: ', end='')
print(imagem.shape[1])
print('Altura em pixeis: ', end='')
print(imagem.shape[0])
print('quantidade de canais: ', end='')
print(imagem.shape[2])

(b, g, r) = imagem[0, 0]
print("O pixel p(0,0) tem as seguintes cores: ")
print("vermelho = ", r, "verde = ", g, "Azul =", b)

cv2.imshow("Carros", imagem)
cv2.waitKey()

cv2.imwrite("GatosLindos.jpg", imagem)
