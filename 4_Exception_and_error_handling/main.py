'''
Exception of Error handling !!
    -sometimes there might be some kind of logical error in our code 
    -Exception handling has mainly 2 parts:
        try:
            code in try block(code that is trying  to be executed)
        except:
            if code fails rest of the part runs here

'''

# x=int(input('Enter numerator: '))
# y=int(input('Enter denominator: '))
x=1
y=0
try:
        
    output= x/y
    print(output)
except Exception as e:
    print(e)


import random

a=random.randint(1,100)
print(a)


''' 
Task: start infinite loop, get random numerator and denominator, calculate total number of
crashes and if total number of crashes == 100 terminate the program

'''


# crash = 0

# while crash<2:
#     try:
#         num1=random.randint(0,100)
#         num2=random.randint(0,100)
#         output= num1/num2
#         print(output)
#     except Exception as e:
#         crash =+ 1
#         print('crashed' , crash)




'''
File Handling


'''


user_name = input('Enter username')

password = input('Enter password')
print(user_name,password)

# writing in file
with open('database.txt','a') as f:
    f.write(user_name+' '+password)



print('--'*25)
#reading a file
with open ('database.txt','r') as f:
    from_file_output=f.readlines()
print(from_file_output)


'''task 2: wap that first ask 2 questions:
    1: write notes
    2: read notes

    if 1 is pressed the program directs u to write a long note, as that note 
    is written or completed, the note is stored in databse.txt file

    if 2 is pressed all the written notes are displayed



'''

def addnotes(note):
    with open('database.txt','a') as f:
        f.write("\n "+note)
    
def readNote():
    with open ('database.txt','r') as f:
        readnoteee=f.readlines()
        print(readnoteee)

while True:
    choice = input('Enter \n1 for writing notes \n2 for reading notes \n3 to quit')
    if  choice == '1':
        newNote = input('Please enter the note')
        addnotes(newNote)
    elif choice =='2':
        readNote()
    elif choice =='3':
        break
    else:
        print('Invalid choice')


