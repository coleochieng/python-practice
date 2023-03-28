'''
student = {
    'name': 'Ellie',
    'school': 'Heritage Elementary',
    'age': 5
}

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

'''

#Exercise 1
students = ['Ann', 'Beth', 'Catherine', 'Doris', 'Emma', 'Fiona']
print(students[1])
print(students[-1])


#Exercise 2
foods = ('apple', 'banana', 'cantaloupe', 'date', 'eggplant', 'fish')
for food in foods:
    print( f"{food} is a good food")


#Exercise 3
for food in foods[-2:]:
    print(food)


#Exercise 4
home_town = {
    'city': 'Pleasantville',
    'state': 'North Carolina',
    'population': 5000
}
print( f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")


#Exercise 5
for key, val in home_town.items():
    print( f"{key} = {val}")


#Exercise 6
cohort = []
for idx, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[idx]
    })
print(cohort)


#Exercise 7
awesome_students = [ f"{name} is awesome!" for name in students]
for student in awesome_students:
    print(student)











          

