import  qrcode


#message que vous voulez encoder dans un code QR
message = input("votre message : ")

#générer notre code QR en définissant la taille des pixels, le niveau d'erreur et la taille de la marge autour du code QR

CodeQR = qrcode.QRCode(version=8,error_correction=qrcode.ERROR_CORRECT_L,box_size=20,border=2)
CodeQR.add_data(message)
CodeQR.make(fit=True)

#créer une image du codeQR et l'enrégistrer
img = CodeQR.make_image(fill_color="black",back_color="white")
img.save("codeQR.png")



