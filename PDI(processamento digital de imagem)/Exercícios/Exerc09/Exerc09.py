import cv2

img = cv2.imread("estrada.jpg")
img = cv2.medianBlur(img, 5)

grayscal = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

altura, largura, canais = img.shape

print('Altura: ', altura)
print('largura:', largura)
print('Canais:', canais)

matriz = [], []

matriz.append(2, 5)
