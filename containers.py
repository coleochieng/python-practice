student = {
    'name': 'Ellie',
    'school': 'Heritage Elementary',
    'age': 5
}

''''
name = student['name']
print(name)

student['name'] = 'Olivia'
print(student['name'])
'''

if 'school' in student:
    print( f"{student['name']} goes to {student['school']}")
else:
   print( f"{student['name']} is not enrolled in public school")

student['teacher'] = 'Ms. Otto'
print(student)

del student['teacher']
print(student)

present = 'teacher' in student
print(present)

length = len(student)
print(length)

for key in student:
    print( f'{key} = {student[key]}')

all = student.items()
print(all)

for key, val in student.items():
    print(f'{key} ={val}')







          

