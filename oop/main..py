class Animal:
    def what_sound_does_it_make(self,flag):
        if flag.lower()=="bark":
            print('hey its a dog')
        elif flag.lower()=='meow':
            print('hey its a cat')
        else:
            print('Its a human')

species_1 = Animal()
species_1.what_sound_does_it_make('bark')
\
species_2 = Animal()
species_2.what_sound_does_it_make('meow')

species_3 = Animal()
species_3.what_sound_does_it_make('nkj')


print ('--'*25)


''' 
create a class named calculator , that must have following methods
add 2 number(), subtract 2 number(), multiply, and divide
create 2 different instances of calculator (create 2 object ) and run those methods
'''

class Calculator:
    def add(self,num1,num2):
       print(int(num1) + int(num2))
    def subtract(self,num1,num2):
       print(int(num1) - int(num2))
    def multiply(self,num1,num2):
       print(int(num1) * int(num2))
    def divide(self,num1,num2):
       print(int(num1) / int(num2))

calc_1 = Calculator()
calc_1.add(1,2)
calc_1.multiply(1,2)
calc_1.divide(1,2)
calc_1.subtract(1,2)
