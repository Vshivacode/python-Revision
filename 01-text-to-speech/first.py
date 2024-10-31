print("hello world")

# modules: module is a file containing the code that is written 
# by someone else like some functions that performs something

# pip: is used to install the modules
# examples flask, django, pyjokes
# now we installed the flask and pyjokes

# now we import the modules by using keyword "import"
import pyjokes

# we can use the .get_joke() to print the jokes everytime we run 
joke = pyjokes.get_joke()
print(joke)



