try:
    inp = raw_input('enter hours:')
    hours = float(inp)
    inp = raw_input('enter rate:')
    rate = float(inp)
    
except:
    print "Error, please enter numeric input"
    quit()

#print rate, hours
if hours <= 40 :
        pay = rate * hours
else :
        pay = rate * 40 + (rate * 1.5 * (hours-40))
print pay
