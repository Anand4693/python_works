
class Shape:

    def __init__(self,name,edge_count):

        self.name = name
        
        self.edge_count = edge_count

    def calculate_are(self):

        print(f"calculating{self.name} area")


class Square(Shape):

    def __init__(self,name,edge_count,s):

        super().__init__(name,edge_count)

        self.s = s

    def calculate_are(self):

        a=self.s**2

        print(f"area of {self.name} is {a}")

class Rectangle(Shape):

    def __init__(self,name,edge_count,b,h):

        super().__init__(name,edge_count)

        self.b = b

        self.h = h

    def calculate_are(self):
        
        a = self.b * self.h

        print(f"area of{self.name} is {a}")



Square.instance1 = Square("SQAURE",4,8)

