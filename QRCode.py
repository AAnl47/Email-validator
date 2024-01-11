import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)

qr.add_data("https://wa.me/918877777663")

qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="pink")
img.save("whats.png")
