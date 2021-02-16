import cv2
img = cv2.imread("estrada.jpg")
cv2.imshow("imagem_original", img)
cv2.waitKey()
cv2.imwrite("nova_imagem_estrada.jpg", img)
