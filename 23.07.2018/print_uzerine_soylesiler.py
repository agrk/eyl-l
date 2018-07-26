print("hava cok guzel",sep='\t\t')
sansur={'hava: "H*va'}
cumle="hava cok guzel"
for karakter in cumle:
    if karakter ==" ":
        print('\t\t',end="")
        continue
        print(karakter,end="")
        print()
        cumle=cumle.replace(' ','\t\t')
        print(cumle)