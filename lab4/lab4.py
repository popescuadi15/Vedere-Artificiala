import cv2
import numpy as np
from PIL import Image

img = Image.open('D:/Vedere_artificiala/lab4/led.png')


img.save('D:/Vedere_artificiala/lab4/led_no_metadata.png')


img = Image.open('D:/Vedere_artificiala/lab4/arduino.png')
img.save('D:/Vedere_artificiala/lab4/arduino_no_metadata.png')


source_image = cv2.imread('D:/Vedere_artificiala/lab4/arduino_no_metadata.png')
template_image = cv2.imread('D:/Vedere_artificiala/lab4/led_no_metadata.png', 0)




if len(source_image.shape) == 3:
    source_image_gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)
else:
    source_image_gray = source_image


height, width = source_image.shape[:2]


result = cv2.matchTemplate(source_image_gray, template_image, cv2.TM_CCOEFF_NORMED)


threshold = 0.8
locations = np.where(result >= threshold)


mask = np.zeros((height, width), dtype=np.uint8)

for pt in zip(*locations[::-1]):
    top_left = pt
    bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
    cv2.rectangle(mask, top_left, bottom_right, 255, -1)


edges = cv2.Canny(source_image_gray, 100, 200)


masked_edges = cv2.bitwise_and(edges, edges, mask=mask)


final_image = cv2.bitwise_and(source_image, source_image, mask=mask)
final_image[masked_edges > 0] = [0, 0, 255]


cv2.imwrite('output_image.jpg', final_image)


cv2.imshow('Final Image', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()