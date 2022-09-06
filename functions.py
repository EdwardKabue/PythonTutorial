# def greet():
#     print('Hello world.')

# def greet(name='Ryu', time='morning'):
#     print(f'Good {time} {name}')

# name = input('Enter your name: ')
# time = input('Enter the time of day: ')

# greet(name, time)
#greet() #Uses default argument values
#greet(name='Shaun') #Pass one of the argunents

def area(radius):
    return 3.142 * radius * radius

def vol(area, height):
    print(area * height)

radius = int(input('Enter a radius: '))
height = int(input('Enter a height: '))

area_calc = area(radius)

vol(area_calc, height)