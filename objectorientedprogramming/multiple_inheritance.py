
class Father:

    def cricket_skills(self):

        print("father cricket skills")

class Mother:

    def cooking_skills(self):

        print("mother cooking skills")

class Child(Mother,Father):

    def learning_skills(self):

        print("child learning skills")

child_instance = Child()

child_instance.learning_skills()

child_instance.cooking_skills()