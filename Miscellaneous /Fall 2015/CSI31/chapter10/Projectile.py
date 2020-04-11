from math import sin, cos, radians

class Projectile:
    """Simulates the flight of  simple projectiles near the earth's surface,
ignoring with resistance. Tracjking is done in two dimensions, height (y) and
distance (x)."""

    def __init__ (self, angle, velocity, height):
        """Create a projectile with given launch angle, initial
velocity and height."""

        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
farther into its flight"""

        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

    def getY(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def getX(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos

def getInputs():
    a = eval(input("Enter the launch angle (in degress): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position: "))
    return a,v, h, t

def main():
    angle, vad, hO, time = getInputs()
    cball = Projectile (angle, vad, hO)
    while cball.getY() >= 0:
        cball.update(time)
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getY()))
main()       
