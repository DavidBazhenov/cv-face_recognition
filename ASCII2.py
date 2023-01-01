import cv2 as cv
import numpy as np
# выводит изображение и преобразует его в реальном времени в ASCII рисунок в консоли
def draw_picture(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    """    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    output = cv2.resize(src, dsize)"""
    picture = cv.resize(gray, (120, 40))
    chars = " .:-=+*#%@"
    for row in picture:
        for pixel in row:
            index = int(pixel / 256 * len(chars))
            char = chars[index]
            print(char, end="")
        print()
def show_web():
    cap = cv.VideoCapture(0)
    cap.set(3, 500)
    cap.set(4, 300)
    while True:
        success, img = cap.read()
        if not success or (cv.waitKey(1) & 0xFF == ord('q')):
            break
        else:
            draw_picture(img)
            cv.imshow('vid', img)
"""img = cv.imread('images/img4.png')
img = cv.resize(img, (img.shape[1]*2, img.shape[0]*2))#размер
#img = cv.GaussianBlur(img, (9,9), 4)#размытие
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.Canny(img, 90,90)
kernel = np.ones((5, 5), np.uint8)
img = cv.dilate(img, kernel, iterations=1)
img = cv.erode(img, kernel, iterations=1)
cv.imshow('newim', img)
cv.waitKey(0)"""
show_web()