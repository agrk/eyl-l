

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



###############################################################################################################################


class Motorcycle(object):

 def __init__(self,tyre):
     self.tyre=tyre
     def show(self):
         print(self.tyre)
         sezer_hocanin_chopperi=Motorcycle(2)
         sezer_hocanin_chopperi.tyre=10
         dogukan_hocanin_motoru=Motorcycle(3)
         print(sezer_hocanin_chopperi.tyre)
         print(dogukan_hocanin_motoru.tyre)





















