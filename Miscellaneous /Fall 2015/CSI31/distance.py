def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile (angle, vel, ho)
    while cball.getY() >= 0:
        cball.update(time)
    print ("\n Distance traveled: %0.1f meters. " % (cball.getX()))
    
           
