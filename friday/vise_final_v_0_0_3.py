class student:
    def __init__(self,name,surname,number,vise,final):
        self.name = name
        self.surname = surname
        self.number = number
        self.vise = vise
        self.final = final


def show(self):
    print(f"students name: {self.name}\n"
          f"students number: {self.number}\n"
          f"students average: {self.average()} ")


def average(self):
    return self.vise*0.4 + self.final*0.6


class classes(object):
    students=[]

def student_add(self):
    try:
        name = input("student name")surname = input("student surname")
        number=input("student number")
        vise = int(input("vise "))
        final = int(input("final "))
        self.student.append(student(name,surname,number,final=final,vise=vise))
        return True
    except Exception as e:
        print(e)
        return False

def show_students(self):
    for student in self.students:
            student.show()


            def student_delete(self,student_no):
                self.students=list(filter(lambda x: x.numara!= student_no,self.students))
                self.students.remove(student_no)


def classes_average(self):
    from functools import reduce
    average= reduce(lambda x,y:x.average()+y.average,self.students)/len(self.students)

if __name__=='__main__':

    input



    python_1b=classes()
    python_1b.students_add()
    python_1b.show_student()






if __name__ == '__main__':
     name=input("students name")
     surname=input("students surname")
     nunber= input("student numbers")
     vise=int(input("students vise"))
     final=int(input("students final"))
     dogukan = student(name,surname,number,final=final,vise=vise)

     student.show()
