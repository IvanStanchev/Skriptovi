class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other_obj):
        return str(self.age) + other_obj.name

    def __sub__(self, other_obj):
        return self.age - other_obj.age

    def __mul__(self, other_obj):
        return self.age * other_obj.age

    def __truediv__(self, other_obj):
        return self.age / other_obj.age


p = Person("Alex", 15)
p1 = Person("Pesho", 10)
h=(input("+ or - or * or /\n"))
if h=="+":
    a=p+p1
if h=="-":
    a=p-p1
if h=="*":
    a=p*p1
if h=="/":
    a=p/p1
    
if type(a)==str:
    p2=Person(a,int(input("How old is the person: ")))
else:
    p2=Person((input("Name of the person: ")),a)

    

    