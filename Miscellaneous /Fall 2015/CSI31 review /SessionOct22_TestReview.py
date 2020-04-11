Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Test Review
>>> 9 % 4
1
>>> 12 % 4
0
>>> 9 / 4
2.25
>>> 9 // 4
2
>>> "34" + "10"
'3410'
>>> S = "BCC Math"
>>> S[2]
'C'
>>> S[3]
' '
>>> S[2:6]
'C Ma'
>>> S[2:]
'C Math'
>>> S[:2]
'BC'
>>> k = -5
>>> if k > 0:
    print(k)
elif k < -5:
    print(k*2)
elif k == -4.9:
    print(k+2)
else:
    print(k - 1)

    
-6
>>> for k in range(2,6):
    print(k+5)

    
7
8
9
10
>>> for k in [2,1,9]:
    print(k**2)

    
4
1
81
>>> k = 2
>>> for ch in "Hi Kid":
    k = k + 2

    
>>> k
14
>>> test_val = 10;
while test_val > 2:
    print(test_val)
    test_val = test_val - 2;
print("done")
SyntaxError: multiple statements found while compiling a single statement
>>> test_val = 10
>>> while test_val > 2:
    print(test_val)
    test_val = test_val - 2

    
10
8
6
4
>>> print("done")
done
>>> test_val = 10
while test_val > 2:
    print(test_val)
    test_val = test_val - 2
    print("done")
    
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> test_val = 10
>>> while test_val > 2:
    print(test_val)
    test_val = test_val - 2
    print("done")

    
10
done
8
done
6
done
4
done
>>> test_val = 10
>>> while test_val < 2:
    print(test_val)
    test_val = test_val - 2

    
>>> test_val
10
>>> A = 9
>>> B = 100
>>> A, B = B, A
>>> A
100
>>> B
9
>>> def average(a,b,c,d,e):
    avg = (a + b + c + d + e) / 5
    return avg

>>> average(1,2,1,2,1)
1.4
>>> L, W = eval(input("Lenght and Width? "))
Lenght and Width? 3,5
>>> print("Area is: ", L*W)
Area is:  15
>>> L, W = eval(input("Lenght and Width? "))
Lenght and Width? 4,-9
>>> if L <= 0 or W <=0:
    print("Not valid dimensions!")
else:
    print("Area is: ", L*W)

    
Not valid dimensions!
>>> def shapes():
    import graphics
    from graphics import *
    win = GraphWin("Practice6",100,100)
    win.setCoords(0,0,10,10)
    Cr = Circle(Point(5,5),4)
    Cr.draw(win)
    Rt = Rectangle(Point(5,5),Point(6,7))
    Rt.draw(win)
    
SyntaxError: import * only allowed at module level
>>> def NumEven(n):
    count = 0
    for k in range(n):
        if k % 2 == 0:
            count = count + 1
    
    return count

>>> NumEven(9)
5
>>> def NumEven(n):
    count = 0
    for k in range(1,n):
        if k % 2 == 0:
            count = count + 1
    
    return count

>>> NumEvn(9)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    NumEvn(9)
NameError: name 'NumEvn' is not defined
>>> NumEven(9)
4
>>> NumEven(8)
3
>>> NumEven(1)
0
>>> 
