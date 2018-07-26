

##enumrate bize index sıra numarı verir
dizi=[[None, "bir", "iki", "uc", "dort", "bes", "altı", "yedi", "sekiz", "dokuz"],
[None, "On", "Yirmi", "Otuz", "Kirk", "Elli", "Altmis", "Yetmis", "Seksen", "Doksan"],]

sayi="38"
sayi = sayi[::-1]


okunus=[]
for i,s in enumerate(sayi):
    print(i,s)
    okunus.append(dizi[i][int(s)])

  #  okunus.reserve()    ##böyle yazzdığıpmda çalışmadı ikinci yazılan son halde çalışan

    print(" ".join(reversed(okunus)))
    print(okunus)


