import qrcode

name = input("name khod ra vared kon: ")
phone = input("shomare hamrah khodra vared kon: ")

data = f"name: {name}, phone: {phone}"

qr = qrcode.make(data)
qr.save("qrcode.png")

print("code qr shoma zakhire shod 'qrcode.png'")


#qrcode tamrin...
