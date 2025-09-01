class Animal:

    name:str

    sound:str

    def set_animal(self,name,sound):

        self.name = name
        
        self.sound = sound
    
    def animal_sound(self):

        print(self.name,"===",self.sound)

    
animal_instance = Animal()

animal_instance.set_animal("lion","roar")

animal_instance2 = Animal()

animal_instance2.set_animal("cat","meow")

