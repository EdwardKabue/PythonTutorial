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
    
    @classmethod
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    #A static method does not have access to self and the class(cls). Only access parameters passed into it individually.
    @staticmethod
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}.'