import cv2
import numpy as np


image = cv2.imread('D:/Vedere_artificiala/lab5/im0.png')


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (5, 5), 0)


edges = cv2.Canny(blurred, 50, 150)


lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)


longest_line = None
max_length = 0
for line in lines:
    x1, y1, x2, y2 = line[0]
    length = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if length > max_length:
        max_length = length
        longest_line = (x1, y1, x2, y2)


x1, y1, x2, y2 = longest_line
cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)


rect_x1 = min(x1, x2) - 10
rect_y1 = min(y1, y2) - 10
rect_x2 = max(x1, x2) + 10
rect_y2 = max(y1, y2) + 10


cv2.rectangle(image, (rect_x1, rect_y1), (rect_x2, rect_y2), (0, 255, 0), 2)


roi = image[rect_y1:rect_y2, rect_x1:rect_x2]


equalized_roi = cv2.equalizeHist(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY))


equalized_roi_bgr = cv2.cvtColor(equalized_roi, cv2.COLOR_GRAY2BGR)
image[rect_y1:rect_y2, rect_x1:rect_x2] = equalized_roi_bgr


cv2.imshow('Image with Longest Line and Equalized ROI', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('output_image0.jpg', image)
