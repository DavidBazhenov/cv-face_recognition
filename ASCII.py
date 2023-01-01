import cv2

# преобразует видео с камеры в ASCII рисунок и сохраняет покадрово в файл
"""cv2.imshow('newim', gray)
cv2.waitKey(0)"""
ascii_chars1 = '@B8#%*ocu-,.'
ascii_chars2 = '.,-uco*%#8B@'
with open("ascii_image.txt", "w") as f:
    cap = cv2.VideoCapture(0)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):#для завершения программы
            break
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (gray.shape[1], gray.shape[0] // 3))  # размер
        try:
            ascii_image = [[ascii_chars1[int(pixel / 255 * len(ascii_chars1))] for pixel in row] for row in gray]
        except:
            pass
        for row in ascii_image:
            f.write("".join(row) + "\n")

cap.release()