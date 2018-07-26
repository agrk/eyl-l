"""
manav uygulması

1) ürün ekle
2) ürün sil
3) stok görüntüle
4)
"""



def menu():

    secenek=input( """ 
   
1) ürün ekle
2) ürün sil
3) stok görüntüle
   
    """)
    return secenek


def main():
    try:
  """      secenek=int(menu())
    except ZeroDivisionError:
        print("sıfıra bölünme hatası")
        print('hata')
        """
    except ValueError:
        print("harf girdiniz.lütfen sayi girin.")
        main()
    else:
        if secenek == 1:
            menu1()

def menu1():
    print("menu 1")
main()























"""
Manav Uygulaması
1-) Ürün Ekle
2-) Ürün Sil
3-) Stok Görüntüle
"""

def menu():
    secenek=input("""
    1-) Ürün Ekle
    2-) Ürün Sil
    3-) Stok Görüntüle 
    """)
    return secenek

def main():
    try:
        secenek = int(menu())
        # try:
        #     secenek / 0
        # except ZeroDivisionError:
        #     print('Sıfıra bölünme hatası')
    except ValueError:
        print('Harf Girdiniz. Lütfen sayı girin.')
        main()
    else:
        if secenek == 1:
            menu1()
        elif secenek == 2:
            pass
        elif secenek == 3:
            pass

def menu1():
    print("Menü 1")


main()





















