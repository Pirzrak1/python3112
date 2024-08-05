import qrcode
qr = qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10, border=4)
print("Give a link for qr code:")
a = input("")
qr.add_data(a)
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("img_qr.png")
