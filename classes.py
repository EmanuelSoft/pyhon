#class name of the first letter always  to be capital ...
#and also class names are separated by it's first capital letter elements
class Point:
    def move(self):
        print("go")
    def stop(self):
        print("stop")

point1= Point()
point1.x=10
print(point1.x)
point1.move()  
'''constractor'''      
class Point:
    def __init__(self,x,y):
     self.x=x
     self.y=y
    def Pint(self,a,b):
        return a * b
    def move(self):
        print("go")
    def stop(self):
        print("stop")

point1= Point(10,20)
print(point1.Pint(23,3))
point1.move()
print(point1.y)
'''inheritance'''
class Mammal:
    def __init__(self,name):
        self.name=name
    def walk(self):
        print(f"{self.name} can walk")
class Dog(Mammal):
     pass
class Cat(Mammal):
    def walk(self):
        print("like tigger")        

dog=Dog("dog")
dog.walk()