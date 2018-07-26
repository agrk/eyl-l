birler = [None, "bir", "iki", "uc", "dort", "bes", "altı", "yedi", "sekiz", "dokuz"]
onlar = [None, "On", "Yirmi", "Otuz", "Kirk", "Elli", "Altmis", "Yetmis", "Seksen", "Doksan"]

sayi="1234"
sayi = sayi[::-1]

okunus=[]
okunus.append(birler[int(sayi[0])])

if len(sayi)>=2:
    okunus.append(onlar[int(sayi[1])])
    if len(sayi)>=3:
        if sayi[2]=="1":
            okunus.append("yuz")
        else:
            okunus.append(birler[int(sayi[2])]+"yuz")
        if len(sayi)>=4:
            okunus.append(birler[int(sayi[3])] +"bin")

        print(okunus)
        print(" ".join(okunus[::-1]))




# binler de 1 olduğunda patlıyorr onlara uğraş
