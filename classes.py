# Object-oriented programming(OOP):think about the world in terms of objects Were object may store information and data
# inside of them,And also support the ability to perform type of operations,Like [actions,methods,or functions]
# that can operate in those objects.
# The [actions,methods,or functions]: Objects procedures (often known as methods) like [__init__].
# Class : a template of a type of object
# Point():The type of the new class of your own making it is called[The object],so you must define it to make it work
# __init__:It's a function that automatically called Every time I'm trying to create a new object [new point].
# All [actions,methods,or functions] like __init__  that operate in object them self are going
# to take the first argument self like   def __init__(self, ,): but if __init__ not under the class Point(): you can
# use it without self and that is applecable to  all the [actions,methods,or functions]
# Self:Represent the object so [self=Point] self =Refrancing  the object that i'm dealing with and allow
# us to store and  assign any value or multible values That might change depending on which
# point We happened to be interacting with at any given time.
#  (self,input1,input2) represent the point itself,becose the point needs to inputs and if it need 3inputs you can do it
#  it depends on how you what the object or the oint to work

class Point () :

    def __init__(self, input1, input2):
#self is representing the pint and we need allw the point to store it's own x,and y values
# You need to assign the the tow inpot spaces of the point[(self, input1, input2):] to be
# able to store values inside the self
# you can call input1, input2 ,p ,and  Point  what ever you want the importent thing is to assign them into x,and y
        self.x = input1
        self.y = input2
#[p = Point(2, 8)]If you want to create a new point and that is the penfit of  __init__


p = Point(2, 8)
#(p.x): means go into the point and access the data x that is inside that point
print(p.x)
print(p.y)

