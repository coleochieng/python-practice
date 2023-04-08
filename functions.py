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
'''
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


