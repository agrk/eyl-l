demet=('a','b','c')
dizi=['a','b','c']
kume={'a','b','c'}

print(demet)
print(dizi)
print(kume)

print(set(dizi))

# yeni_kume={{'a'},'a'}
# print(yeni_kume)

sehir='ankara'
sehir2='istanbul'
sehir_kume=set(sehir)
# print(sehir_kume[0])
sehir2_kume=set(sehir2)

birlesik_kume=sehir_kume.union(sehir2_kume)
print(birlesik_kume)
dizi_birlesik_kume=list(birlesik_kume)
print(dizi_birlesik_kume)


print(" ". join(sehir))    #join icinde ne sectiydem bana o kelimeyi veya diziyi başta nasıl bitr ayrıma işlamei yapmek iistiyorsam jaoin kullna
print("-".join(birlesik_kume))
print("\t".join(dizi_birlesik_kume))