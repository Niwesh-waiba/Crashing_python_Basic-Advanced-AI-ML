''' 
Libraries / Packages

- Collection of codes and resources that has a lot of functions and operations already written for us


'''

import pandas as pd

''' 
pandas library:
    - pandas is equivalent to SQL for python, SQL already exists for python but pandas is more suited for AI works
    - works on table, read table, modify, save and everything related to table
'''

dictionary_variable={
    'student':['Ram', 'Shyam', 'Sita', 'Gita'],
    'Marks': [10,20,30,40]

}


#pandas operation 1

data_frame_variable = pd.DataFrame(dictionary_variable)   #higher level abstraction convert dictionary to dataframe (table)
print(data_frame_variable)

#adding new column
data_frame_variable['Social Skills']=[10,20,30,40]
print(data_frame_variable)


# Removing column

data_frame_variable=data_frame_variable.drop(columns=['Social Skills'])
print(data_frame_variable)


''' 
task 1



'''

# questions = []
# answers = []

# N = int(input('Enter Number of Questions?'))
# for i in range(N):
#     questions.append(input('Enter the Question'))
#     answers.append(input('Enter the Answer'))
# dictionary_val=dict(zip(questions,answers))
# print(dictionary_val)

# df = pd.DataFrame(dictionary_val)
# print(df)

#looking up certain row loc, iloc'
print("--"*25)
failed_students = data_frame_variable.loc[data_frame_variable['Marks']<=32]
print(failed_students)


#saving dataframe to csv
data_frame_variable.to_csv('Data.csv',index=False)

#loading from csv
new_data_frame=pd.read_csv('Data.csv')
print('loaded from data')
print(new_data_frame)

print(new_data_frame.iloc[1])