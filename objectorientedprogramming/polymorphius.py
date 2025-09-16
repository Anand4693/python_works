"""
Polymorhius

 definition: more than one form (many forms)

1) method_overloading
   within same class same method_name different number of parameters

3) method_overriding """



class Calculator:

    def add(self,num1,num2):

        print(num1+num2)

    def add(self,num1,num2,num3):

        print(num1+num2+num3)

    def add(self,num1,num2,num3,num4):

        print(num1+num2+num3+num4)

calc_instance = Calculator()

calc_instance.add(100,200,300,400)

class Operations:

    def add(self,*args):

        print(sum(args))

operation_instance = Operations()
operation_instance.add(10,20)
operation_instance.add(10,20,30)
operation_instance.add(10,20,30,40)



# (*args*,*kwargs*)

def add_numbers(*args):

    # *args take any numner of parameters as tuple

    print(sum(args))

add_numbers(10,20,30)


"""
Topics Covered

features and application
datatypes
operators
decisionmaking
looping
function and lambda function, recursion(pending)
collection properties and methods
    *list
    *tuple
    *dictionary
    *set
nested collections

String and string methods

File operations

opps
    >class,object
    >constructor(__init__)
    >magic methods(__str__)
    >inheritance(single,mutlilevel,multiple)
    >polumorphism(method overloading,method overriding)
    >obstraction
    >super and self

*args and **kwargs
decorator functions
error handling
error handling
modules and packages

______________________________________________________________

Topics to be covered

Database
Django
DRF
Javascript
react
"""