test_degiskeni= "bu bir test degiskenidir"
print(test_degiskeni.upper().lower())   #büyütür ---küçültür
print(test_degiskeni.capitalize())
test_degiskeni= " bu bir test degiskenidir"
print(test_degiskeni)
print(test_degiskeni.strip())  #boşlulkları  silerr
test_degiskeni ="\r\n bu bir test degiskenidir"
print(test_degiskeni)

x=5
y=10
print (x+y)     #bu şekilde 15 çıktısı verir

x=5
y=10
print(x+y)      #bu şekilde 510 çıktısı verir, string olarak algılar


a=5
b=2
c=a/b
print(c)    #kendi kendine int türünü float yapacak ve sonucu 2.5 çıkacak


a=5
b=2
c=int(a)/b   #bu şekile türr değişimi yapılabililr

dogru = True  #baş harfleri büyük olmalı
yanlıs=False  # baş harfleri büyük olmalı
print(dogru)

print(type(dogru))  #tipini bool olduğunu gösterdi çıktı olarak
print(dogru==False)  #bu çalışınca compare mekanizması çıktı nolartak False çıkartır


liste = [x,y,"elma",dogru,c]

print(liste)   #listenin ilk halini yazdırır

liste.append("armut")   #listenin sonuna ekler
liste.insert(0,"yeni")   #ilki indextir yazılan indexe ne girileceğini ise sonr ayazarız


liste=[x,y,"elma",dogru,c]

print(liste)  #listenin ilk ghalini yazdırır

liste.append("armut")  #listenin sonuna ekler
liste.insert(0,"yeni")   #ilki indextir yazılan indexe ne  girileceğini ise virgülden sonra yazarız
cikarilan= liste.pop()   #boş iken en başkakini çikarir ve atadigin degiskene cikarilani da atar


print(liste)
print(cikarilan)


print(liste)

cikartilan = liste.remove('5')   #liste.remove(liste[4])

print(cikarilan)


liste2=[5,4,3,2,1]
liste.append(liste2)
#print(liste[8][2])

#print(liste[liste.index(liste2)])
liste.extend(liste2)
#print(liste)


liste3=liste2.sorted(liste2)


#sort içeriği değilitir


#print(liste2)
#print(liste3)


liste4=[2,6,1,9,10,2]

liste4.sort(reserve=True)
#print(liste4)
liste4.reserve()
#print(liste4)


#print(liste4.count(1))

#print(len(liste4))

print(max(liste4))   #veya bir de yazabiliriz




























