import qrcode


qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

url = input("URL: ")

qr.add_data(url)
qr.make(fit=True)

img = qr.make_image()
img.save("url.png")