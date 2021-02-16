import cv2

img = cv2.imread("imagens/estrada.jpg")

fonte = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, "Caurya Deus Lima de Jesus Alcantara",
            (15, 65), fonte, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("imagem_escrita", img)
cv2.waitKey()
