import time
game = True
def intro(): 
    print ("Welcome to Diya's Area/Volume calculator")
    print ('This calculator will calculate the area/volume of 2D and 3D shapes')
    print ('Before we begin, these are some parameters this calculator will follow') # These are the common vaules and terms used in the program
    print (' 1. pi = 3.14 \n 2. Radius = r \n 3. Base = b \n 4. Height = h \n 5. Lenght = l \n 6. Height = h \n 7. Side x = x \n 8. Side y = y \n 9. 1/3 = 0.333 \n 10. 4/3 = 1.333')
    print ()

    time.sleep(2) 

    print ('-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-')

    print ("Let's Begin! ")
    print ('Below is the list of shapes you can select from:' ) #The shape selection / Menu
    print (" 1. Circle \n 2. Triangle \n 3. Trapezoid \n 4. Rectangle \n 5. Square \n 6. Cylinder \n 7. Pyramind \n 8. Sphere \n 9. Rectangular Prism \n 10. Cube ")

def using():
    usershape = input("Enter your selection: ")
    usershape = int (usershape) 

    if usershape == 1:
        print ("Input the radius")
        r = input()
        r = int(r)

    if usershape == 2:
        print ( "Input the base and height")
        b = input()
        h = input()
        b = int(b)
        h = int(h)

    if usershape == 3:
        print ( "Input the Side x, Side y, and height")
        x = input()
        y = input()
        h = input()
        h = int(h)
        x = int(x)
        y = int(y)
    if usershape == 4:
        print ( "Input the lenght and width")
        l = input()
        w = input()
        l=int(l)
        w=int(w)

    if usershape == 5:
        print ( "Input the lenght ")
        l = input()
        l = int(l)

    if usershape == 6:
        print ( "Input the radius and height ")
        r = input()
        h = input()
        r = int(r)
        h = int (h)
    if usershape == 7:
        print ( "Input the base and height")
        b = input()
        h = input()
        b = int(b)
        h = int(h)

    if usershape == 8:
        print ( "Input the radius")
        r = input()
        r = int(r)


    if usershape == 9:
        print ( "Input the lenght, width, and height")
        l = input()
        w = input()
        h = input()
        l = int(l)
        h = int(h)
        w = int(w)

    if usershape == 10:
        print ( "Input the lenght ")
        l = input()
        l= int(l)


    def circle (r):
        result = 3.14 * r * r 
        result = str (result)
        print ("Result: " + result)

    def triangle (b,h):
        result = 0.5 * b* h 
        result = str (result)
        print ("Result: " + result)

    def trapezoid (x,y,h):
        value = x + y
        result = 0.5 * value *h 
        result = str (result)
        print ("Result: " + result)

    def rectangle (l,w):
        result = l * w
        result = str (result)
        print ("Result: " + result)

    def square (l):
        result = l * l
        result = str (result)
        print ("Result: " + result)

    def cylinder (r,h):
        result = 3.14 * r * r * h
        result = str (result)
        print ("Result: " + result)

    def pyramid (b,h):
        result = 0.333 * b * h
        result = str (result)
        print ("Result: " + result)

    def sphere (r):
        result = 1.333 * 3.14 * r * r
        result = str (result)
        print ("Result: " + result)

    def reactangularprism (l,w,h):
        result = l * w * h
        result = str (result)
        print ("Result: " + result)

    def cube (l):
        result = l * l * l 
        result = str (result)
        print ("Result: " + result)

    if usershape == 1:
        circle(r)

    if usershape == 2:
        triangle(b,h)

    if usershape == 3:
        trapezoid(x,y,h)

    if usershape == 4:
        rectangle(l,w)
        
    if usershape == 5:
        square(l)

    if usershape == 6:
        cylinder(r,h)

    if usershape == 7:
        pyramid(b,h)

    if usershape == 8:
        sphere(r)

    if usershape == 9:
        reactangularprism(l,w,h)

    if usershape == 10:
        cube(l)

def playagain(): 
    print('Do you want to continue?')
    print('Answer yes or no:')
    answer = input().lower()
    if answer == "no":
        exit()

while (game == True): 
    intro()
    using()
    playagain() 