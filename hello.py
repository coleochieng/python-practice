#control flow
color = input('Enter "green", "yellow", or "red": ').lower()
print(f'The user has enetered {color}')

if color == 'green':
    print('Go!')
    color = input('Enter "green", "yellow", or "red": ').lower()
elif color == 'yellow':
    print('Slow down!')
    color = input('Enter "green", "yellow", or "red": ').lower()
elif color == 'red':
    print('Stop!')
    color = input('Enter "green", "yellow", or "red": ').lower()
else:
    print('Chloe... follow instruction')
    color = input('Enter "green", "yellow", or "red": ').lower()





