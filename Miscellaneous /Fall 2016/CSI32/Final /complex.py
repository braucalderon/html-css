class Complex:
    
    def __init__(self,r=0,im=0):
        self._r = r
        self._im = im
        
    def __str__(self):
        if self._r == 0 :
            return str(self._im) + 'i'
        elif self._im == 0:
            return str(self._r)
        else:
            if self._im < 0:
                return str(self._r) + str(self._im) + 'i'
            else:
                return str(self._r) + '+' + str(self._im) + 'i'
            
    def __add__(self, other):
        return Complex(self._r + other._r, self._im + other._im)
    
    def __mul__(self, other):
        a,b = self._r, self._im
        c,d = other._r, other._im
        return Complex((a*c - b*d), (a*d + b*c))
        
    def __sub__(self, other):
        return Complex(self._r - other._r, self._im - other._im)
    
    def __truediv__(self, other):
        a,b = self._r, self._im
        c,d = other._r, other._im
        return Complex((a*c + b*d)/(c**2 + d**2), (b*c - a*d) / (c**2 + d**2))
    
    def __neg__(self):
        a,b = -self._r, -self._im
        return Complex(a,b)

def main():
    m1 = Complex(-2,-5)
    m2 = Complex(3,2)
    print(m1 + m2)
    print(m1*m2)
    print(m1 - m2)
    print(m1/m2)
    print(-m1)
main()
