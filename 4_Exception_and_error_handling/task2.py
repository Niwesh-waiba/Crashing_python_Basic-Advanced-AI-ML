'''
    task3 : wap that first gives 2 options
    1:sign up
    2: sign in

    when 1 is pressed user needs to provide following info
    1: username , 2: Password 3: mobile nummber
    all this info must be saved a file everytime a new user signs up the same ffile is updated

    when 2 is pressed 
    user needs to provide username and password
    this username and password is checked with username and password in the database if  
    if matchedL
        welcome to the device and show the phone number
    else :
        terminate the program saying invalid credentials

'''




import json

to_save_dictionary={
    'userName': ['Ram', 'Shyam', 'Sita'],
    'Password': [10,20,30],
    'phoneNumber':[987654,3324432234,34324324],
 }

with open('userData.json','w') as f:
    json.dump(to_save_dictionary,f)

with open('userData.json','r') as f:
    loaded_json=json.load(f)

print(loaded_json)


def addUser(userName, password, phoneNumber):
    with open('usersData.json','a') as f:
        f.write(userName+','+ password+','+phoneNumber)
    
def displayUser():
    with open ('usersData.json','r') as f:
        displayUser=f.readlines()
        print(displayUser)

while True:
    choice = input('Enter \n1 for sign up \n2 for sign in \n3 to quit')
    if  choice == '1':
        userName = input('Enter Username')
        password = input('Enter password')
        phoneNumber = input('Enter phoneNumber')
        addUser(userName,password,phoneNumber)
    elif choice =='2':
        displayUser()
    elif choice =='3':
        break
    else:
        print('Invalid choice')

