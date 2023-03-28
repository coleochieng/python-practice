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

where_my_things_are = {
    'phone': 'fanny pack',
    'glasses': 'bedside table',
    'computer': 'bookbag',
    'lotion': 'bathroom'
}

for key, val in where_my_things_are.items():
    print(f'My {key} is kept {val}')

'''

scores = [
    {
     'name': 'Bill',
     'points': 25
    },
    {
     'name': 'Bob',
     'points': 30
    }
]

for score in scores:
    print(f"{score['name']} scored {score['points']} points")







          

