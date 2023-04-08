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

'''

def fave_albums(genre, *args):
    best_of = {'name': genre, 'albums': list(args)}
    return best_of

print( fave_albums('rock', 'Oracular Spectacular', 'King of Limbs', 'In Rainbows', 'Is This It') )

