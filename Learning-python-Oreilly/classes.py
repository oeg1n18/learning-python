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

# self is used to reference the instance of the class.

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

#============================== Larger Class ========================================

class Person: 
    def __init__(self, name, job=None, pay=0): #constructor takes three arguments
        self.name = name # Fill out fields when created
        self.job = job #self is the new instance object
        self.pay = pay
""" self is the newly created instance object, and name, job, and pay become state information
descriptive data saved on an object for later used. 'job' is a local variable in the scope of 
the __init__ function, but self.job is an atribute of the instance that's the implied subject
 of the method call. They are two different variables """

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay=1000000)
print(bob.name, bob.pay)
print(sue.name, sue.pay)

""" say we want to import this module into another but do not want any of the output statements
we can do this doing the following method. As once imported the __name__ is no longer '__main__'"""

if __name__=='__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=1000000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

