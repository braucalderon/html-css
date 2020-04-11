class Planet:

  def __init__(self,name,rad,mass,moonsList,dist):
    self._name = name
    self._radius = rad
    self._mass = mass # in 10^25 pounds
    self._moonsList = moonsList
    self._distance = dist

  # position 1
  def getName(self):
    """ returns the name of the planet """
    
   
    return self._name
  
  # position 2
  def getRadius(self):
    """ returns the radius of the planet, in miles """

   
    return self._radius
  
  # position 3
  def getDistance(self):
    """ returns the distance to the sun """
    
  
    return self._distance
  
  # position 4
  def getMass(self):
    """ returns the mass of the planet, in 10^25 pounds """
    
    return self._mass * (10**24)
  
  # position 5
  def getNumMoons(self):
    """ returns the number of moons the planet has """

    
    return self._moonsList
  
 
  def getCircumference(self):
    """ returns the circumference of the planet
        C = 2 * PI * r """
    c = (2 * 3.14 * self.getRadius())
    return c

  
  def getVolume(self):
    """ returns the volume of the planet
        v = 4/3 * PI * r^3 """
    
    v=(4/3)*3.14*(self.getRadius()**3)

    return v

  
  def getSurfaceArea(self):
    """ returns the surface area of the planet
    sa = 4 * PI * r^2 """

    
    sa = 4 * 3.14 * (self.getRadius()**2)
    return sa

  # position 9 
  def getDensity(self):
    """ returns density of the planet
        d = mass / volume """
    d = self.getMass() / self.getVolume()
    return d

  def addMoon(self,name):
    """ adds the moon with name <name> to the list of the planet's moons"""
    
    if name not in self.getNumMoons():
      t=self.getNumMoons().append(name)
      
    return t
      
  def removeMoon(self,name):
    """ removes the moon named <name> from the list of the planet's moons,
    if the moon is not in the list, does nothing"""
    
    for i in self.getNumMoons():
    
      if i in name:
        h=self.getNumMoons().remove(i)
        
    return h 
        

  def setMass(self,value):
    """ updates the planet's _mass"""
    value = self.getMass()
    
    return value

  def __str__(self):
    """ prints the information about the planet """
    return "Planet " + self._name + ':\n' + \
       "has " + str(len(self._moonsList)) + " moon(s): " + \
       str(self._moonsList) + '\n' + \
       'its radius is ' + str(self._radius) + " miles, and \n" + \
       'Its mass is ' + str(self._mass) + "x10^25 pounds,\n" + \
       'its distance to the sun is ' + str(self._distance) + ' miles.\n'


def main():
  earth = Planet("Earth",3958.8,1.31668,['Moon'],92.96*10**6)
  neptune = Planet("Neptune",22.5819495,15299.401,["Triton","Naiad","Thalassa","Despina","Galatea","Larissa","S/2004 N 1","Proteus","Nereid","Halimede","Sao","Laomedeia","Psamathe","Neso"],2.795*10**9)

  print(earth)
 
  print(neptune)

  print("\nEarth's radius is ",earth.getRadius()," miles")
  print("\nEarth's Density is ", earth.getDensity())

  print("\nNeptune has ",neptune.getNumMoons()," moons")
  print("\nDistance from Neptune to Sun is ",neptune.getDistance()," miles")

  print("\nEarth's circumference is ",earth.getCircumference()," miles")

  print("\nLet's add the moon Lida to earth.")
  earth.addMoon("Lida")
  print("\nNow earth has ",earth.getNumMoons()," moons")

  print("\nNeptune's volume is ",neptune.getVolume()," mi^3")

  print("\nEarth's mass is ",earth.getMass(), " pounds")
  print("\nNow let's change earth's mass to 30 pounds.")
  earth.setMass(30)
  print("\nEarth's mass is now ",earth.getMass())

  print("\nLet's remove Naiad from the list of Neptune's moons ")
  neptune.removeMoon("Naiad")
  print("\nNow Neptune has ",neptune.getNumMoons(), " moons")

main()
  
