import cv2
import time
import pyautogui
from PIL import ImageGrab
import difflib
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")
i = 0
time.sleep(1.5)
while 1:
    start_time = time.time()
    time.sleep(0.25)
    base_screen = ImageGrab.grab(bbox=(1080, 1228, 1634, 1415))
    base_screen.save('C:/Users/DIMA/Desktop/IMAGE_GRAB/IMG_GRAB.png')  # Сохранение картинки

    block_2 = ImageGrab.grab(bbox=(1638, 1228, 2190, 1415))
    block_2.save('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_2.png')

    block_3 = ImageGrab.grab(bbox=(2195, 1228, 2745, 1415))
    block_3.save('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_3.png')

    block_4 = ImageGrab.grab(bbox=(2750, 1228, 3303, 1415))
    block_4.save('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_4.png')

    block_5 = ImageGrab.grab(bbox=(3303, 1228, 3840, 1415))
    block_5.save('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_5.png')


    # Функция вычисления хэша
    def CalcImageHash(FileName):
        image = cv2.imread(FileName)  # Прочитаем картинку
        resized = cv2.resize(image, (8, 8), interpolation=cv2.INTER_AREA)  # Уменьшим картинку
        gray_image = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)  # Переведем в черно-белый формат
        avg = gray_image.mean()  # Среднее значение пикселя
        ret, threshold_image = cv2.threshold(gray_image, avg, 255, 0)  # Бинаризация по порогу

        # Рассчитаем хэш
        _hash = ""
        for x in range(8):
            for y in range(8):
                val = threshold_image[x, y]
                if val == 255:
                    _hash = _hash + "1"
                else:
                    _hash = _hash + "0"

        return _hash


    def CompareHash(hash1, hash2):
        l = len(hash1)
        i = 0
        count = 0
        while i < l:
            if hash1[i] != hash2[i]:
                count = count + 1
            i = i + 1
        return count

    hash_red = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/template.png')
    hash_black = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/template_black.png')

    hash1 = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/IMG_GRAB.png')
    hash2 = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_2.png')
    hash3 = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_3.png')
    hash4 = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_4.png')
    hash5 = CalcImageHash('C:/Users/DIMA/Desktop/IMAGE_GRAB/GRAB_BLOCK_5.png')

    print("Красное: ", CompareHash(hash_red, hash1))  # Полученный хэш при сравнении 2-ух изображений
    print("Серое: ", CompareHash(hash_black, hash1))

    def PressButton(hash_image):
        first = CompareHash(hash_red, hash_image)
        second = CompareHash(hash_black, hash_image)
        if first == 23 and second == 26:
            print("PRESS RIGHT(LAST)")
            shell.SendKeys("{RIGHT}")
        if first == 22 and second == 29:
            print("PRESS LEFT(LAST")
            shell.SendKeys("{LEFT}")
        if first == 29 and second == 22:  # КОД ЗОЛОТОЙ ПОДКОВЫ (КРАСНОЕ)
            print("PRESS LEFT???")
            shell.SendKeys("{LEFT}")
        else:
            if first < second:
                if first < 5:
                    print("PRESS LEFT")
                    shell.SendKeys("{LEFT}")
            else:
                if second < 10:
                    print("PRESS RIGHT")
                    shell.SendKeys("{RIGHT}")

    PressButton(hash1)
    time.sleep(0.1)
    PressButton(hash2)
    time.sleep(0.1)
    PressButton(hash3)
    time.sleep(0.1)
    PressButton(hash4)
    time.sleep(0.1)
    PressButton(hash5)
    time.sleep(0.1)
    # print("Итерация: ", i, "--- %s seconds ---" % (time.time() - start_time))
    i += 1
    time.sleep(0.2)
