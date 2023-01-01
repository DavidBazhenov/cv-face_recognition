import cv2 as cv
import numpy as np
#просто рисует фигуры
photo = np.zeros((300, 300, 3), dtype='uint8')
#photo[100:140, 100:140] = (153, 204, 255)
#cv.rectangle(photo, (13, 12), (100,100), (153, 204, 255), thickness=cv.FILLED)
cv.line(photo, (0,0), (300, 300), (153, 204, 255), thickness=3)
cv.circle(photo, (photo.shape[1]//2, photo.shape[0]//2), 50,(153, 204, 255), thickness=3 )
cv.putText(photo, 'David', (100, 150), cv.FONT_ITALIC, 2, (255, 0, 0), 2)

cv.imshow("ph", photo)
cv.waitKey(0)