

# students={}


print("welcome to my students listing programme:\n")
while True:
    #print()

   choose=input("""
    1) add student(a)
    2) delete student(d)
    3) look student(l)
    4) delete students(o)
    5) exit(x)\n""").lower()



if choose == 'a':
    std_no= input("enter the student ID.")
    temp_sayac=0


while True:
   temp_sayac +=1
   if temp_sayac==3:
       print("deneme hakkinizi doldurdunuz!")


   if len(std_no)!=9:
       print("student number must be 9 digits")
   continue
   std_vise=input("enter the vize.")
std_final=input("enter the final.")
students.update({std_no : { 'vise' : std_vise,'final': std_final}})
pass

elif choose == 'd':

deleting_std_no= input("please enter the deleting number")

if deleting_sdt_no in students.keys():
    students.pop(deleting_std_no)
    print("{} the number of students will be delete".format(deleting_std_no))

else:
    print("{} the number of students didnt find".format(deletind_std_no))
    pass


elif choose == 'l':

for std_no in students:
    print("""students no:{}
    students vise:{}
    students final:{}""".format(students[std_no],students[std_no].get('vise'),students[std_no].get('final')))
    #print(students)

for std_no, std_notlari in students.items():
        print("""students no:{}
            students vise:{}
            students final:{}""".format(std_no, std_notlari.get('vise'), std_notlari.get('final')))

     pass
     break


elif choose=='c':
pass

elif secim =='o':
students.clear()
printf("list of students deleted")
else
print("bilinmeyen bir komut girdiniz"



























# ogrenciler = {}
# Kullanicinin ne yapmak istedigini sor
# 1) Ogrenci Ekle
# 2) Ogrenci Sil
# 3) Ogrencileri Goruntule
# 4) Cıkış
print("Ogrenci kayit programina hosgeldiniz")
while True:
    ogrenciler = {
        '120101003': {'vize': 80, "final": 90},
        '120101004': {'vize': 60, "final": 100}
    }
    # print()
    secim = input("""
    1) Ogrenci Ekle(e)
    2) Ogrenci Sil(s)
    3) Ogrencileri Goruntule(g)
    4) Ogrencileri Sil (d)
    4) Çıkış(c)\n""").lower()
    if secim == 'e':
        tmp_sayac = 0
        while True:
            ogr_no = input("Ogrencinin numarasini giriniz.")
            tmp_sayac += 1
            if tmp_sayac == 4:
                print("Deneme hakkınızı doldurdunuz.")
                break
            if len(ogr_no) != 9:
                print("Ogrenci numarasi 9 haneli olmalidir")
                continue
            ogr_vize = input("Vize notunu giriniz")
            ogr_final = input("Final notunu giriniz")
            ogrenciler.update({ogr_no : { 'vize': ogr_vize,
                                          'final': ogr_final}
                           })
            break
    elif secim == 'g':
        # print(ogrenciler)
        # for ogr_numara in ogrenciler:
        #     print("""Ogrenci no: {}
        #     Ogrenci vize: {}
        #     Ogrenci Final: {}""".format(ogr_numara,
        #                                 ogrenciler[ogr_numara].get('vize'),
        #                                 ogrenciler[ogr_numara].get('final')))
        for ogr_no, ogr_notlari in ogrenciler.items():
            print("""Ogrenci no: {}
                        Ogrenci vize: {}
                        Ogrenci Final: {}""".format(ogr_no,
                                                    ogr_notlari.get('vize'),
                                                    ogr_notlari.get('final')))
    elif secim == 's':
        silinecek_ogr_no = input("Lütfen silinecek ogr no giriniz.")
        if silinecek_ogr_no in ogrenciler.keys():
            ogrenciler.pop(silinecek_ogr_no)
            print("{} numarali ogrenci silinmistir.".format(
                silinecek_ogr_no))
        else:
            print("{} numarali ogrenci sistemde bulunamadi.".format(silinecek_ogr_no))
    elif secim == 'c':
        break
    elif secim == 'd':
        ogrenciler.clear()
        print("Ogrenci listesi basariyla temizlendi.")
    else:
        print("Bilinmeyen bir komut girdiniz.")

## Eger ogrenci eklemek istiyorsa
## Ogrenci ismini vizesini finalini al
## Sozluge ekle
## Tekrar ana menuye dondur

## Eger ogrenci silmek istiyorsa
## Ogrencinin varligini kontrol et
## Varsa sil ve "başarılı" yazdir, yoksa ogrenci bulunamadi
## Ana menuye don

## Ogrencileri goruntulemek istiyorsa
## Ogrenci listesini ekrana yazdir













