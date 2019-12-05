# Import QRCode from pyqrcode 
import pyqrcode
from pyqrcode import QRCode


# String which represent the QR code
def generate_qrCode():
    s = "Patrick Martini, " \
        "Rodrigo Wessner - " \
        "Trabalho de Computacoo Grafica"

    url = pyqrcode.create(s)
    url.svg("myqr.svg", scale=1)
    return
