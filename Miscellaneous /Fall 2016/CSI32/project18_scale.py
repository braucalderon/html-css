from cs1graphics import *
#from file import *

def readData():
    """ reads data values from file and returns the list of tupples """
    while True:
        filename = input('Please, input the filename:')
        try:
            fname = open(filename)
            break
        except IOError:
            print('Cannot open the file. Try again, please')

    listLines = fname.readlines()
    print('read from file:', listLines)

    fname.close()
    print('File is closed')

    n=len(listLines)
    data=[]
    
    for i in range(n):
        pair=listLines[i].split()
        print(pair)
        data.append((int(pair[0]),int(pair[1])))

    print(data)
    return data


def display(data,paper):
    """ draws the rectangular coordinate system and
    displays all the points provided by data variable"""
    n=len(data) # getting number of points

    #minX,minY,maxX,maxY=0,0,0,0
    #for i in range(n):
    #    if data[i][0] > maxX:
    #        maxX=data[i][0]
    #    if data[i][0] < minX:
    #        minX=data[i][0]
    #    if data[i][1] > maxY:
    #        maxY=data[i][1]
    #    if data[i][1] < minY:
    #        minY=data[i][1]

    #print('MinX = %d, MaxX = %d, MinY = %d, and MaxY = %d'%(minX,maxX,minY,maxY))

    

    xAxis=Path(Point(0,300),Point(700,300)) # creating x-axis
    yAxis=Path(Point(350,0),Point(350,600)) # creating y-axis

    paper.add(xAxis) # drawing x-axis
    paper.add(yAxis) # drawing y-axis

    #xscale=round(700.0/(abs(maxX)+abs(minX)))
    #yscale=round(600.0/(abs(maxX)+abs(minX)))

    #print(xscale, yscale)

    # for x-coordinate: x*scale + 350
    # for y-coordinate: -y*scale + 300

    for i in range(n):
        print("x coordinate:",data[i][0]+350) 
        print("y coordinate:",(-1)*data[i][1]+300)
        point = Point(data[i][0]+350,(-1)*data[i][1]+300)
        p = Circle(1,point) # creating a circle with r=1 for the point
        paper.add(p) # display it

def findRegression(data):
    """ finds the equation of the regression line """
    n=len(data)

    sumxy=0
    sumx=0
    sumy=0
    sumx2=0
    sumy2=0

    for i in range(n):
        sumxy += data[i][0]*data[i][1]
        sumx += data[i][0]
        sumx2 += data[i][0]**2
        sumy += data[i][1]
        #sumy2 += data[i][1]**2

    print('sum_x=%d, sum_y=%d, sum_xy=%d, sum_x^2=%d'%(sumx,sumy,sumxy,sumx2))
    
    m = (n*sumxy-sumx*sumy)/float(n*sumx2 - sumx**2)
    m = round(m,2)
    print('m=',m)

    b =(sumy-m*sumx)/float(n)
    b = round(b,2)
    print('b=',b)

    print("Regression line equation: y = ",m,"x + ",b)

    return m,b

def draw_reg(m,b,paper):
    """ draws the regression line """
    x1=-100
    y1=x1*m+b
    point=Point(x1+350,(-1)*y1+300)
    print('x1=%f, y1=%f'%(x1,y1))
    print('x1_=%f, y1_=%f'%(x1+350,(-1)*y1+300))

    x2=100
    y2=x2*m+b
    point2=Point(x2+350,(-1)*y2+300)
    print('x2=%f, y2=%f'%(x2,y2))
    print('x2_=%f, y2_=%f'%(x2+350,(-1)*y2+300))

    regline=Path(point,point2)
    paper.add(regline)

def dispEq(m,b,paper):
    """ displays the equation """
    text='y='+str(m)+'x + ' + str(b)
    t=Text(text,12)
    t.move(100,550)
    paper.add(t)
    

def main():

    # read data from the input file
    data=readData()

    paper=Canvas(700,600,'light yellow','Regression Line')

    # display data on the screen
    display(data,paper)
    
    # find regression
    m,b=findRegression(data)

    # draw regression line
    draw_reg(m,b,paper)

    # display the equation of the regression line
    dispEq(m,b,paper)

main()


    
