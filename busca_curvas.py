import cv2
from matplotlib import pyplot as plt
import numpy as np


class Busca_Curvas:
    def __init__(self):
        pass

    def equaliza(self):
        src = cv2.imread("pano1.png")
        src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        src_eq = cv2.equalizeHist(src_gray)
        cv2.namedWindow("source_window", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("source_window", src_gray)

        plt.figure()
        plt.hist(src_eq.ravel(), 256, [0, 256])
        plt.title("Histograma Equalizado")
        plt.show()
        cv2.namedWindow("src_equalized", cv2.WINDOW_AUTOSIZE)
        cv2.imshow("src_equalized", src_eq)

        # hist = cv2.calcHist(src_gray, [0], None, [256], [0, 256])
        plt.figure()
        plt.title("Histograma Original")
        plt.hist(src_gray.ravel(), 256, [0, 256])
        # plt.plot(hist)0
        plt.show()
        cv2.waitKey(0)


    def area_teste(self):
        #img = cv2.imread("pano1_azul.png", -1)
        img = cv2.imread("pano1.png", -1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        binary = cv2.bitwise_not(gray)
        cv2.imshow("cinza", gray)

        (contours, hierarchy) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for contour in (contours, hierarchy):
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("teste", img)
        cv2.waitKey(0)



Busca_Curvas().area_teste()