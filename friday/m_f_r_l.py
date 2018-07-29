

#lambda map filter reduce
#
# def carpma(say,say2):
#     return say*say2                    ##def ile tanımlayığ yaptıgımız islem aslında

a=lambda say1,say2: say1*say2          ##(lambda) sol tarafa alınacak degerler sag tarafa yapılacak islem yazılır, islemleri tek satırda yapmış oluruz
b=lambda deger: deger
#
# def sayi_dondur():
#     for say in range(1,10):
#         yield say
#
# # return say
#
#
# siradaki=sayi_dondur()
# # sonraki=sayi_dondur().__next__()
# print(siradaki.__next__())
# print(siradaki.__next__())
# print(siradaki.__next__())
#

############################################333333333

# print(b("ornek"))
# print(a(10,15))
#
#
# bir_dizi_var = [5,10,2,18,21,55]
# string_deger=[]
# for deger in bir_dizi_var:
#     string_deger.append(str(deger))

# yeni_deger = map(b, bir_dizi_var)                   #her deger üzzerinde gezip verdiğimiz fonksiyonu bir parametre olarak kullanır

# print(list(yeni_deger))
# print(list(yeni_deger))                             #list payarsam cursor özelliğini yani tek tek gzme işlemini yok temiş olurum

#    # print(list(yeni_deger))
#
# # print(bir_dizi_var,string_deger,sep="\n")
#
#print(yeni_deger)

#############################################################################################

# sonuc=filter(lambda say:say%2==0,bir_dizi_var)               #şartın true olduğu oldurmlarda döndürüyor ve sadecec doğru değerleri alıp yazdırıyor
# print(list(sonuc))

#################################lamda map reduce####################################################################

bir_dizi_var = [5,10,2,18,21,55]
def carpma(say,say2):
   return say*say2


sonuc = filter(lambda say:say % 2 == 0, behzat_c)
from functools import reduce
print(behzet_c)
toplam=0
for deg in behzat_c:
    toplam+=deg
    print(toplam)

    resp=reduce(lambda x,y:x*y,behzat_c)
    print(resp)
#####################################################################################################################


































