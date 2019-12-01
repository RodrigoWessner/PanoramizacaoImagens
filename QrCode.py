import qrcode

class QrCode(object):
    def __init__(self, nome):
        self.Nome = nome

    def criaImagem(self):
        return qrcode.make(self.Nome)
