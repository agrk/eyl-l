
sayi = input("bir sayi giriniz: ")


rakamlar = {"1": "Bir", "2": "İki", "3": "Uc", "4": "Dort", "5": "Bes",
            "6": "Alti", "7": "Yedi", "8": "Sekiz", "9": "Dokuz"}
onlar = ["On", "Yirmi", "Otuz", "Kirk", "Elli", "Altmis", "Yetmis", "Seksen", "Doksan"]
eklenecekler = ["Bin", "Yuz"]


sayicumlesi = " "
birlerbasamagi = 0
sayac = 0

for i in range(len(sayi)):
    if (len(sayi) == 4):
        if (sayac <= 1):
            if ((int(sayi[1]) != 0) or (i != 1)):
                if ((int(sayi[1]) != 1) or (
                        i != 1)):
                    sayicumlesi += rakamlar[sayi[
                        i]] + " "
                sayicumlesi += eklenecekler[sayac] + " "
            sayac = sayac + 1

        else:
            if birlerbasamagi == 0:
                if (int(sayi[2]) != 0):
                    sayicumlesi += onlar[int(
                        sayi[i]) - 1] + " "  

                birlerbasamagi = 1
            else:
                if (int(sayi[3]) != 0):
                    sayicumlesi += rakamlar[str(sayi[i])]
        print (sayicumlesi)
