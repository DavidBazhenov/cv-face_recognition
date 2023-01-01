import cv2 as cv
import numpy as np
#выделяет лицо на фото
img = cv.imread('images/BazhenovDV.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face_cascade = cv.CascadeClassifier("cas/face.xml")
faces = face_cascade.detectMultiScale(img, 1.1, 19)
for x, y, width, height in faces:
    cv.rectangle(img, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
cv.imshow('newim', img)
cv.waitKey(0)