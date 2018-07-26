# been bir sayı yazacağım ama karşılığında rakam halşnde alacağım
#
import math

def oku(sayi):

    birler={"0": "", "1":"bir","2":"iki","3":"üc","4":"dort","5":"bes","6":"altı","7":"yedi","8":"sekiz","9":"dokuz"}
    onlar={"1":"on","2":"yirmi","3":"otuz","4":"kırk","5":"elli","6":"altmıs","7":"yetmis","8":"seksen","9":"doksan","0":" "}
    yuz={"yuz","ikiyuz","ucyuz","dortyuz","besyuz","altıyuz","yediyuz","sekizyuz","dokuzyuz"}
    if len(sayi) == 3:
        if sayi[0] == "1":
            oku = yuz[0 ] +onlar[sayi[1] ] +birler[sayi[2]]
            return oku
            if sayi[0] == "0":
                oku = onlar[sayi[1] ] +birler[sayi[2]]
                return oku
            else:
                oku = birler[sayi[0] ] +yuz[0 ] +onlar[sayi[1] ] +birler[sayi[2]]
            return oku
        if len(sayi) == 1:
            if sayi[0] == "0":
                oku = "Sifir"
                return oku
            else:
                oku = birler[sayi[0]]
                return oku
        if len(sayi) == 2:
            oku = onlar[sayi[0] ] +birler[sayi[1]]
            return oku
            sayi = raw_input("Sayiyi Giriniz :")
            basaSifirEkle = len(sayi) % 3
            if basaSifirEkle == 1:
                sayi = "00 " +sayi
            elif basaSifirEkle == 2:\
                sayi = "0 " +sayi
            else:
                sayi = sayi
#
# kacYuzlerVar =  math.ceil(int(len(sayi) ) /3.0)
#
# ucluGrub = {"0" :"" ,"1" :"Bin" ,"2" :"Milyon" ,"3" :"Milyar" ,"4" :"Trilyon" ,"5" :"Katrilyon"}
#
# oku = " "
# for i in range(int(kacYuzlerVar)):
#     if sayi[- 1 *(( i *3 ) +3) ] +sayi[- 1 *(( i *3 ) +2) ] +sayi[- 1 *(( i *3 ) +1)] == "000":
#         oku = oku
#     elif sayi[- 1 *(( i *3 ) +3) ] +sayi[- 1 *(( i *3 ) +2) ] +sayi[- 1 *(( i *3 ) +1)] == "001" and len(sayi) == 6:
#             oku = ucluGrub[str(i)] + oku
#     else:
#         oku = ucHaneOku(sayi[- 1 *(( i *3 ) +3) ] +sayi[- 1 *(( i *3 ) +2) ] +sayi[- 1 *(( i *3 ) +1)]) + ucluGrub
#         [str(i)] + oku
#

print(oku)