# Multilevel Inheritance


class GrandParent:

    def house(self):

        print("grand parent House")

class Parent(GrandParent):

        def car(self):

            print("parent swift car")

class Child(Parent):

    def bike(self):

        print("child bike method")

child_instance = Child()

child_instance.bike()

child_instance.car()

child_instance.house()


