import qrcode

url = "http:// 10.60.186.58:500/"

img = qrcode.make(url)
img.save("monkey_qr.png")

print("QR code created: monkey_qr.png")
