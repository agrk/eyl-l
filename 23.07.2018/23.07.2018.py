
"""

def us_alma (deger_1,deger_2):

    sonuc=deger_1** deger_2
    print("sonuc: {}".format(sonuc))
    return sonuc
try:
    deger1=input("lütfen ilk degeri giriniz")
    deger2=input("lütfen ikinci degeri giriniz")
    sonucu=us_alma(deger1,deger2)
except ValueError as e:
    print(e)
    print("lütfen sayi degeri giriniz")
except Exception:
    print("bir hata olustu :(")
else:
    print(sonucu)



if type(deger1)==int and type(deger2)==int:
    sonucu=us_alma(deger1,degere2)
    print(sonucu)
    
else:
    print("lütfen sayi giriniz")


sonucu= us_alma(deger1,deger2)
print(sonucu)


"""

def topla_cikarma(say1,say2,topla=True):
    return say1+ say2 if topla else say1-say2
    #if topla:
    #    return say1+say2
   # return say1-say2                     #bu durumda eger durum true ise birinci return yapılacak ikinciye ghecmeyecek bile

deger1 = input("lütfen ilk degeri giriniz")
deger2 = input("lütfen ikinci degeri giriniz"

topla_cikarma(say2=deger1,say1=deger2)



