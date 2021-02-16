import cv2

imagem = cv2.imread("imagens/carro.jpg")

print("linhas da imagem: ", imagem.shape[0])
print("colunas da imagem: ", imagem.shape[1])

imagem[300:389, 300:389] = (0, 255, 0)
imagem[50:90, 50:90] = (255, 0, 0)
imagem[178:250, 179:200] = (0, 0, 255)
imagem[0:100, 0:960] = (255, 0, 0)
imagem[0:960, 0:100] = (255, 0, 0)
imagem[70:100, 300:450] = (0, 0, 0)
imagem[:, 200:250] = (0, 0, 0)
imagem[200:250, :] = (0, 0, 0)
imagem[500:550, 580:600] = (255, 255, 255)
cv2.imshow("imagem_alterada", imagem)
cv2.waitKey()
cv2.imwrite("carro_alterado.jpg", imagem)
