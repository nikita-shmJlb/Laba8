import cv2
import math


Img = cv2.imread("variant-7.jpg")

if Img is None:
    print("Ошибка загрузки изображения")
    exit()

h, w = Img.shape[:2]
center_x, center_y = w // 2, h // 2

#Выбор точки отсчета
point_x, point_y = 0, 150

#Измерение расстояния от центра до точки
distance = math.sqrt((point_x - center_x)**2 + (point_y - center_y)**2)

#Центр (зеленый)
cv2.circle(Img, (center_x, center_y), 5, (0, 255, 0), -1)
cv2.circle(Img, (center_x, center_y), 10, (0, 255, 0), 2)

#Точка (красный)
cv2.circle(Img, (point_x, point_y), 5, (0, 0, 255), -1)

#Линия от точки до центра
cv2.line(Img, (point_x, point_y), (center_x, center_y), (255, 0, 0), 2)

#Выводим текст с расстоянием
text = f"Distance: {distance:.2f} pixels"
cv2.putText(Img, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

cv2.imshow("Distance to Center", Img)
cv2.imwrite("result_with_distance.jpg", Img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Расстояние от точки ({point_x}, {point_y}) до центра ({center_x}, {center_y}) = {distance:.2f} пикселей")