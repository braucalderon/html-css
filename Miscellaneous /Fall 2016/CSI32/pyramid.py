from cs1graphics import *

def main():

    paper_w, paper_h=600,500
    

    print('This program draws a pyramid')

    levels = eval(input('Please, input the number of levels you\'d like:'))

    if levels < 0:
        raise ValueError('Number of levels should be positive')

    elif not isinstance(levels,int):
        raise TypeError('Number of levels should be integer')

    base_w,base_h = eval(input('Please, input the dimenstions of the base level of the pyramid (w,h):'))

    if base_w < 0 or base_h < 0:
        raise ValueError('Width and height should be positive')

    elif not isinstance(base_w,int) or not isinstance(base_h,int):
        raise TypeError('Width and height should be integers')

    
    paper = Canvas(paper_w,paper_h,'white','Pyramid')

    step = int(base_w/float(levels)) # calculating the step in the width
    
    for i in range(levels):
        # each consequitive (smaller) rectangle's width is decremented by step
        level = Rectangle(base_w-i*step,base_h)
        # each consequitive (smaller) rectangle is moved to the center and above
        # the previous rectangle ,therefore dy = ...
        level.move(paper_w/2,paper_h/2 - i*base_h)
        # draw the rectangle
        paper.add(level)

main()        
        
