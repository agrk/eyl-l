dosya=open('dosya.txt')

# icerik=dosya.read()

# print(dosya.readlines())  # dosya bir kere okunuyorr
print(dosya)
satirlar=dosya.readlines()
print(satirlar)
dosya. close()



# r-> read
# w-> write
# a-> append
# x-> create

try:
    dosya=open('dosya.txt','a')

    icerik=dosya.readline(10)   #kac karakter okunaxcağını gösterir
    # cleaned_icerik=[]
    # for line in icerik
    #     cleaned_icerik.append(satir.strip())
    # print(cleaned_icerik)
    icerik=[satir.strip() for satir in icerik]
    dosya.close()
except Exception:
    print("dosya yoktur")