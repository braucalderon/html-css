inp = raw_input('Enter Hours')
hours = float(inp)
inp = raw_input('Enter Rate')
rate = float(inp)
print rate, hours
if hours <= 40 :
    pay = rate * hours
else :
    pay = rate * 40 + (rate * 1.50 * (hours - 40))
print pay