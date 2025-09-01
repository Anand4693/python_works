# Movies (titel,director,language,year)

class Movie:

    def __init__(self,title,director,language,year):
        
        self.title = title

        self.director = director

        self.language = language

        self.year = year

    def display_movie(self):

        print(self.title,self.director,self.language,self.year)

    def __str__(self):
        
        return self.title

movie_instance1 = Movie("F1","Goddy","english",2025)

movie_instance1.display_movie()

print(movie_instance1)