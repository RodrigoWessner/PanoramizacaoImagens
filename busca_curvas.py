import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import math

class Busca_Curvas:
    def __init__(self):
        pass

    def compara_curvas(self):
        img = cv2.imread("pano1.png")
        img2 = cv2.imread("pano2.png")
        img3 = cv2.imread("pano3.png")
        curvas1 = self.area_teste(img)
        curvas2 = self.area_teste(img2)
        curvas3 = self.area_teste(img3)
        i = 1
        cv2.destroyAllWindows()
        for a in curvas1:
            print("a shape[1]: ", a.shape[1], "a shape[0]: ", a.shape[0])
            cv2.imshow("AA", a)
            for l in curvas2:
                print("l shape[1]: ", l.shape[1], "l shape[0]: ", l.shape[0])
                cv2.imshow("BB", l)
                cv2.waitKey(0)

        #     cv2.waitKey(0)
        # for b in curvas2:
        #     cv2.imshow("a", b)
        # for b in curvas3:
        #     cv2.imshow("a", b)
        cv2.imshow("AAAAaaaaaa", curvas1[0])

        cv2.waitKey(0)
    def compare(self, img1, img2):
        print("entrou")
        k = cv2.subtract(img1, img2)
        b, g, r = cv2.split(k)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
        return
    def area_teste(self, img):
        print(img.shape)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        binary = cv2.bitwise_not(gray)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        lim = 20
        temp = []
        for contour in (contours):
            (x, y, w, h) = cv2.boundingRect(contour)
            if w > lim and h > lim and w != img.shape[1] and w < 70 and h < 70:
                if (w - h) < 10 or (-10 < (w - h) < 0):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    var = img[y:y+h, x:x+w]
                    temp.append(var)
                print("x+w: ", (x + w), "y+h: ", (y+h), "x: ", x, "y: ", y, "w: ", w, "h: ", h)
            cv2.imshow("teste", img)
        cv2.waitKey(0)
        for v in temp:
            cv2.imshow("v", v)

        return temp



Busca_Curvas().compara_curvas()