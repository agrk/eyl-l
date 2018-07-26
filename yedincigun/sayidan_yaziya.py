
def sayi_yazdir(say):

    birler=["sıfır","bir","iki","uc","dort","bes","altı","yedi","sekiz","dokuz"]
    onlar = [" ","On", "Yirmi", "Otuz", "Kirk", "Elli", "Altmis", "Yetmis", "Seksen", "Doksan"]


basamak_degeri=len(say)

if basamak_degeri == 1:
    print(birler[int(say)])
elif basamak_degeri == 2:
    if int(say[1])!=0:
        print(onlar[int(say[0])],birler[int(say[1])])
else:
    print(onlar[int(say[1])])
if basamak_degeri == 3:
elif int(say[0])!=1 or int(say[0])!=0 :
    print(birler[int(say[0])],"yuz",onlar[int(say[0])],birler[int(say[1])])
else:
    print("yuz",onlar[int(say[1])],birler[int(say[2])])




say = input("sayi giriniz")
sayi_yazdir(say)

