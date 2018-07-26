# import math
#
# print(math.log10(20))
# print(math.cos(30))
# print(math.pow(2,4))
# print(math.sqrt(16))
# print(math.pi)



##yıcapı girilen dairenin cevresi ve ala# nı

#
# import math
# r=int(input("yarıcap giriniz"))
#
# def cevre(r):
#
#     hesapla=(math.pi)*2*r
#     return hesapla
#
# def alan(r):
#
#     hesapla2=(math.pi)*(sqrt(r))
#     return hesapla2
#
#
# print(hesapla)
# print(hesapla2)
##################################33
"""
import math


r=int(input("yarıcap girinz"))

sphere=(math.pi)*2*r
print(sphere)

area=(math.pi)*(math.sqrt(r))
print(area)

"""


##############iki noktanın biribirine olan uzaklığı ##############

#####uzaklık(x,y,x2,y2)
"""
import math

koorX1= int(input("x degerini giriniz"))
koorX2= int(input("x 2 degerini giriniz"))


koorY1=int(input("y degerini giriniz"))
koorY2=int(input("y 2 degerini girinz"))


def uzaklik(*args):
    return math.sqrt(math.pow((args[2]-args[0]),2) + math.pow((args[3]-args[1]),2))

mesafesi = uzaklik(koorX1, koorY1, koorX2, koorY2)
print(mesafesi)

################################################################################################################

from math import sqrt
import random

def uzaklik(*args)
    sonuc=sqrt((args[2]-args[0])**2 + (args[3]-args[1])**2 )
    return sonuc

def main():
    x1,x2,y1,y2= random.randint(1,20),\ random.randint(1,20),\random.randint(1,20),\ random.randint(1,20)

    sonuc=uzaklik(x1,x2,y1,y2)
    print("f({x1},{x2},{y1},{y2}) "f" arasındaki uzakllık:{sonuz}")


main()
  """
####################################################################################################################

  #kullanıcıdan bir zar tahmin alacak
  #dogru ise +1 puan,yanlıssa -1 puan
  #oyundan cıkınca puanı ekrana basacak





import random

def zar_oyunu(sayi):

    zar=random.randint(1,6)
    if sayi==zar:
        return True
    return False


def main():
    sayi=0
    puan=0
    while True:
        sayi= int(input("tahmininiz:  "))
        if sayi!= 7:
            if zar_oyunu(sayi):
                puan+=1
                print("dogru bildiniz puanininz:",puan)
            else:
                puan-=1
            print("yanlis tahmin puanininiz:",puan)

        else:
            print("oyun bitti",str(puan))

        main()



















   # if tahmin == sayi:
   #   print("dogru tahmin")
   #   puan+=1
   # else:
   #   print("yanlış tahmin")
   #   puan+=-1
   #
   # return(puan)
   #
   #
   # return sayi
   #




def tahmin(sayi):

    sayi=random.choise(liste)
    if tahmin == sayi:
        print("dogru tahmin")
        puan+=1
    else:
        print("yanlış tahmin")
        puan+=-1
        return sayi
        print(puan)

main()





































































