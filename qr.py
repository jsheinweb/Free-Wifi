import qrcode

url = "https://l5hfnxzx-5500.asse.devtunnels.ms/"

img = qrcode.make(url)
img.save("monkey_qr.png")

print("QR code created: monkey_qr.png")
