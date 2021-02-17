import cv2

img = cv2.imread("estrada.jpg")

img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cane = cv2.Canny(img, 100, 200)

cv2.imshow("imagem_cinza", img_cinza)
cv2.imshow("imagem triansformada", cane)
cv2.waitKey()
cv2.imwrite("imagem_cinza.jpg", img_cinza)
cv2.imwrite("imagem_Filtro_Cane.jpg", cane)
