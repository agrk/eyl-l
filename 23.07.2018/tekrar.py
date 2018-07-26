
#sozluk yazimi

def ornek_fonksiyon(*args):
    print("ahmet",sap="#",end="\n\n")

    def yazdirma(*args):
        yazdirilacaklar=args[:-2]
        bitirici=args[-1]
        ayirici=args[-2]
        for kelime in yazdirilacaklar:
            print(kelime,end='',sep='')
            print(ayirici,end='',sep='')
        #     print(bitirici)

        print(*yazdirilacaklar,sep=ayirici,end=bitirici)



        def kw_yazdirma(**kwargs):
            print(kwargs)
            print(kwargs.get('yazdirilacaklar'),sep=kwargs.get('ayirici'),end=kwargs.get('bitirici'))
            pass


        kw_yazdirma(yazdirilacaklar=["ahmet","mehmet","ayse","fatma"],ayirici="#22",bitirici='bitirdik')



        def args_kwargs_yazidrma(*args,**kwargs):
            print(args)
            print(kwargs)

            args_kwargs_yazdirma("ahmet",ayirici='#',bitirici='bitirdik')







def args_kwargs_yazdirma(*args,**kwargs):
    print(*args,sep=kwargs.get('ayirici'),
          end=kwargs.get('bitirici'))


kwargs={
    'atirici:'#',
'bitirici':'bitirdim'
           'gir }
    args_kwargs_yazdirma("ahmet","mehmet",ayirici='#', bitirici='bitirdim')



 #   yazdirma("ahmet","mehmet","ayse","fatma","#22",'bitirdik')




"""

def fonk(*args):

    print("merhaba", sep="""""", end=".")
    fonk("merhaba","dünyalı")



"""
































