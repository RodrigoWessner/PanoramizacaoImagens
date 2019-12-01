import cv2
import imutils

def rotacionar(imagem, angulo):
    altura, largura = imagem.shape[:2]
    centro = (largura / 2, altura / 2)
    rotacao = cv2.getRotationMatrix2D(centro, angulo, 1.0)
    rotacionando = cv2.warpAffine(imagem, rotacao, (largura, altura))
    return rotacionando
    #cv2.imshow("Rotacionada", rotacionando)
    #cv2.waitKey(0)

def escalar(imagem, escala):
    altura, largura = imagem.shape[:2]
    centro = (largura / 2, altura / 2)
    escala = cv2.getRotationMatrix2D(centro, 0, escala)
    escalando = cv2.warpAffine(imagem, escala, (largura, altura))
    return escalando
    #cv2.imshow("Escalada", escalando)
    #cv2.waitKey(0)

def encontrarPontos(imagem):
    lf = cf = 0  # LINHA INICIAL E COLUNA FINAL; COLUNA INICIAL E FINAL
    ci = li = 1000 # COLUNA INICIAL E LINHA FINAL
    for x in reversed(range(imagem.shape[0])):  # ALTURA DE BAIXO PRA CIMA
        if x < 300: break #NAO PERCORRER TODA A IMAGEM, CONSIDERA QUE O PONTO PROCURADO ESTEJA NA PARTE INFERIOR DA IMAGEM
        for y in range(imagem.shape[1]):  # LARGURA
            (b, g, r) = imagem[x, y]
            if (b, g, r) == (255, 255, 255):
                if x < li:
                   li = x
                elif x > lf:
                    lf = x
                if y < ci:
                    ci = y
                elif y > cf:
                    cf = y
    li = (lf - 20)
    ci = (cf - 30)
    '''print(li)
    print(lf)
    print(ci)
    print(cf)'''
    #cv2.imshow('aa', imagem[li:lf, ci:cf])
    #cv2.imshow('ab', imagem)
    return li, lf, ci, cf

def encontraReta(imagem, li, lf, ci, cf): #REALIZA A BUSCAC DE BAIXO PARA CIMA NA IMAGEM
    xx1 = xx2 = yy1 = yy2 = -1
    for x in range(li, lf): #PERCORRE ALTURA
        flagi = False
        flagf = False
        x1 = y1 = x2 = y2 = -1
        for y in range(ci, cf):  # PERCORRE LARGURA
            (b, g, r) = imagem[x, y]
            if flagf == False:
                if (b, g, r) == (255, 255, 255) and flagi == False:
                        flagi = True
                elif (b, g, r) != (255, 255, 255) and x1 == -1 and flagi == True:
                    x1 = x
                    y1 = y
                elif (b, g, r) == (255, 255, 255) and flagi == True and x1 != -1:
                    x2 = x
                    y2 = y
                    flagf = True
        if x1!= -1 and x2 != -1 and y1 != -1 and y2 != -1:
            xx2 = x2
            yy1 = y1
            if xx1 == -1:
                xx1 = x1
            if yy2 == -1:
                yy2 = y2
    #print('> ', xx1, xx2, yy1, yy2)
    return xx1, xx2, yy1, yy2

if __name__ == '__main__':
    #GERAÇÃO DO QRCODE
    #Qr = QrCode('Rodrigo e Patrick')
    #imgQR = Qr.criaImagem()
    #imgQR.show()

    #DIVIDE A IMAGEM EM 3
    ImPan = cv2.imread('Im1.jpg')#CARREGA IMAGEM PRINCIPAL
    reta = cv2.imread('reta.jpg') #CARREGA IMAGEM DA RETA
    aux = int(ImPan.shape[1]/3)
    Im1 = ImPan[0:ImPan.shape[0], 0:aux]
    aux += aux
    Im2 = ImPan[0:ImPan.shape[0], aux-int(ImPan.shape[1]/3):aux]
    aux += int(ImPan.shape[1]/3)
    Im3 = ImPan[0:ImPan.shape[0], aux-int(ImPan.shape[1]/3):aux]

    reta = imutils.resize(reta, width=30, height=30)
    Im1[348:369, 376:406] = reta #INSERE RETA A DIREITA NA IMAGEM A ESQUERDA
    Im2[348:369, 376:406] = reta #INSERE RETA A DIREITA NA IMAGEM DO MEIO
    Im2[348:369, 20:50] = reta #INSERE RETA A ESQUERDA NA IMAGEM DO MEIO
    Im3[348:369, 20:50] = reta  # INSERE RETA A ESQUERDA NA IMAGEM A DIREITA
    Im1 = rotacionar(Im1, 7)
    #Im3 = escalar(Im3, 1.10)

    li, lf, ci, cf = encontrarPontos(Im1) # ENCONTRA QUADRO COM A RETA
    x1, x2, y1, y2 = encontraReta(Im1, li, lf, ci, cf) # DENTRO DO QUADRO ENCONTRA OS CANTOS DA RETA
    cv2.imshow('aa', Im1[x1:x2, y1:y2])
    cv2.imshow('a', Im1[li:lf, ci:cf])

    cv2.waitKey()
    cv2.destroyAllWindows()
    #cv2.imwrite("Im3.jpg",Im3)
    #im3.save('Im2.jpg')

