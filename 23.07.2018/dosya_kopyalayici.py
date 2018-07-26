# Verdiğim dosya isminin İçerisindeki veriyi okuyup, verdiğim dosyaya yazan program

# Verilen dosya ismine sahip dosyayı okuyan ve içeriğini bana dönen bir fonksiyon
def dosya_oku(dosya_adi):
    with open(dosya_adi, 'r') as f:
        icerik = f.read()
        return icerik
# Parametre olarak verilen dosyaya yine verilen iceriği yazan fonksiyon
def dosya_yaz(dosya_adi, icerik):
    with open(dosya_adi, 'w') as f:
        f.write(icerik)
    return True

dosyanin_icerigi = dosya_oku('file.txt')
dosya_yaz('kopyalanan.txt', dosyanin_icerigi)