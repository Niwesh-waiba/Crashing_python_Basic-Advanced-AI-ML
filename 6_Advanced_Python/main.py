'''

1. List comprehensions and generator Expressions
list comprehensions are a concise way to create lists in python
they are faster than using a for loop to create a list
'''


list_variables=[1,2,3,4,5]
list_variables=[]
list_variables.append(1)
list_variables.append(2)
list_variables.append(3)
print('--'*25)


odd_numbers=[i for i in range(1,100,2)]
print(odd_numbers)



'''
list comprehension works best when we are working with very simple data modificaions or conditions
when complex conditions arise list comprehension is difficult to code



'''


a=[1,2,3,4,5]
#mini task
# u have a list a=[1,2,3,4,5] create list b which has each element of a squared, b=[1,4,9,16,25]

b=[]
for element in a:
    b.append(element**2)

print(b)

print('--'*25)

b=[element**2 for element in a]
print(b)

#even off using if
even_numbers=[i**2 if i%2==0 else i**3 for i in range(1,100)]
print(even_numbers)
'''

Generator in python
    -Special type of function that returns multiple 
    -def function_name():
        yield statement
'''

#simple generator:
def simple_generator_function():
    yield 'a'
    yield 'b'
    yield 'c'

for value in simple_generator_function():
    print(value)

print('--'*25)
x =  simple_generator_function()
print(next(x))
print(next(x))
print(next(x))

#generator Expression
'''
Create generator object very similar to list comprehension
'''

square_gen=(x**2 for x in range(10))  #generator Expression!!
print(square_gen)
print(list(square_gen))

# Task

'''
Create a generator operator that yields all the even numbers using generator expression
create a infinite loop where user is asked to type something
if the user types next
display the next value of generator operator
when the iteration is over the loop must exit (hint: using try except to handle this situation)

'''

# even_gen=(i for i in range(1,10) if i%2==0)  #generator Expression!!
# while True:
#     userInput= input('Enter next for next')
#     try:
#         if userInput=='next':
#             print(next(even_gen))
#     except:
#         break


'''
lamda:
     
    -lambda function are often reffered as anonymous function
    -for very short and sweet operation
    - These functions are used in conjunction with higher level functions like maps, filter, so on
'''

x=lambda parameter:parameter**2
print(x(5))
sum_of_2_numbers=lambda parameter1,parameter2: parameter1+parameter2
print(sum_of_2_numbers(1,2))

'''
Task 2, given a list_1=[1,2,3,4,5,6,7,8,9,10] create a lambda function that returns half of that value and pass
each element of this list to that function and save everything in new list (using list comprehension)

list_2=[0.5,1.5,2.5....]
'''

list_1=[1,2,3,4,5,6,7,8,9,10]

halff= lambda parameter:parameter/2
list_2=[halff(item) for item in list_1]
print(list_2)



#using if else inside lambda 
get_greater_number= lambda x,y:x if x>y else y
print(get_greater_number(10,20))



'''
wap to basically take in N (N=number of elements on a list)
Loop till N times and get different numbers 
put all the numbers in a list named list_variable 
create a lambda function that takes in parameter1, return 'even' if the number is even
and 'odd' if the number is odd
using list comprehension create another list named odd_even_list it should contain all the output of lambda function
passed over each element of list variable
finally create a dataframe with 2 columns number, even/odd
number column should have list_variable on it and Even/odd column should have odd_even_list
display the final dataframe


'''

import pandas as pd

userInput=int(input('enter number of elements on the list'))
numbersList=[]
for i in range(userInput):
    numbersList.append(int(input('enter the number')))
print(numbersList)
even_odd_number= lambda x:'even' if x%2==0 else 'odd'
even_odd_list=[even_odd_number(i) for i in numbersList]

mydict={
    'Number':numbersList,
    'even/odd': even_odd_list,
}
print(pd.DataFrame(mydict))



'''
map, filter and reduce

- Map takes in function and collection and iterates all element 
one by one over that function

- map can also be used to map out 2 different parameters
from 2 different collections over a function

'''

print('--'*25)

list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
output_of_map=list(map(lambda x:x**2,list_of_numbers)) #syntax map(function,list/iterables)
print(output_of_map)

print('--'*25)

def add_squared_numbers(x,y):
    return x**2+y**2

list_a=[1,2,3,4,5]
list_b=[6,7,8,9,10]

output_of_map_2=list(map(add_squared_numbers,list_a,list_b))
print(output_of_map_2)

'''
task
1.take N from user (number of elements)
2. Create a list of length N asking number from user (ask numbers and put it in a list)
3. Create another list of length N asking number from user (2nd list created with first list)
4. using map figure out which from both list add up to 10.Concat the 2 numbers and display the result in the list

list_a=[1,2,3,4,5]

list_b=[9,2,7,6,0]
[]
'''


# def concatTen(x,y):
#     if x+y==10:
#         return str(x)+str(y)
    

# N = int(input("Enter the number of elements: "))

# list1 = []
# print("Enter numbers for the first list:")
# for _ in range(N):
#     number = int(input())
#     list1.append(number)
# list2 = []
# print("Enter numbers for the second list:")
# for _ in range(N):
#     number = int(input())
#     list2.append(number)

# result = list(map(concatTen, list1, list2))


# print("The concatenated numbers that add up to 10 are:", result)



'''
Filter

    -Filter works very similar to map
    -It takes functions and iterables as input

    -returns output whenever its true
'''


numbers=[1,2,3,4,5]
evens_map=(list(map(lambda x:x%2==0,numbers)))
evens=list(filter(lambda x:x%2==0,numbers))
print(evens)
print(evens_map)


'''
given a list =['apple',  'ball' , 'cat', 'dog', 'elephant']
create another list of words which have length > 3 
from the given list
'''
list_ap =['apple',  'ball' , 'cat', 'dog','elephant' ]
list_bp=list(filter(lambda x:len(x)>3,list_ap))
print(list_bp)

#reduce
'''
    -[1,2,3,4,5]
    -multiply(x,y) -> x*y
    - reduce(function, iterable, initial_value)
    -it runs the function one by one in cumulative way
    from left to right
    [20,3,4,5]
        [1,2,3,4,5] -> [multiply(1,2),3,4,5]
        [multiply(2,3),4,5]

    '''
from functools import reduce
list_of_numbers=[1,2,3,4,5]
output=reduce(lambda x,y:x*y,list_of_numbers)
print(output)

'''
create a list taking N like done previously
pass the list to function square and add 4(x)
return x**2+4

-using map create transition_list_1 passing over the function

-using filter create another transition list 2 
which accepts only those numbers divisible by 5

-Finally create sum of all the numbers of transition list using reduce
'''


from functools import reduce

N = int(input("Enter the number of elements: "))

numbers_list = []
print("Enter the numbers:")
for _ in range(N):
    number = int(input())
    numbers_list.append(number)

def square_and_add_4(x):
    return x**2 + 4

transition_list_1 = list(map(square_and_add_4, numbers_list))

transition_list_2 = list(filter(lambda x: x % 5 == 0, transition_list_1))

sum_transition_list_2 = reduce(lambda x, y: x + y, transition_list_1, 0)

print("Original List:", numbers_list)
print("Transition List 1 (x^2 + 4):", transition_list_1)
print("Transition List 2 (Divisible by 5):", transition_list_2)
print("Sum of Transition List 2:", sum_transition_list_2)


#Decorators
'''
    -Decorators are special function that takes in other functions as parameter
    - Decorators are understood by the code editors with @
'''

print('--'*25)

def smart_conversion(func):
    def wrapper(x,y):
        return  func(int(x),int(y))
    return wrapper

@smart_conversion
def division(x,y):
    return x/y

@smart_conversion
def addition(x,y):
    return x+y

print(addition('1','2'))



'''
task 
Create a function named division()-> that divides 2 number
addition()-> that adds 2 number
subtraction()-> that subtract 2 number
multiplication()->  that multipleis 2 numbers

 function structure should be something like this
 def addition(x,y):
    return x+y

create a decorator named identify_function_and_Parameters
that should display which function is running
and what are its parameters

at the end result should be something like this
division(10,20)

output->division running 

'''


def identify_function(func):
    def wrapper(x,y):
        return(f" name{func} is running with parameter {x} and {y} result {func (x,y)}" )
    
    return wrapper

@identify_function
def division(x,y):
    return x/y

@identify_function
def addition(x,y):
    return x+y
@identify_function
def subtraction(x,y):
    return x-y
@identify_function
def multiplication(x,y):
    return x*y

print(addition(20,10))

print(division(20,10))

print(subtraction(20,10))

print(multiplication(20,10))