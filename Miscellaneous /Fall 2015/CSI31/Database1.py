#BCC Database

from math import*

class Database:

    def __init__(self, fname):
        self.List = []
        self.fname = fname
        infile = open(fname, "r")
        for line in infile:
            b = line.strip('\n').split(',') # = ['reyes'= 0, ' ben'= 1, ' student', ' male', ' hispanic', ' 26', ' 5']
##            print(b[0])#Last
##            print(b[1])#First
##            print(b[2])#Status
##            print(b[3])#Gender
##            print(b[4])#Race
##            print(b[5])#Age
##            print(b[6])#Years
            self.List.append(b)
        print(self.List)

    def listor(self,fname):
        for i in self.List:
            if i[0] == fname:
                print("Found!")
                return
            
            if i[1] == fname:
                print('F')
                return
            
            if [2] == fname:
                print('F')
                return        
    
            if [3] == fname:
                print ('F')
                return        
    
            if [4] == fname:
                print ('F')
                return
                    
            if [5] == fname:
                print ('F')
                return

            if [6] == fname:
                print ('F')
                return
            
            else:
                print ('Does not exist!!')
                return 
        
   
        

class Person():
    
    def __init__(self):
        self.database = Database()

    def listor(self):
        self.database.listor()

    def listand(self):
        self.database.listand()
    

        





def main():
    print_intro()

    stats = Database('myfile.txt')
    stats.listor('black')
    info = Person(listor,listand)

    for i in n:
        if i == info:
            pass
            
        
        

def print_intro():
    print("Welcome to the BCC Database")

def getInputs():
    f = input("Please enter the file name, for example 'myfile.txt': ")
    n = input("Enter any of the following information, name, last name, age, or department to : ")

def getOutput():
    
        
main()


