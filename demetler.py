demet = (1,5,1,20)
print(dir(demet))


sozluk = {'one':'bir','two':'[2,10,3,2']}

#print(sozluk.get('two'))

print(dir(sozluk))

sozluk['one'] =1 #kullaılması çok daiyi değil

print(sozluk)
sozluk.update({'two':2})
sozluk.update({'three':2})
#print(sozluk)

sozluk['four']=4

print(sozluk)

del sozluk['one']
print(sozluk)

print(sozluk.pop('two'))

#print(sozluk)
print(sozluk)
print(sozluk.keys())  #başta atana keyletri döndürüür
print(sozluk.values())  #ataann değeri döndürür
print(sozluk.items())  #her ikisini de döndürür




