'''
def first_function():
    pass

result = first_function
print(result)

def add(a, b):
    return a + b

print(add(6, 3))


def artist_work(artist_name, *args):
    artist = {'name': artist_name, 'songs': []}
    for song in args:
        artist['songs'].append(song)
    return artist

print( artist_work('Radiohead', 'Nude', 'Separator', 'Little by Little', 'Lotus Flower') )


def fave_albums(genre, *args):
    best_of = {'name': genre, 'albums': list(args)}
    return best_of

print( fave_albums('rock', 'Oracular Spectacular', 'King of Limbs', 'In Rainbows', 'Is This It') )



def album_rank(artist, **kwargs):
    list = {'name': artist, 'albums': kwargs}
    return list
print( album_rank('Kanye', MBDTF=2, Yeezus=3, Graduation=1) )

#from example
def arg_demo(pos1, pos2, *args, **kwargs):
  print(f'Positional params: {pos1}, {pos2}')
  print('*args:')
  for arg in args:
    print(' ', arg)
  print('**kwargs:')
  for keyword, value in kwargs.items():
    print(f'  {keyword}: {value}')

arg_demo('A', 'B', 1, 2, 3, color='purple', shape='circle')


#write a function with required positional, optional positional, and keyword arguments

def immigrant_family(original_country, new_country, *args, **kwargs):
    print( f"My parents moved from {original_country} to {new_country} when they were 20. They have the following kids: ")
    for arg in args:
        print(' ', arg)
    for keyword, value in kwargs.items():
        print( f"{keyword} is {value} years old")

print( immigrant_family('Kenya', 'America', 'Nicole', 'Chloe', 'Olivia', 'Ellie', Nicole=24, Chloe=11, Olivia=8, Ellie=6))



#functions lab
#challenge 1: Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
def sum_to(x):
    ans = 0
    for n in range(1, x + 1):
        ans += n
    return ans

print( sum_to(6) )
print( sum_to(10) )



#challenge 2: Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(num):
    num.sort()
    highest = num[-1]
    return highest

print( largest([10, 4, 2, 231, 91, 54]) )


#challenge 3: Write a function named print( occurrences that takes two string arguments as input and counts the number of print( occurrences of the second string inside the first string.

def occurrences(text, instance):
    return text.count(instance)

print( occurrences('fleep floop', 'e') )  # returns 2
print( occurrences('fleep floop', 'p') )  # returns 2
print( occurrences('fleep floop', 'ee') ) # returns 1
print( occurrences('fleep floop', 'fe') ) # returns 0


#challenge 4: Write a function named print(  that takes an arbitrary number of numbers, multiplies them all together, and returns the print( .
def product(*args):
    value = 1
    for arg in args:
        value *= arg
    return value

print( product(-1, 4) ) # returns -4
print( product(2, 5, 5) ) # returns 50
print( product(4, 0.5, 5) ) # returns 10.0
'''
