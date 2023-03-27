student = {
    'name': 'Ellie',
    'school': 'Heritage Elementary',
    'age': 5
}

name = student['name']
print(name)

student['name'] = 'Olivia'
print(student['name'])

print(student.get('mname', 'Geno'))