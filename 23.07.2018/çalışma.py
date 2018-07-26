def choose menu():

     choose=input("""           
         1) add student(a)      
         2) delete student(d)             
         3) look student(l)               
         4) delete students(o)            
         5) exit(e)\n""")
     return choose

def main():
    print("Ogrenci kayit programina hosgeldiniz")
    while True:
        students= {
            '120101003': {'vize': 80, "final": 90},
            '120101004': {'vize': 60, "final": 100}
        }




    try:
        choose=int(input(menu()))

    except ValueError:

        print("have to enter digit")
        main()


    else:
        if choose=='a':
            menu1()
            pass
        elif choose=='d':
            menu2()
            pass

        elif choose=='l':
            menu3()
            pass
        elif choose=='o':
            menu4()
            pass
        elif choose == 'e':
            menu5()
            pass
            

def menu1():
    print("menu 1")
std_no= input("enter the student ID.")
std_vise=input("enter the vize.")
std_final=input("enter the final.")
menu1.update({std_no : { 'vise' : std_vise,'final': std_final}})
pass

main()


def menu2():
    print("menu 2")
deleting_std_no= input("please enter the deleting number")
if deleting_std_no in students.keys():
students.pop(deleting_std_no)
print("{} the number of students will be delete".format(deleting_std_no))
else
print("{} the number of students didnt find".format(deleting_std_no))





def menu3():
    print("menu 3")

    for std_no, std_no in students.items():
                print("""Ogrenci no: {}
                            Ogrenci vize: {}
                            Ogrenci Final: {}""".format(std__no,
                                                        std_no.get('vize'),
                                                        ogr_notlari.get('final')))















    print("""students no:{}
    students vise:{}
    students final:{}""".format(students[std_no],students[std_no].get('vise'),students[std_no].get('final')))


def menu4():
    print("menu 4")
        students.clear()
print("list of students deleted")
else
print("bilinmeyen bir komut girdiniz")




def menu5():
    print("tekrar deneyin")
    return main()