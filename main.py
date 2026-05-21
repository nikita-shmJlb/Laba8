import cv2

Img = cv2.imread("variant-7.jpg")

step1 = cv2.flip(Img, 1)
final = cv2.flip(step1, 0)

cv2.imshow("Итоговый результат (горизонталь + вертикаль)", final)
cv2.imwrite("variant-7_final.jpg", final)

cv2.waitKey(0)
cv2.destroyAllWindows()