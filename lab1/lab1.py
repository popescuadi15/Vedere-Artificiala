import cv2

image = cv2.imread('D:\Vedere_artificiala\lab1\clouds.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Clouds', image)
cv2.imshow('Gray clouds', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()