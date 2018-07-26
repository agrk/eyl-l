print("hava cok guzel",sep='\t\t')
cumle="hava cok guzel"
for karakter in cumle:
    if karakter ==" ":
        print('\t\t',end="")
        continue
        print(karakter,end="")
        print()
        cumle=cumle.replace(' ','\t\t')
        print(cumle)