# a = int(2)
# print(type(a))
# shiva = str("shiva")
# print(shiva)

# ls = [1,2, 'shiva', "234iusdfsf"]
# # print(ls)
# ls = [5]
# print(ls)

# set_1 = {1, 1, 1, 2, 3, 5, 5, 9, 10}
# print(set_1)

# dict_1 = {
#     "name": "shiva",
#     "age": 25,
# }

# print(dict_1)


# tup = (1,3,4)
# # tup[0] = 20
# # print(tup)

# ls = [1,2,3,4,5]
# ls[0] = 20
# print(ls)


# shiva = True
# print(type(shiva))




# a = 2
# print("a: ", a)

# a = 5
# print("a: ", a)

# c = a + a
# print(c)


# name = "shiva prasad a human being"
# print(name[2 : 15 : 2])

# address = 'i am "shiva" i"ll \nhave a coke'
# print(len(address))


b = """iamshiva'prasaddeveloper"""
# print(b[::2])


name = "shiva is a learning python"

# print(name)

name1 = "prasad"

result = name[:5] + " " + name1 + " " + name[5:]
# print(result)


str = '2' + '4'
# print(str)

# print(result.capitalize())



# print(result.split('i'))  # it removes the "i" and split them as a item in list




# string formatting
name = "shiva"
# print(name * 10)

# print("hello world")


# print("i am shiva a {} and learning {}".format("developer", "python"))

# print("i am shiva a {1} and learning {0}".format("developer", "python"))


# print("i am shiva a {dev} and learning {lang}".format(dev="developer", lang="python"))


# float formatting = value:width.precisionf
# precision = no.of decimals you want to display

age = 38432.99102
# print("lion is the {k} and age is {a:1.2f}".format(k="king", a=age))
# here a is value and width is 1 white space and 2 is no of decimals and f 




# string literals 
# print(f"my name is {name}")




# lists
list1 = [23,34,3,543,6,56,45758,58]
# print(list1)

# print(list1[2])


list2 = [
    1,24,234.533, 
    (2343, "shiv"), 
    {"name":"shiva", "lang": "python"},
    ["shiva", "prasad", 2314]
    ]

# print(list2[3])


list2[4]["age"] = 25
# print(list2)


# print(list1 + list2)


list1.append("shiva")
# print(list1)

list1.pop(0)
# print(list1)


list3 = [234,3254,36,5,42,34,34654,7,68,6,2,124,23]
list3.sort()
# print(list3)

list4 = ["2", "sda", "abc","@#$%"]
list4.sort()
# print(list4)


list3.reverse()
# print(list3)



# dictionaries
my_dict = {"name": "shiva", "age": 25}
# print(my_dict)

dict1 = {
    "name": "shiva",
    "age": [1,2,3,5,6,7,8,9],
    "address": {"colony": "colony 1", "street": "road no 1"}
}

# print(dict1)
# print(dict1["address"]["colony"])

dict1["name"] = "new value"
# print(dict1)
dict1.pop("name")






set1 = {2,45,2,2,5,2,6,4,6,5}
# print(set1)

# lets add one value to a set
set1.add("shiva")
# print(set1)




# user = input("enter your name: ")
# print(user)



# file_name = open('C:/Users/shiva/Downloads/python-Revision/python-udemy-course/myfile.txt')


# print(file_name.read())

# this will print only first line and we can print specific characters in the first line also
# print(file_name.readline())
# print only 10 characters of first line
# print(file_name.readline(10))



# readlines() this will print all the lines in a list format and each line is divided into an item in the list
# print(file_name.readlines())



# file_name.close()
# once it is closed we cant read the file
# print(file_name.read())





# we can perform open and close at same time 
with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt") as file_name_oc:
    # text_file = file_name_oc.read()
    readline_file = file_name_oc.readline()
    readlines_file = file_name_oc.readlines()

# # print("text-file: ",text_file)
# print("readline: ",readline_file)
# print("readlines: ", readlines_file)




# with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt", mode='r') as file_modes:
#     mode_r = file_modes.read()

# print("read mode: ",mode_r)



with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt", mode='r') as file_modes:
    print("write mode: ", file_modes.read())

with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt", mode='a') as file_modes:
    file_modes.write("i am appending a new line")

with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt", mode='r') as file_modes:
    print("write mode: ", file_modes.read())

with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt", mode='w') as file_modes:
    file_modes.write("i am new line using write mode")

with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/python-topics/myfile.txt", mode='r') as file_modes:
    print("write mode: ", file_modes.read())


with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/test.txt", mode='w') as new_file:
    new_file.write("i am a new test file")

with open("C:/Users/shiva/Downloads/python-Revision/python-udemy-course/test.txt", mode='r') as new_file:
    print(new_file.read())




ls = [0]
ls.append(0)
ls.append(0)
# print(ls)


ls1 = [0]
ls2 = [0]
ls3 = [0]
# print(ls1 + ls2 + ls3)






ls4 = [1,2,4,35,4,64,2,2,3,32,2,23,2]
unq_set = set(ls4)
# print(unq_set)


# print(0 == 0)






# statements
# if some condition:
#     execute this 
# elif some condition:
#     do this 
# else:
#     do this 

# if True:
#     print("it is true")


hungry = True

if hungry:
    print("it is true")


not_hungry = False

if not_hungry:   # it does go inside, because it only goes when the condition is true
    print("not hungry")




# lets combine both of them if true then this works and if false then this works 
if not_hungry:
    print("it is False")
else:
    print("it is True")


# lets use elif
phone = 'vivo'
if phone == "iphone":
    print("iphone is good")
elif phone == "vivo":
    print("vivo phone camera is good")
else:
    print("i dont have a phone")





# for loops with lists
mylist = [1,3,3.5,92,943,3,1,432,52,9]
for item in mylist:
    print(item)


for num in mylist:
    if num == 3:
        print("number is 3")
    elif num == 9:
        print("number is 9")
    else:
        print(num)




# finding even and odd numbers
for num in mylist:
    if num %2 == 0:
        print(f'even: {num}')
    elif num %2 == 1:
        print(f'odd: {num}')
    else:
        print(f'floating number: {num}')




# adding all the numbers in the list
add = 0
for num in mylist:
    add = add + num    
    # print(add)
print(add)



# for loops with strings
name = "shiva, hello world"
for char in name:
    print(char)


# if you dont want to use the item then we can simply use the underscore
for _ in name:
    print("loop is running")



# for loop with tuples
mytup = (2, "shiva", 93,29, "prasad", [2,3,4,2,1])
for tup in mytup:
    print(tup)



tup_list = [(1,2), (2,3), (3,4), (4,5)]

for a,b in tup_list:
    print(a)
    print(b)


tup_list1 = [(1,2,3), (2,3,4), (3,4,5), (4,5,6)]

for a,b,c in tup_list1:
    print(a,c)




# for loops with dictionaries
loop_dict = {"name": "shiva", "age": 25}

for key in loop_dict.keys():
    print(key)

for value in loop_dict.values():
    print(value)

for items in loop_dict.items():
    print(items)






# while loops: it goes inside the loop when it condition is True
# while some condition:
#     do something
# else:
#     do something

pool = 10

while pool < 15:
    print(f"pool: {pool} ")
    pool = pool + 1


pool = 50
while pool < 20:
    print(f"pool: {pool}")
else:
    print("50 is not less than 20")





# break, continue, pass
# break
my_num = 10 
while my_num < 20:
    print(f" {my_num} is less than {my_num}")
    break
else:
    print(f"{my_num} is not less than {my_num}")



# pass
# for item in something:
#     pass #do nothing
a = [1,2,3]

for num in a:
    pass



# continue
my_name = "shiva prasad"
for name in my_name:
    if name == "a":
        continue
    print(name)



# remove the whitespaces from this 
sent = "my name is shiva, learning python udemy course"
result = ""
for item in sent:
    if item == " ":
        continue
    print()
    result = result + item
print(result)





# using break
result = ""
for item in sent:
    if item == "r":
        break
    result = result + item
print(result)





# operators
# range()
for num in range(2,20, 3):
    print(num)


# using range() with print data structures list, tuple, set
print(list(range(0, 20)))
print(tuple(range(0, 20)))
print(set(range(0, 20)))






# Enumerate
# it displays the index value and the value of an iterator in tuple format
fname = "shiva prasad"
for item in enumerate(fname):
    print(item)




# zip
l1 = [1,2,3]
l2 = [2,3,4]
l3 = [3,4,5]
list_combine = l1 + l2 + l3
for item in list_combine:
    print(item)


for item in zip(l1, l2, l3):
    print(item)



# but if we have different no of items in each list then it ignores the other itmes
list_1 = [1,2,3,8,9,0]
list_2 = [2,3,4,45]
list_3 = [3,4,5,85,34,89]

for item in zip(list_1,list_2,list_3):
    print(f"New list: {item}")


# we can conver them into a list or any other data structure also
print(list(zip(list_1, list_2, list_3)))




# in keyword
check_name = "shiva prasad"
print("d" in check_name)    # o/p: True


# we can use with dictionaries also 
check_dict = {"name": "shiva", "age": 25, "a": "alphabet"}
print(25 in check_dict.values())
print("name" in check_dict.keys())
print("shiva" in check_dict.keys())
print("shiva" in check_dict.values())




# min() and max()
num_list = [1,3,4,5,2,3,53,4,3,6,456]
print(min(num_list))
print(max(num_list))




# random library importing shuffle function: it will shuffle the items
# it only works in lists
from random import shuffle

shuffle(num_list)
print(num_list)






# importing randint() from random library
from random import randint
print(randint(0,2)) 



# input()
# fullname = input("enter your full name: ")
# print(fullname)

# age = input("enter your age: ")
# print(age)
# print(type(age))    # string

# lets convert this to a int
# age = int(age)
# print(type(age))





# List Comprehensions
# lets use a normal for loop with list
str_a = "hello shiva"

list_a = []
for item in str_a:
    list_a.append(item)
print(list_a)


# we can do this by using list comprehension
list_a = [ item for item in str_a]
print(list_a)


range_list = [num for num in range(0,11)]
print(range_list)


#lets print only even or odd numbers
even = [num for num in range(0,11) if num%2==0]
print(even)


odd = [num for num in range(0,11) if num %2 == 1]
print(odd)




# Nested loops
xy_list = []
for x in [1,2,3]:
    for y in [2,3,4]:
        xy_list.append(x*y)

print(xy_list)




# Questions 
# display the words that starts with "s"
sent = "i am shiva prasad sam sandy dinesh bharath sanju"
res = sent.split(" ")
final_list = []
for item in res:
    if item.startswith("s"):
        final_list.append(item)

print(final_list)


# or we can use indexing
r = []
for item in res:
    if item[0] == "s":
        r.append(item)
print(r)



# print all the even numbers from 0 to 10
num_res = []
for num in range(0,11):
    if num%2 == 0:
        num_res.append(num)
print(num_res)




# use list comprehension list all the numbers that are divisible by 3
div_by_3 = [num for num in range(1, 51) if num %3 == 0]
print(div_by_3)




# if the length of the words are even then print EVEN
str_final = "print every word in this sentence that has an even number of letters"
res_list = str_final.split(" ")

for word in res_list:
    if len(word) %2 == 0:
        print(word + " is EVEN")



# fizz buzz
for num in range(1, 101):
    if num %3 == 0 and num %5 == 0:
        print("Fizz Buzz")
    elif num %3 == 0:
        print("Fizz")
    elif num %5 == 0:
        print("Buzz")
    else:
        print(num)
    





# create a list take every word first letter to display as a list
sent_1 = "Create a list of the first letters of every word in this string"
sent1_list = sent_1.split(" ")
sent1_res = []
for letter in sent1_list:
    sent1_res.append(letter[0])
print(sent1_res)


# using list comprehension
sent1_list_compr = [letter[0] for letter in sent1_list]
print("Using list comprehension: ", sent1_list_compr)






# methods and functions
# .append, .pop and many more are methods
add_item = [1,2,3]
add_item.append(4)
print(add_item)


# functions
# if we want to write the same code again again is not a good idea
#  instead we can store the code in a function and we use this function many times in the code 
# we can create a function using "def <function_name>"
# example: def name_of_function():
                # some code here
def hello_name(name):
    """prints hello and user name"""
    print(f"hello {name}")
hello_name("shiva")



# using return instead of print()
# return allows to save the result in a variable
def without_return(num1, num2):
    print(num1 + num2)
without_return(2,4)


# lets do some calculation for the result of a function
def with_return(num1, num2):
    return num1 + num2

func_result = with_return(2,4)
print(func_result)




# Basic functions
def say_hello(name="Default"):
    print("hello", name)

say_hello()



def sum_numbers(num1, num2):
    return num1 + num2

result = sum_numbers("shiva", "prasad")
print(result)

result = sum_numbers(2, 4)
print(result)

result = sum_numbers('2', '4')
print(result)




# Functions with Logic
def check_even_num(num):
    return num %2 == 0

print(check_even_num(29))



# checks even numbers in the list
result = []
def check_even_num_list(num_list):
    for item in num_list:
        if item %2 == 0:
            result.append("EVEN")
        else:
            result.append("ODD")
    return result

print(check_even_num_list([1,2,3]))




# return even numbers from given list
even_numbers_list = []
def even_numbers(num_list):
    for num in num_list:
        if num %2 == 0:
            even_numbers_list.append(num)
    return even_numbers_list
print(even_numbers([1,2,3,4,5,6,7,8]))


# return odd numbers from given list
odd_numbers_list = []
def odd_numbers(num_list):
    for num in num_list:
        if num %2 == 1:
            odd_numbers_list.append(num)
    return odd_numbers_list
print(odd_numbers([1,2,3,4,5,6,7,8]))





# Functions and Tuple Unpacking
# Unpacking the tuples from a list
numbers_list = [("shiva", 24), ("prasad", 12), ("hari", 23)]
for a,b in numbers_list:
    # print(a)
    # print(b)
    print(a, b)



work_hours = [("shiva", 100), ("hari", 200), ("raj", 150)]
def best_employee(emp_list):
    max_working_hours = 0
    employee_name = ''
    for emp_name, emp_hours in emp_list:
        if emp_hours > max_working_hours:
            max_working_hours = emp_hours
            employee_name = emp_name
        else:
            pass
    return (employee_name, max_working_hours)
# print(best_employee(work_hours))
result = best_employee(work_hours)
print("Best employee with max working hours:", result)





# Interaction between functions
# lets shuffle a list using random library with shuffle()
from random import shuffle

original_list = [1,2,3,4,5,6,7,8]

def shuffle_list(num_list):
    shuffle(num_list)
    return num_list

result = shuffle_list(original_list)
print(result)



# Game: Finding the ball is in which place
ball_list = [" ", "0", " "]
shuffle(ball_list)
# print(ball_list[0])

# user_guess = int(input("enter your guess (0/1/2): "))
# for value in ball_list:
#     if ball_list[user_guess] == value and value == '0':
#         print(f"its a match: {ball_list} ")
#         break
#     else:
#         print(f"not a match: it is here {ball_list}")
#         continue



# user_guess = ' '
# while user_guess not in ['0','1','2']:
#     user_guess = input("enter your guess(0/1/2): ")




# lets create functions for above logic
# def player_guess():
#     guess = ' '
#     while guess not in ['0', '1','2']:
#         guess = input("enter your guess(0/1/2): ")
#     return int(guess)

# print(player_guess())


# def check_guess(player_guess, ball_list):
#     if ball_list[player_guess] == "0":
#         print(f"correct: {ball_list}")
#     else:
#         print(f"Wrong, it is here: {ball_list}")

# check_guess(player_guess(), ball_list)




# *args and **kwargs
# arguments and keyword arguments
def myfunc(num1, num2):
    """Returns 5% of the sum of num1 and num2"""
    return sum((num1, num2)) * 5/100

print(myfunc(40, 60))

# but if we add more values to myfunc it will throw error
# print(myfunc(40,60,10,2,20))
# we can add give more arguments but what if we dont know how many arguments we need to perform 
# we use " *args "   it takes unlimited arguments 

def func_args(*args):
    print(args)     # it returns in tuple format

func_args(1,3,4,4,5,7,8,0)  # we can give many args



# similarly we have "*kwargs"  we give arguments using keywords
def func_kwargs(**kwargs):
    print(kwargs)   # it returns in dictionary format

func_kwargs(name= "shiva")


def favorites(**kwargs):
    if 'fruit' in kwargs:
        print(f"my fav fruit is : {kwargs['fruit']}")
    else:
        print("fruit is not there")

favorites(fruit="apple", veg="dal")




# Combining *args and **kwargs
def args_kwargs(*args, **kwargs):
    print(args, kwargs)

args_kwargs(1,2,3,4,name="shiva")





# Exercise
def least_number_of_even_numbers(num1, num2):
    if num1 %2 == 0 and num2 %2 == 0:
        if num1 < num2:
            print(num1)
        else:
            print(num2)
    else:
        if num1 > num2:
            print(num1)
        else:
            print(num2) 


least_number_of_even_numbers(4,3)



# lets try with return 
def least_number_even(num1, num2):
    if num1 %2 == 0 and num2 %2 == 0:
        # even numbers
        if num1 < num2:
            return num1
        else:
            return num2
    else:
        # odd numbers
        if num1 < num2:
            return num2
        else:
            return num2

print(least_number_even(1,2))



# lets use min and max functions 
def least_number_efficient(num1, num2):
    if num1 %2 == 0 and num2 %2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)
    
print(least_number_efficient(10,9))






#  write a func that takes two strings and if the two words start with same letter then return True if not return False
def check_first_char(str1, str2):
    if str1[0] == str2[0]:
        return True
    else:
        return False

print(check_first_char("shiva", "Shambo"))
# print(check_first_char("shiva", "prasad"))


# lets do this in one string having two words
def check_first_word_char(words):
    text = words.split()
    if text[0][0] == text[1][0]:
        return True
    else:
        return False
print(check_first_word_char("shiva prasad"))
print(check_first_word_char("shiva shambo"))




# we can do this way also in efficient way
def check_first_word_char(words):
    text = words.split()
    return text[0][0] == text[1][0]

print(check_first_word_char("shiva prasad"))