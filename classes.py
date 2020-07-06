#================ class =====================
class FirstClass:
    def setdata(self, value):
        self.data = value ## self is the instance
    def display(self):
        print(self.data)

""" Class objects provide default behaviour and serve as factories ofr instance objects. 
Instance objects are the real objects your programs process -- each is a name-space in its
own right, but inherits names in the class from which it was created. Class objects come from 
statements, and instances come from calls; each time you call a class, you get a new instance
of that class

Assignmetns to attributes of self in methods make per-instance attributes. insude a class's 
method functions, the first argument (called self by convention) reference the instance
 object being processed; assignmentst to attributes of self create or change data 
 in the instance, not the class."""

x = FirstClass()
y = FirstClass()
x.setdata("King Arthur")
y.setdata("3.1459")
x.display() #prints king arthur
y.display() #prints 3.1459

class SecondClass(FirstClass): #inherts setdata from first class
    def display(self):    # Re-defines display
        print('Curnt value = "%s"' % self.data)

z = SecondClass()
z.setdata(42)
z.display() # finds overridden method in Second Class 

# Classes are attributes in modules e.g. if you have a class in a module you want to import 
# 'from modulename import classname' now you can accesss the imported class as if it where 
# written in the working module.

class ThirdClass(SecondClass): # inherit form second class
    def __init__(self, value): # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other): # on self + other
        return ThirdClass(self.data + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data
    def mul(self, other): #In-place change: named
        self.data *= other

a = ThirdClass('abc') #__init__ called
a.display() #inherited method called
print(a) #__str__:returns display string

b = a + 'xyz' #__add__: makes a new instance
b.display() # b has all ThirClass methods. prints Current value = "abcxyz"
print(b) #[ThirdClass: abcxyz]

a.mul(3) # mul:changes instance in place
print(a) #returns mul: changes instance in place