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
          
          

