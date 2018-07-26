def print_soz():
    print('hello world!')
    print('hello venüs')


#def iki_defa_yazdır():

#yazdir_soz()

#iki_defa_yazdir()

def dondur_soz():
    return "hello world"

def iki_yazdir(soz):
    print(soz)
    print(soz)

def iki_yazdir(soz):
    print(soz)
    print(soz)
    iki_yazdir(soz)



 #soz=dondur_soz()
#iki_yazdir(soz)



  # yazdir(dondur_soz())   #içinde merhaba dün ya yazıyor aslında
"""

def hata_dondur():
    raise ValueError("value error verdi")
#int('a')

#hata_dondur()
try:
    hata_dondur()
    x=5                                      #trydan sonra x kullanılacaksa yukarda tanımlanması lazım

except:
    print("diger hata")
else:
    print("hata yok")
    print(x)


"""






def main(arg1=10):


    raise ValueError("value error verdi")
try:
    x=dondur_soz()
  #  hata_dondur()

except:
    print("diger hata")
else:
    print("hata yok")
    print(x)

finally:
    print('sürekli çalıştı')



def yeni(arg1=10):
    liste=list(range(1,20,4))
    print(liste)
    liste.sort(reserve=True)
    print(liste)
    print(arg1)

    yeni(30)














