age = input('Enter your age: ')
age = int(age)

if age < 10:
    print('You are young.')
elif age < 40:
    print('You are strong.')
else:
    print('You are old.')

meaty = input('Do you eat meat? (y/n):')

if meaty == 'y':
    print('Here is the meaty menu.')
else:
    print('Here is the veggie menu.')
