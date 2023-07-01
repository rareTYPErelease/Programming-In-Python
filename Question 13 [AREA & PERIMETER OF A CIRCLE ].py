#CODE TO CALCULATE THE AREA AND PERIMETER OF A CIRCLE

def _init_(self,radius):
 self.radius=radius
 
 def area(self):#Method
 area=22/7*self.radius*self.radius
 return area
 
 def perimeter(self):#Method
 perimeter=22/7*(self.radius*2)
 return perimeter
 
circle2 =Circle(14)
circle3=Circle(28)
#object #class

print(circle2.area())
print(circle2.perimeter())

print(circle3.area())
print(circle3.perimeter())
