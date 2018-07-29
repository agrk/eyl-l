"""

class Motorcycle(object):             ##bos olarak da kalabilyor grnrl kukllanımı öyle
 tyre=2
 parts=['gidon','tekrar']

 def __init__(self,tyre):
     self.tyre=tyre
    # print('worked')
def show(self):
    print(self.tyre)

motor=Motorcycle(2)

print(Motorcycle)
print(motor)
print(motor.tyre)

"""

###############################################################################################################################
"""
class Motorcycle(object):
    tyre=2
    def __init__(self,tyre):
        self._tyre=tyre                   ##korunan degisken procted
        self.__motor='Btwin'              ##privete sadece calss içreinde erişilebilir

    def get_tyre(self):
        return self._tyre
        def set_tyre(self,tyre):
            self._tyre=tyre

        def show(self):
            print(self.tyre)
            
sezer_hocanin_chopperi=Motorcycle(2)
sezer_hocanin_chopperi.tyre=10
dogukan_hocanin_motoru=Motorcycle(3)
print(sezer_hocanin_chopperi.tyre)
print(dogukan_hocanin_motoru.tyre)
print(sezer_hocanin_chopperi._tyre)
print(sezer_hocanin_chopperi.__motor)

"""
###############################################################################################################

"""

class Student(object):

    def __init__(self,name,surname,number,moms_name,father_name):
        self.name=name
        self.surname=surname
        self.number=number
        self.moms_name=moms_name
        self.father_name=father_name

        def student_show(self):
        

            def moms_adi_change(self,cici_moms_name):
                self.moms_name=cici_moms_name


        sezer=Student('sezer','bozkir',120101003,'gonul','can')
        sezer.name='dogukan'
        sezer.student_show()

"""
#####################################################################################################################

# classes ile ogrenscinin notunu al yazdır

class student(object):

    def __init__(self,name,surname,vise,final):
        self.name=name
        self.surname=surname
        self.vise=vise
        self.final=final
        print(self.name,self.surname, self.vise,self.final )

    def avg(self):

        avg = lambda vise, final: (vise * 0.4) + (final * 0.6)
        return avg



class classes(object):

 def add_Student(self,student):
     classes_list[]:

     name=input("ogrenci ismi")
        surname=input("ogrenci soyismi")
        vise=int(input("vise notu"))

        final=int(input("final notu"))
        anystudent=student(name,surname,vise,final)
        classes_list.append(anystudent)

    ogrenci_list=


    def remove_Student(self,student):
   # self.ogrenci=
        pass

    def show(self,student):
        print("N:{} I:{} S:{}".format(self.name, self.surname, self.vise,self.final ))
        pass

    def classes_avg(self,student):
        pass

    def main(self):



if __name__ == '__main__':
    sınıf = classes()



###  TAMAMLANMASI LAZIM TEKRAAR BAK #####











































