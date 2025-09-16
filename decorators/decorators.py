"""         
decorators are function that change the behaviour of another function without changing definition 

"""

#DSA

class Socialmedia:

    def __init__(self,name):

        self.name = name
    
    def add_post(self):
        # logic check is user authenticated
        print(self.name,"adding new post")

    def list_all_post(self):
        # logic check is user authenticated

        print(self.name,"listing all post")

    def add_story(self):
        # logic check is user authenticated

        print(self.name,"adding new story")



# decorators are normal function that receives function as a parameter
# there will be another wrapper function inside function

def swap_decorator(fn):

    def inner_func(n1,n2):

        if n1<n2:
            
            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    
    return inner_func

@swap_decorator
def sub(n1,n2):

    return n1-n2

@swap_decorator
def div(n1,n2):

    return n1/n2

print(sub(10,5))
print(div(10,5))

print(sub(5,10))
print(div(10,5))