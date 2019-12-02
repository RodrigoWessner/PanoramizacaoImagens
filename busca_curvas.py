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

    def escreve(img, texto, cor=(255, 0, 0)):
        fonte = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0, cv2.LINE_AA)

    def area_teste(self):
        img_colorida = cv2.imread("pano2.png")
        img = cv2.cvtColor(img_colorida, cv2.COLOR_BGR2GRAY)
        suave = cv2.blur(img, (7, 7))

        T = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
        bin = suave.copy()
        bin[bin > T] = 255
        bin[bin < T] = 0
        bin = cv2.bitwise_not(bin)

        bordas = cv2.Canny(bin, 70, 150)
        (lx, objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        temp = np.vstack([
            np.hstack([img, suave]),
            np.hstack([bin, bordas])
        ])
        cv2.imshow("Quantidade de objetos: " + str(len(objetos)), temp)
        cv2.waitKey(0)
        imgC2 = img_colorida.copy()
        cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
        self.escreve(imgC2, str(len(objetos)) + " objetos encontrados!")
        cv2.imshow("Resultado", imgC2)
        cv2.waitKey(0)


Busca_Curvas().area_teste()