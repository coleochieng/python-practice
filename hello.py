#control flow
color = input('Enter "green", "yellow", or "red": ').lower()
print(f'The user has enetered {color}')

while color != 'quit':
    if color == 'green':
        print('Go!')
        color = input('Enter "green", "yellow", "red": ').lower()
    elif color == 'yellow':
        print('Slow down!')
        color = input('Enter "green", "yellow", "red": ').lower()
    elif color == 'red':
        print('Stop!')
        color = input('Enter "green", "yellow", "red": ').lower()
    else:
        print('Bogus!')
        color = input('Enter "green", "yellow", "red": ').lower()

if color == 'quit':
    print('The user has quit')





