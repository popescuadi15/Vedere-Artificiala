import cv2
import numpy as np


image_path = 'D:/Vedere_artificiala/lab3/input.png'
image = cv2.imread(image_path)


height, width = image.shape[:2]


central_width = int(width * 0.7)
central_height = int(height * 0.7)


start_x = (width - central_width) // 2
start_y = (height - central_height) // 2

central_region = image[start_y:start_y+central_height, start_x:start_x+central_width]


gray = cv2.cvtColor(central_region, cv2.COLOR_BGR2GRAY)


adaptive_threshold = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)


border_width = int(width * 0.15)
border_height = int(height * 0.15)


border_region = image[start_y-border_height:start_y+central_height+border_height, start_x-border_width:start_x+central_width+border_width]


gray_border = cv2.cvtColor(border_region, cv2.COLOR_BGR2GRAY)


blurred_border = cv2.GaussianBlur(gray_border, (15, 15), 0)


image[start_y:start_y+central_height, start_x:start_x+central_width] = cv2.cvtColor(adaptive_threshold, cv2.COLOR_GRAY2BGR)


image[start_y-border_height:start_y+central_height+border_height, start_x-border_width:start_x+central_width+border_width] = cv2.cvtColor(blurred_border, cv2.COLOR_GRAY2BGR)


cv2.imwrite('output_image.jpg', image)


cv2.imshow('Processed Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
