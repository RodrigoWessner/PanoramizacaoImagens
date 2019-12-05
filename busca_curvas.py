import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import math
from QrCode import generate_qrCode

class Busca_Curvas:

    def __init__(self):
        generate_qrCode()
        img = cv2.imread("panoA.png")
        img2 = cv2.imread("panoB.png")
        img3 = cv2.imread("panoC.png")
        curvas1 = self.area_teste(img)
        curvas2 = self.area_teste(img2)
        curvas3 = self.area_teste(img3)
        if curvas1[0].shape[1] < 49:
            img = cv2.rotate(img, 90)
            curvas1 = self.area_teste(img)
        if curvas2[0].shape[1] < 49:
            img2 = cv2.rotate(img2, 90)
            curvas2 = self.area_teste(img2)
        if curvas3[0].shape[1] < 49:
            img3 = cv2.rotate(img3, 90)
            curvas3 = self.area_teste(img3)
        contador1 = 0

        while contador1 != 1:
            if self.compara_curvas(curvas1, curvas2) == 0:
                if self.compara_curvas(curvas1, curvas3) == 0:
                    img = cv2.rotate(img, 180)
                else:
                    img_res = np.concatenate((img, img3), axis=1)
                    contador1 = 1
            else:
                img_res = np.concatenate((img, img2), axis=1)
                contador1 = 1
        cv2.imshow("resultado", img_res)
        cv2.waitKey(0)
        contador2 = 0
        while contador2 != 1:
            if self.compara_curvas(curvas2, curvas3) == 0:
               img3 = cv2.rotate(img3, 180)
            else:
                img_res = np.concatenate((img_res, img3), axis=1)
                contador2 = 1

        cv2.imshow("resultado", img_res)
        cv2.waitKey(0)

    def compara_curvas(self, curvas1, curvas2):
        for a in curvas2:
            a = cv2.resize(a, (51, 37))
            cv2.imshow("AA", a)
            for l in curvas1:
                l = cv2.resize(l, (51, 37))
                cv2.imshow("BB", l)
                if self.compare(a, l) == 1:
                    return 1
            cv2.destroyAllWindows()
        return 0

    def compare(self, img1, img2):
        print("entrou")
        k = cv2.subtract(img1, img2)
        b, g, r = cv2.split(k)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
            return 1
        else:
            return 0
    def compare2(self, img1, img2):
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        res = cv2.subtract(img1, img2)
        print(cv2.countNonZero(res))
        cv2.imshow("res", res)
        return

    def rotaciona_imagem(self, img):
        if img.shape[1] > 50:
            img = cv2.rotate(img, 90)
        if img.shape[1] == 51:
            img = cv2.rotate(img, 180)
        return img

    def area_teste(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        binary = cv2.bitwise_not(gray)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        lim = 20
        temp = []
        for contour in (contours):
            (x, y, w, h) = cv2.boundingRect(contour)
            if w > lim and h > lim and w != img.shape[1] and w < 70 and h < 70:
                if (w - h) < 10 or (-10 < (w - h) < 0):
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 1)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    var = img[y:y+h, x:x+w]
                    temp.append(var)
                print("x+w: ", (x + w), "y+h: ", (y+h), "x: ", x, "y: ", y, "w: ", w, "h: ", h)
            cv2.imshow("teste", img)
        cv2.waitKey(0)
        for v in temp:
            cv2.imshow("v", v)

        return temp
    def insere_qrCode(self, img):
        img.shape[1]

Busca_Curvas()
