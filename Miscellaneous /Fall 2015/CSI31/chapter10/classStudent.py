class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

   # aStudent = Student ('Adam, Henry', 127, 228)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQpoints(self): 
        return self.qpoints

    # These methods will allow to get information back out of a student

    # print (aStudent.getName())

    def gpa(self):
        return self.qpoints/self.hours

    
def makeStudent(infoStr):
        # infoStr is a tab-separated line: name hours qpoints
        # returns a correspondhing Student object
    name, hours, qpoints = infoStr.split("\t") # ('\t') is gonna NOT split the info in parts. 
    return Student(name, hours, qpoints)

def main():

    # open the input file for reading
    filename = input("Enter name the grade file: ")
    infile = open(filename, 'r')

    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())

    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember ir.
        if s.gpa() > best.gpa():
            best = s

    infile.close()

    # print information about the best student
    print('The best student is: ', best.getName())
    print('hours:' , best.getHours())
    print('GPA:', best.gpa())

if __name__ == '__main__':
    main()
    
    
