# Solar_System.py
import operator


class Solar_System:
    
    def __init__(self, name, distanceG, distanceG1, star1, stardis1,
                 star2, stardis2, minorplanets, nameK, distanceK, sun):
        
        self.name = name
        self.distanceG = distanceG
        self.distanceG1 = distanceG1
        self.star1 = star1
        self.star2 = star2
        self.stardis1 = stardis1
        self.stardis2 = stardis2
        self.distanceK = distanceK
        self.nameK = nameK
        self.sun = sun
        self.minorplanets = minorplanets
        self.planets = []

    
    def addPlanets(self, aplanet):
        '''append each planet into self.planets array'''
        
        self.planets.append(aplanet)

    def showPlanets(self):
        ''' sort the planets by distance shorter to larger from the sun'''
        
        planets = sorted(self.planets, key = lambda p:p.distance)
        #print(planets)
        for aplanet in planets:
            print(aplanet)
        
    def getName(self):
        ''' returns name of the object'''

        return self.name

    def getDistanceG(self):
        '''return distance of the object for galactic center'''

        return self.distanceG

    def getDistanceG1(self):
        '''returns a second distance for galactic center'''

        return self.distanceG1

    def getSun(self):
        '''return sun for later use in the str function'''

        return self.sun

    def getStar1(self):
        '''returns another solar system star's name'''

        return self.star1

    def getStar2(self):
        '''returns another solar system star's name'''

        return self.star2

    def stardis1(self):
        '''returns distance for another solar system'''

        return self.stardis1

    def stardis2(self):
        '''returns distance for 2nd solar system'''

        self.stardis2

    def getMinorPlanets(self):
        '''returns number of minor planets around the solar system'''

        return self.minorplanets

    def getNameK(self):
        '''returns the name of the circumstellar disc in our outer Solar System'''

        return self.nameK

    def getDistanceK(self):
        '''returtns the system of the circustellar disc'''

        return self.distanceK

    def getPlanets(self):
        '''return the number of planets for later use in str'''

        planets = {'Saturn':'E', 'Mercury':'A','Mars':'D', 'Jupiter':'F',
                   'Neptune':'J', 'Earth':'C', 'Uranus':'X', 'Venus':'B'}

        return planets

    def __str__(self):
        '''returns all the information about the solar system'''

        return '\t''\t''\t''\t' + self.name + '\n''\n' +\
               'Our Solar System has a distance of ' + str(self.distanceG) +\
               ' +/- ' + str(self.distanceG1) + ' ly '+ ' to the Galactic Center' + '\n' +\
               'Nearest stars: ' + str(self.star1) + ' ' + str(self.stardis1) + ' ly'  +\
               ' and ' + str(self.star2) + ' ' + str(self.stardis2) + ' ly' + '\n''\n' +\
               'Known minor planets: ' + str(self.minorplanets) + ' as of 2018-04-23' + '\n' +\
               'Distance to ' + str(self.nameK) + ': ' + str(self.distanceK) + ' AU' + '\n''\n' +\
               'The Solar System has a ' + str(self.sun) + ' with '+ str(len(self.getPlanets())) +\
               ' planets.'
    
