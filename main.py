import qrcode

data = input("QRCode content...\n- ")
file_name = input("File name...\n- ")

img = qrcode.make(data)

img.save(f'{file_name}.png')
