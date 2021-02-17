import cv2

img = cv2.imread("estrada.jpg")

img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mediana = cv2.medianBlur(img, 5)
media = cv2.blur(img, (5, 5))

cv2.imshow("imagem_mediana", mediana)
cv2.imshow("imagem_media", media)
cv2.waitKey()
