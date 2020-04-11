import math


class Planet:
    
    def __init__(self, name, radius, dis, mass, rotation, moons):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = dis
        self.moons = moons
        self.rotation = rotation

    
    def getName(self):
        ''' returns name of the object'''

        return self.name
    
    def getRadius(self):
        ''' return the radius of the object'''

        return self.radius
   
    def getDistance(self):
        ''' return the distance of the object'''

        return self.distance 
    
    def getMass(self):
        ''' return the mass of the object'''

        return self.mass

    def geRotation(self):
        '''return the rotation around the soon of the opbject'''

        return self.rotation 

    
    def getNumMoons(self):
        ''' returns the number of moons of the object'''

        return self.moons
    

    def getVolume(self):
        ''' return the volkume of the object by the above calculation'''

        v = (4/3) *math.pi* (self.getRadius()**3)

        return v
   
    def getCircumference(self):
        '''returns the ciscumference of the object'''

        c = 2* math.pi * self.getRadius()

        return c
   
    def getSurfaceArea(self):
        ''' returns the surface area of the object'''

        sa = (2 * math.pi * (self.getRadius()**2))

        return sa

   
    def getDensity(self):

        den = (self.mass / self.getVolume())

        return den
    
    def addMoon(self, name):
        ''' check if moon is not on the list'''

        if name not in self.getNumMoons():
            m = self.getNumMoons().append(name)
        else:
            # it does return the list intact without changes
            # if moon no in the list 
            m = str('not found')

        return m

    def removeMoon(self, name):
        ''' remove moon of the object'''
        
        for i in self.getNumMoons():
            if i in name:
                a = self.getNumMoons().remove(i)
            else:
                # it does return the list intact without changes
                # if moon no in the list 
                a = str('Not found')
        return a

    
    def __str__(self):
        ''' return all the information about the planest by calling the class'''

        return '\n' +\
               '--------------------------' + '\n' +\
               'Planet ' + self.name + ': \n\n' +\
               'The radius of the planet is ' + str(self.radius) + ' mi' + '\n' +\
               'The planet has a distance of ' + str(self.distance) + ' million/billion mi from the Sun,\n' +\
               'with a mass of ' + str(self.mass) + ' M' + ' and\n'  +\
               'with an orbit period of ' + str(self.rotation) + ' days / years.\n\n' +\
               'Volume of ' + str(self.getVolume()) + ' kg\n' +\
               'Density of ' + str(self.getDensity()) + ' g/cm^3\n' +\
               'Circumference of ' + str(self.getCircumference()) + ' million mi^2\n' +\
               'Surface Area of ' + str(self.getSurfaceArea()) + ' mi\n\n' +\
               'The planet has ' + str(len(self.moons)) + ' moon(s):\n' + str(self.moons) + '\n'
               


 
    
               
               
               

    

        
    
