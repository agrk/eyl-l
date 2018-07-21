
#0-40 dc
#41-60 cb
#61-80 bb
#80-100 aa

vize=int(input("vize notu"))
final=int(input("final  notu"))

#sonuc = int(input("notunuzu giriniz"))     #br şeyi inputla alıuorsak ınu string alır

#if type(vize)== "int" and type(final)== "int":
#if 0 < vize < 100 and 0 <final <100:
 #   sonuc =(vize*40 +final*60)/100
  #  print("notunuz dc")

   # if 40 < sonuc <=60:
    #    print("notunuz cb")
     #   if 60 < sonuc <= 80:
      #      print("notunuz bb")
       #     if < 80 kul_not <=100:
        #        print("notunuz aa")
         #   else:
          #      printf("tanımsız")

       # else:("lütfen sayi giriniz:")


print(gecici_vize, type(gecici_vize))
print(gecic_final,type(gecici_final))



def ortalama_hesapla(gecici vize,gecici final):   #gloabal bir şekilde değişken yukarda kullanıldıysa içerde tekerar kullnamak verim kaybıne neden olanş--bilr

if type(gecici vize) == "int" and type(gecici final) == "int":
    if 0 < vize < 100 and 0 < final < 100:
        sonuc = (gecici vize * 40 + gecici final * 60) / 100
        print("notunuz dc")

        if 40 < sonuc <= 60:
            print("notunuz cb")
            if 60 < sonuc <= 80:
                print("notunuz bb")
                if < 80 sonuc <= 100:
                    print("notunuz aa")
                else:
                    printf("tanımsız")

            else:
                ("lütfen sayi giriniz:")


                ogr_1_vize= int(input("ilk ögrencinin vizesini giriniz"))
                ogr_1_final= int(input("ilk ogrencinin final notunu giriniz"))

                ortlama_hesapla(ogr1_vize, ogr_1_final)

        """"
  sayi = int(input("vize notunu giriniz"))
  
   vize=sayi*0.4

sayi2 = int(input("final notu"))

final= sayi2*0.6       
        
        tplm=vize+final
        
   print( tplm)
    
    
    
        
        """