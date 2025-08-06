

#int,float,bool,str,list,set,tuple,dictionary

# class str:
    #def capitalize()
    #def casefold()
    #def index(str) - to search the position of a str, indexing not applicable with (int,float,bool)
    #def isalpha() - To check if everythings is alphabet in a string
    #def isdigit() - To check if the string is number or not
    #def isalnum() - alphanumeric
name = "luminar"

new_name = name.capitalize() # first character capitalize
print(new_name)


name = "Luminar Technolab"

new_str = name.casefold() # lower case
print(new_str)


name = "Luminar Technolab"
#       01234567890123456
print(name.index(" in"))


name = "Luminar Technolab"
print(name.isalpha())

name = "123456"
print(name.isdigit())

name = "LuminarTechnolab1"
print(name.isalnum())