class NotInteresting:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.z = x + y

    def __str__(self):
        returnString = \
                     "My x: " + self.getX() + \
                     "\nMy y: " + self.getY() + \
                     "\nMy z: " + self.getZ()

        return returnString

    def getX(self):
        return str(self.x)

    def getY(self):
        return str(self.y)

    def getZ(self):
        return str(self.z)

    def changeX(self, newX):
        self.x = newX

    def changeY(self, newY):
        self.y = newY

    def changeZ(self, newZ):
        self.z = newZ

    def copy(self):
        myClone = NotInteresting(self.x, self.y)
        myClone.changeZ(self.z)
        return myClone

def main():
    A = NotInteresting(3,4)
    E = NotInteresting(1,5)
    F = NotInteresting(1,5)
    x = 100
    s = "hello there"
    L = [3,2,1]

    changeValues(A, E, F, x, s, L)

    printAll(A, E, F, x, s, L)

    print("\n ***************************** \n")
    
    changeMoreValues(A, E, F, x, s, L)

    printAll(A, E, F, x, s, L)

    print("\n ***************************** \n")


    AA = A.copy()
    print("A object: ")
    print(A)
    print("\nAA object: ")
    print(AA)    
    
    A.changeX(2015)
    AA.changeZ(3016)

    print("\nA object: ")
    print(A)
    print("\nAA object: ")
    print(AA)


def printAll(A, E, F, x, s, L):
    print("A object:")
    print(A)
    print("\nE object:")
    print(E)
    print("\nF object:")
    print(F)
    print("\nx = ", x)
    print("s = ", s)
    print("L = ", L)

def changeValues(A,B,C,x,st,theList):
    A.changeX(333)
    B.changeX(111)
    C = NotInteresting(10,50)
    x = 45
    st = "New String"
    theList[1] = 144

def changeMoreValues(a, e, f, X, S, l):
    X = e
    X.changeZ(555)
    l = [10, 20]
    changeValues(a, e, f, X, S, l)
    


