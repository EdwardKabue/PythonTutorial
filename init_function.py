#Blueprint for how an object should look.
class Planet:
     shape = 'round' #Class level attribute. Used for attributes shared across instances.

    #self is the instance of the object that is to be created.
    def __init__(self, name, radius, gravity, system):
        #instance attributes
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    #instance method because it takes self as an argument
    def orbit(self):
        return f'{self.name} is orbiting the {self.system}.'

hoth = Planet('Hoth', 100000000, 5.6, 'Hoth System')

print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(hoth.orbit())

naboo = Planet('Naboo', 3000000, 8, 'Naboo System')
print(f'Name is: {naboo.name}')
print(f'Radius is: {naboo.radius}')
print(f'Gravity is: {naboo.gravity}')
print(naboo.orbit())

print(naboo.shape) #class attribute can be returned from instance.