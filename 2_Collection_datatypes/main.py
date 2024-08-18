'''
List 
    - list is a collection datatype that is capable of holding more than 1 variable
    - its very similar to Array but has 1 fundamental difference
    - it is heterogeneous for these u can put in any type of value {any datatypes}
    - it is denoted with '[' brackets
    - Each value has index or location associated
'''

# address = [0,1,2,3,4]
list_var = [1,2,3,4,5]
print(list_var,type(list_var),list_var[0],len(list_var))

print('...'*22)

for i in range(0,len(list_var)):
    print(list_var[i])

for list_element in list_var:
    print(list_element)


print('...'*22)

list_var_2 =[1,2,3,4,5,6,7,8,9,10]

for i in range(0,len(list_var_2)):
    
    if(list_var_2[i] % 2 == 0):
        print(list_var_2[i])

print('...'*22)

list_var_4 =[]
for i in range(0,100):
    
    if(i % 2 == 0):
        list_var_4.append(i)
print(list_var_4)

print('...'*22)

#slicing in list
list_var_5 = [1,2,3,4,5]
print(list_var_5[1:3])

#using pop
list_var_5.pop(2)

print(list_var_5)
list_var_5.pop(3)

print(list_var_5)



'''
DIctionary val
'''

dictionary_val = {
    'key_1' : 10,
    'key_2' : 20
}

print(dictionary_val['key_1'])
print(dictionary_val.keys(),dictionary_val.values())



print('...'*22)

#aApproach 1 using list

list_keys=['apple','ball','cat']
value_list=['red','blue','white']
dictionary_val_2=dict(zip(list_keys,value_list))
print(dictionary_val_2)

#task 4
questions=['what is national animal','who isprime minister','what is capital']
answer=['cow','kp oli','kathmandu']
dictionary_val_3=dict(zip(questions,answer))


# uQuestion = str(input('Enter your question'))

# print('The answer is', dictionary_val_3[uQuestion])

#approach 2 using update
dict_var_1 = {'key_1': 10, 'key_2': 20}
print(dict_var_1['key_1'])

dict_var_1.update({'key_3':30,'key_4': 50})
print(dict_var_1)



#reverse using recursive
#string = Apple

def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]
    
output=reverse('apple')
print(output)