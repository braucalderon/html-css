# sun
import math

class Sun:

    def __init__(self, name, radius, mass, temp, volume, distance):

        self.name = name
        self.radius = radius
        self.mass = mass
        self.temp = temp
        self.volume = volume
        self.distance = distance

    def getName(self):
        ''' returns self name '''

        return self.name

    def getRadius(self):
        ''' returns self radius'''

        return self.radius

    def getMass(self):
        '''returns mass * (10**27)'''
        
        return self.mass * (10**27)
    
    def getDistance(self):
        '''returns self diatance'''

        return self.distance

    def getTemperature(self):
        ''' returns self temperature'''

        return self.temp
        
    def getVolume(self):
        ''' returns self Volume'''

        v = self.volume * (10**27)

        return v

    def getDensity(self):
        ''' returns mass / getVolume()'''

        d = self.mass / self.getVolume()

        return d

    def __str__(self):
        ''' returns all the ionformation in the class '''

        return '\n' +\
               '____________________________' + '\n' +\
               'THE STAR' + '\n''\n' +\
               'The ' + self.name + ' has a radius of ' + str(self.radius) + ' mi' +\
               ' with a mass of ' + str(self.mass) + ' 10^30 kg ' + '\n' +\
               'which is about ' + str(self.getMass()) + '\n' +\
               'and with a surface temperature of ' + str(self.temp) + ' K' + '\n' + '\n' +\
               'The Volume of the ' + self.name + ' is: ' + str(self.volume) + ' x 10^27' + '\n' +\
               'The Density of the ' + self.name + ' is: ' + str(self.getDensity())
               
               
               
            

    
