class Shapes(object):  
    def __init__(self, name, sides):  
        self.name=name
        self.sides=sides
   

class Circle(Shapes):  
    def __init__(self, name= "Circle", sides=1):  
        super().__init__()
        self.name=name
        self.sides=sides
        self.radius=radius
    def Details(self):
        print("name:",self.name)
        print("sides:",self.sides)
        print("radius:",self.radius)

class Rectangle(Shapes):
    def __init__(self, name= "Rectangle", sides=4, longside= 2, shortside= 1):
        Shapes.__init__(self, name, sides)
        self.name=name
        self.sides=sides
        self.longside=longside
        self.shortside= shortside
    def Details (self):
        print("name:",self.name)
        print("sides:",self.sides)
        print("long side:",self.longside)
        print("short side:",self.shortside)

class Square(Shapes):
    def __init__(self, name= "Square", sides=4, side=5):
        Shapes.__init__(self, name, sides)
        self.name=name
        self.sides=sides
        self.side=side
    def Details (self):
        print("name:",self.name)
        print("sides:",self.sides)
        print("side:",self.side)

class Ellipse(Shapes):
    def __init__(self, name="Ellipse", sides=1, longradius=4, shortradius=3):
        Shapes.__init__(self, name, sides)
        self.name=name
        self.sides=sides
        self.longradius=longradius
        self.shortradius= shortradius
    def Details(self):
        print("name:",self.name)
        print("sides:",self.sides)
        print("longradius:",self.longradius)
        print("shortradius:",self.shortradius)





        
