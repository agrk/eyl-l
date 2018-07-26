## bastan tekrar
#
# print ofnksıyonu ve ozellikleri
# yuz_olcumu="200"
# tevellut="1990"
# print("burasi cok guzel sen de gelsene ")
# print("bizim koyun yuz olcumu" + yuz_olcumu + "tevelletu" + tevellut)
# print("bizim koyun yuz olcumu{} tevellutu {}".format(yuz_olcumu,tevellut))
# print("bizim koyun yuz olcumu{yo} tevellutu {tv}".format(yo=yuz_olcumu,tv=tevellut))
# # print("bizim koyun yuz olcumu ". join(yuz_olcumu))   #joının kullanım amacaı birleştirme işlemi iki veriyi bir araya getitir
# priit("""ornek\n
#     ornek\t""")
# print("ornek degisken",end="")
#
# print("burada tirnak'kullandim")
# print(" burada tirnak \" ")      #onemli bir nokta
# ilk_parca="bizim koyun yuz olcumu"
# print(ilk_parca[0])
# for gelecek_sey in ilk parca:
#      print(gelecek_sey)
# print("hava cok guzel",sep='\t\t')
# cumle="hava cok guzel"
# for karakter in cumle:
#      if karakter ==" ":
#       print('\t\t')
#          continue
# print(karakter,end="")
#         cumle="\t\t".join(cumle.split(" "))
# cumle=cumle.replace(' ','\t\t')
#
#
#
# # degisken turleri nelerdir
# ilk="ornek"
# iki=10
# uc=10.0
# ornek=True
# kocaman_sayi=2354723452857056096350693456098
#
#


# input fonksiyonu ve tip donusumlari


# ad=input("adınız")     #sayilarda aslında bir string eğer sayisal mislem yapacaksam int e göre tip donusumu kullnaırım





# liste nedir? nerelerde kullanilir?
#
# bu_bir_listedir=["bir","kac","tane","bilinen","degisken"]
# farkli_liste=["baska","liste"]
# bu_bir_listedir.append(farkli_liste)
# print(bu_bir_listedir)
# bu_bir_listedir.
# bu_bir_listedir.append({"bu":"sozluktur"})
# for degisken in bu_bir_listedir:      #for ile cagırdıgımız icin alt alta yazdirdi
#     if type(degisken)== dict:
#         print(degisken.get("bu", ))
#         continue
#     print(degisken)

# print(bu_bir_listedir[3][0:5])   # : ile yazdırmak istediğimiz yere kadar olan herfleri secebiliyoruzz,  bir : nokta daha koyup sayı yazarsak kacar kacar gidecegimizi secebiliriz
# print("listeninn ilk hali: {}".format(bu_bir_listedir))
# siralanmis_liste=sorted(bu_bir_listedir,reversed=True)
# print("listenin sorted fonksiyonundan sonraki hali: {}\n siralanmis hali:{}".format(bu_bir_listedir,siralanmis_liste))
# bu_bir_listedir.sort()
# print("sort fonksiyonun calistiktan sonraki hali: ")
# print(bu_bir_listedir)
# print(siralanmis_liste)

#
# liste1=['a','b','e']
# liste2=['c','d']
# yeni_liste=[]
# yeni_liste.extend(liste2)
#
# yeni_liste.extend([*liste1])
# liste1.extend(liste2)                # yildiz degiskenleri aktarir
#                                      #yerler değişerek aslında birbirlerinie eklnme sıraları da değiştirilebilir
# print(liste1)
# print(liste2)
# print(yeni_liste)
#
# print(list(*liste1))
#
#

###sort olursa direkt degiskenin kendisine mudajhale eder sorted olursa ama deiskene dokunmadan sıralayıp bize son halini gonderir###

# set











# sozlukler

# ozel_meyveler=["portakal",'cilek','madalina']
# meeyveler={'yaz_meyveleri':
#                {'sevdiklerimiz':['avokado','guantanamo elması','carkıfelek'] ,
#                 'sevmediklerimiz':['elma','armut','kiraz']
#                 },
#            'kis_meyveleri':{
#                'ozlediklerimiz':"portakal cilek mandalina",
#                "efsaneler":0
#
#
#            }}

#print(meyveler['yaz_meyveleri'])

# print(meyveler.get('yaz_meyveleri'))
# if meyveler.get("bahar meyveleri"):
#   print(meyveler.get("bahar_meyveleri"))
# elif meyveler.get("sonbahar_meyveleri"):
#     print(meyveler.get('sonbahar_meyveleri'))
# else:
#     meyveler.update({'bahar_meyveleri':{}})
#     meyveler
#
# print(meyveler)
#

# l_meyveler=[[
#     ['avokado','guantanamo elması','carkifelek'],
#     ['elma','armut','kiraz']],
# [[],
#  []]]
#
#
#
#


# kosullu ifadeler

# degisken=['a','b','c']
# degisken2= degisken
#
# if degisken==degisken2:
#     print("1")
#     print(id(degisken),id(degisken2))
#
# if degisken is degisken2:
#     print("2")
#     print("ikinci ornek:\n\n")
#
# degisken = ['a', 'b', 'c']
# degisken2 = degisken[:]
#
# if degisken == degisken2:
#     print(id(degisken),id(degisken2))
#     print("1")
#
# if degisken is degisken2:
#     print("2")

# donguler for ve while
"""
sayilar=[]

for say in range(1,10):
    if say%2 == 0:
        sayilar.append(say*say)
    print(sayilar)
    sayilar2=[say*say for say in range(1,10) if say % 2 == 0]
print(sayilar2)

"""


# fonksiyonlar
#
# def write(word):
#     print(word)
#     return 10
#
# # degisken=write('meyve')
# # print(degisken)
#
#
# def args_yazdir(ilki,ikinci,*args):
#     print(args)
#     print(birinci)
#     print(ikinci)

    # args_yazdir(1,2,3,4,5,6)
#
# def kwargs_yazdir(bir=1,**kwargs):
#         print(kwargs)
#         print(bir)
#         kwargs_yazdir(bir=1,iki=2)
#
#
#
# def args_kwargs_yazdir(ilki,ikinci,*args,bir,hasan,**kwargs):
#     print(ilki)
#     print(ikinci)
#     print(args)
#     print(bir)
#     print(kwargs)
#
#     args_kwargs_yazdir(9,8,7,6,1,2,hasan=2,bir=1,test=10)
#
#


def dongu():
    for i in range(1,10):
        yield str(i)

        for x in dongu():
            print(x)
    print(dongu())
    print(dongu())
    print(list(dongu()))


# hata kontrol yapisi
# args ve kwargs kavramlari
# bir kac tane varsayilan fonksiyonlar(len,type,range,  )
# dosya islemleri

def open_file(name_of_file):
    file=open(name_of_file,'r')
    return file

file=open_file('file.txt')

#print(file.readline())
#print(file.readline())



def open_file(name_of_file):

    file=open(name_of_file,'a+')
    return file

def file_read(file):
    return file.read()

def write_file(file,*args):

    file.write()
    pass


#bir dosyayı okuyacak
#okuduklarını diger dosyaya yazacak


# dosya.txt dosyasını başka dosyaya kopyalayın

file=open_file('file.txt')


print()























