#Importing a module. I.e. importing from another python file
from classes import Planet

hoth = Planet()

print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')