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


# str = '2' + '4'
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
    text = words.lower().split()
    return text[0][0] == text[1][0]

print(check_first_word_char("shiva Srasad"))





# return True if sum of two integers is equal to 20 or if any one integer is 20 
# and return False if above does not follow
def check_twenty(num1, num2):
    if num1 + num2 == 20 or num1 == 20 or num2 == 20:
        return True
    else:
        return False
print(check_twenty(12, 80))





# Level 1 problems
# display like this= Ex: old_macdonald('macdonald') --> MacDonald
def old_macdonald(word):
    return word[:3].capitalize() + word[3:].capitalize()
    
print(old_macdonald('macdonald'))





# reverse the words 
# ex: master_yoda('i am home') --> 'home am i'
def master_yoda(words):
    splitted_words = words.split()
    result = ''
    for word in splitted_words[::-1]:
        result = result + word + ' '
    return result
print(master_yoda('i am home'))




# we can use .join() also with list
def master_yoda(words):
    splitted_words = words.split()
    reversed_words = splitted_words[::-1]
    return ' '.join(reversed_words)
print(master_yoda('i am home'))




# check whether the given number is within 10 
# when subtracting with either 100 or 200
# Using abs() function 
# abs():  used to give us a postive number instead of negative sign
# ex: abs(100-120) = 20 not -20

def check_number(number):
    return abs(100 - number) <=10 or abs(200 - number) <= 10

print(check_number(110))
print(check_number(10))
print(check_number(200))





# Level 2 Problems
# check whether an array contains 3 and 3 side by side or not 
# Ex: has_33([1,2,3,3]) = True
# has_33([1,3,2,3]) = False
# has_33([3,2,1,3]) = False
num_list = [1,3,4,5,3,3]
def has_33(num_list):
    for num in range(len(num_list)-1):
        if num_list[num] == 3 and num_list[num + 1] == 3:
            return "it has 3 & 3"
    return " it does not have 3 & 3"
print(has_33(num_list))       




# print every character 3 times instead of single time
# Ex: paper_doll("Hello")  --->  'HHHeeellllllooo'
# name = "hello"
# result = ''
# for char in name:
#     result = result + char * 3
# print(result)
    

def paper_doll(word):
    result = ''
    for char in word:
        result = result + char * 3
    return result

print(paper_doll("Hello"))
print(paper_doll("Mississippi"))




# Blackjack problem
# if their sum is <= 21 then return their sum
# if their sum is >21 and there is 11 number in among three numbers then reduce their sum by 10
# if their sum is >21 and it does not contain any 11 number then return by "BUST"
def blackjack(numbers):
    if len(numbers) < 4:
        total_sum = sum(numbers)
        # print(total_sum)
        # to check whether a number is in a list or tuple or string we use "in"
        if total_sum >21 and 11 in numbers:
            result = total_sum - 10
            return result
        elif total_sum <=21:
            return total_sum
        else:
            return "BUST"
    else:
        return "Error: Required 3 numbers, but given 4 numbers"

blackjack_numbers = (5, 6, 7)
blackjack_numbers = (9, 9, 9)
blackjack_numbers = (9, 9, 11)
print(blackjack(blackjack_numbers))





# summer_69 
# return sum() of numbers when it does not have any 6 to 9 numbers
# if numbers are from 6 to 9 then sum remaining numbers
# if 6 and 9 are side by side then sum remaining numbers
# if a list contains 6 and 9 but not side by side then sum all the numbers
# 6 and 9 cannot be together if yes then sum remaining numbers
# if list have [1,2,6,7,8,9, 10] then sum remaining numbers 1 + 2 + 10 = 13
# if list have 6 to 9 not in side by side
# [1,2,6,3,9,8,4,7] sum all numbers 1+2+6+3+9+8+4+7

# list_num = [1,2,3,4,5,6,9,6,7,8,9]
# for num in range(len(list_num)-1):
#     if list_num[num] == 6 and list_num[num+1] == 9:
#         result = sum(list_num)
#     print(result)


arr = [4, 5, 6, 7, 8 ,9]
def summer_69(arr_list):
    total = 0
    add = True
    for num in arr_list:
        while add:
            if num != 6:
                total = total + num
                break
            else:
                add = False
        while add == False:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69(arr))





# Challenging problems
# spy problem
# check whether list contains 007 or not 
# the numbers to be in order 007 return True
# if it has 007 but the order is 700 then return False
# ex: [1,2,4,0,0,7,5] = order = 007 = True
# [1,0,2,4,0,5,7] = order = 007 = True
# [1,7,2,0,4,5,0] = order = 700 = False
spy_list1 = [1,2,4,0,0,7,5]
spy_list2 = [1,0,2,4,0,5,7]
spy_list3 = [1,7,2,0,4,5,0]
def spy_game(spy_game_list):
    spy_number = ''
    for num in spy_game_list:
        if num == 0 or num == 7:
            spy_number = spy_number + str(num)
    # print(spy_number)
    if spy_number == '007':
        return True
    else:
        return False
print("spy_list1: ",spy_game(spy_list1))



# Another Method 
# if we add one more number between that 0 or 7 
# it does nt give correct answer spy_list1 = [1,2,4,0,0,0,7,5]
# so we use this method
spy_list1_new = [1,2,4,0,0,0,7,5]
def spy_game(nums_list):
    check_spy = [0, 0, 7, 'x']
    for num in nums_list:
        if num == check_spy[0]:
            check_spy.pop(0)
    return len(check_spy) == 1

print("spy_list1_new: ",spy_game(spy_list1_new))





# Count primes
def count_primes(number):
    primes_list = []
    for num in range(2, number+1):
        if num < 2:
            return "please enter number 2 or greater number"
        else:
            primes_list.append(num)
    return primes_list
print(count_primes(2))






# Lambda Expressions Map and filter 
def square(number):
    return number ** 2

# lets take a list of numbers to square them 
my_num_list = [1,2,3,4,5]
result = []
for num in my_num_list:
    result.append(square(num))
print(result)



# but we can do this without using the for loop also 
# we do this using map() func
# we convert the map() to a list or tuple or set to see the output
power_num = map(square,my_num_list)
# print(list(power_num))  # or
# print(tuple(power_num))   # or
print(set(power_num))


# we can use in single line
power_num = list(map(square, my_num_list))
print(power_num)





# display the "even" if the no of characters are even in a word
# and if character are odd then print the first character of word
def check_even_word(words):
    if len(words) %2 == 0:
        return "EVEN"
    else:
        return words[0]

words_list = ["Shiva", "Hari", "Ram"]
even_words = list(map(check_even_word, words_list))
print(even_words)


# we can use for loop to do this
result = []
for word in words_list:
    result.append(check_even_word(word))
print(result)




def multiple_2(num):
    return num * 2

numbers_2 = [1,2,3,4,5,6,7,8]

print(list(map(multiple_2, numbers_2)))

result = []
for num in numbers_2:
    result.append(multiple_2(num))
print(result)



strings = ["shiva", "prasad", "hari", "raj"]

def even_word(words):
    if len(words) %2== 0:
        return "EVEN"
    else:
        return words[0].capitalize()

print(list(map(even_word, strings)))






# filter() func
# it display the iterables according to the condition that a function have
# in our case condition is checking even numbers
def check_even(num):
    return num %2 == 0

even_list = [1,2,3,4,5,6]

print("filter func even:",list(filter(check_even, even_list)))
# when we use the same with map func it returns boolean value 
print("map func even:",list(map(check_even, even_list)))



def check_odd(num):
    return num %2 == 1

odd_list = [1,2,3,4,5,6]
print("filter func odd:",list(filter(check_odd, odd_list)))
# when we use the same with map func it returns boolean value 
print("filter func odd:",list(map(check_odd, odd_list)))






# Lambda Expressions
# lambda functions are single use functions
# when a function is used only once we do this using lambda
# code can be one liners
# map(), filter(), sorted() are used with lambda
# lets take square func 
def square(num):
    return num ** 2

print(square(3))



# so previously we used map(), filter() func by creating a seperate def functions 
# instead we can use lambda to do this 
# we want to print even_words 
even_words_list = ["Ram", "Hari", "Dinesh", "Shiva"]
even_word_result = list(filter(lambda char: len(char) %2 == 0, even_words_list))
print(even_word_result)


# lets see another example: power of 4
numbers = [1,2,3,4,5,6,7]

result = list(map(lambda num: num ** 4, numbers))
print(result)

# print only odd number powers in set format
# to get this o/p we need to use both map and filter functions
result = set(filter(lambda num: num %2 == 1, numbers))

# now we combine this with map() to implement the logic
result = list(map(lambda num: num ** 4, filter(lambda num: num %2 == 1, numbers)))
print("Power 4 of odd numbers: ",result)




# Lets reverse the words using map() and order by asc using sorted()
list_of_words = ["Ram", "Hari", "Dinesh", "Shiva", "abcde", "prqs"]
reverse_list = list(sorted(map(lambda char: char[::-1], list_of_words),reverse= True))
# reversed the characters and ascending order
print(reverse_list)
# reversed the characters and descending order
reverse_list = list(sorted(map(lambda char: char[::-1], list_of_words),reverse= True))
print(reverse_list)




# lets try this in traditional way
def reverse_words_sort(words):
    result_list = []
    for word in words:
        result_list.append(word[::-1])
    return sorted(result_list, reverse=True)

print(reverse_words_sort(list_of_words))


# using map with def function
def reverse_word_with_map(words):
    return words[::-1]

reverse_map_result = list(map(reverse_word_with_map, list_of_words))
print("reverse_map_result DEFAULT:",reverse_map_result)
# sort in asc
reverse_map_result = list(sorted(map(reverse_word_with_map, list_of_words)))
print("reverse_map_result ASC ORDER:",reverse_map_result)
# sort in desc
reverse_map_result = list(sorted(map(reverse_word_with_map, list_of_words), reverse=True))
print("reverse_map_result DESC ORDER:",reverse_map_result)






# Nested Statements and Scopes
# scope of variables where it can be accessed 
x = 25
def printer():
    x = 50
    return x

print(x)    # o/p: 25

print(printer())    # o/p: 50


# LEGB RULE:
# LEGB = Local, Enclosing, Global, Built-in
# Local
# lambda num: num ** 2



# GLOBAL SCOPE name
name = "THIS IS A GLOBAL FUNC"
def greet():
    # ENCLOSING SCOPE name
    name = "I AM ENCLOSING SCOPE"
    def hello_name():
        # LOCAL SCOPE
        print("Hello", name)
    hello_name()
greet()     # o/p: hello name


# if we comment out the enclosing scope variable then
# then it takes the global scope variable
# GLOBAL SCOPE name
name = "THIS IS A GLOBAL FUNC"
def greet():
    # ENCLOSING SCOPE name
    # name = "I AM ENCLOSING SCOPE"
    def hello_name():
        # LOCAL SCOPE
        print("Hello", name)
    hello_name()
greet()     # o/p: hello THIS IS A GLOBAL FUNC




# Lets add local scope variable 
name = "THIS IS A GLOBAL FUNC"
def greet():
    # ENCLOSING SCOPE name
    name = "I AM ENCLOSING SCOPE"
    def hello_name():
        # LOCAL SCOPE
        name = "I AM LOCAL SCOPE"
        print("Hello", name)
    hello_name()
greet()     # o/p: hello I AM LOCAL SCOPE






# Methods and Funtions problems
# write a func to find the volume of sphere by giving the radius 
def volume_sphere(rad):
    return 4/3 * 3.14 * rad ** 3

print(volume_sphere(2))




# write a func check a number is in given range or not inclusive high and low
# Ex: range_check(5, 2, 7)
# o/p: 5 is in range of 2 and 7
def range_check(num, low, high):
    if num in range(low, high+1):
        return f"{num} is in range between {low} and {high}"
    else:
        return f"{num} is NOT in range between {low} and {high}"

# print(range_check(5, 2, 7))
print(range_check(7, 2, 7))



# print only the boolean values 
def range_check_bool(num,low,high):
    return num in range(low, high)

print(range_check_bool(3,1,10))






# Find the no.of upper case characters and no.of lower case characters in a string 
# Expected o/p: No.of Upper Case characters: 4
# Expected o/p: No.of Lower Case characters: 33
sample_str = "Hello Mr. Rogers, how are you this is Tuesday?"
def count_upper_lower(words):
    upper_char_count = ''
    lower_char_count = ''   
    for char in words:
        if char.isupper():
            upper_char_count += char
        elif char.islower():
            lower_char_count += char 
        else:
            pass
    return f"No.of Upper Case characters: {len(upper_char_count)}\nNo.of Lower Case characters: {len(lower_char_count)}"

print(count_upper_lower(sample_str))






# write a func that takes a list of numbers and returns a new list with unique elements of first list
sample_list = [1,1,1,1,2,2,3,3,3,3,4,5]
def unique_list(list_num):
    return list(set(list_num))

new_list = unique_list(sample_list)
print(new_list)



# lets try this without using set 
def unique_list(list_num):
    seen_numbers = []
    for num in list_num:
        if num not in seen_numbers:
            seen_numbers.append(num)
    return seen_numbers

print(unique_list(sample_list))




# write a func to multiply all the numbers in a list
sam_list = [1,2,3,-4]
def multiply(num_list):
    total = 1
    for num in num_list:
        total = total * num 
    return total

print(multiply(sam_list))





# write a func to check palindrome or not 
# racecar 
pal_word = "race car"
pal_word = "nu rs es ru n"
def palindrome(word):
    removed_space_word = word.replace(' ','')
    return removed_space_word[::-1] == removed_space_word

print(f"{pal_word}: ",palindrome(pal_word))






# check a sentence is pangram or not
sentence_str = "The quick brown fox jumps over the lazy dog"
import string

# print(string.ascii_lowercase) = abcdefghijklmnopqrstuvwxyz
def ispangram(sentence, alphabet = string.ascii_lowercase):
    # converting it to set 
    alphabet_set = set(alphabet)
    # removing spaces from given sentence
    removed_spaces = sentence.replace(' ', '')
    # converting it to lowecase
    lower_case_sentence = removed_spaces.lower()
    # converting to set
    lower_case_sentence_set = set(lower_case_sentence)
    # comparing both sets
    return alphabet_set == lower_case_sentence_set


print(ispangram(sentence_str))




#####################################
# CHECK TIC TAC TOE PROJECT - 1
#####################################






# OOPS CONCEPTS STARTS HERE
# Attributes and class keywords
# class Sample():
#     pass

# my_sample = Sample()
# print(my_sample)



# lets create  attributes in a class
# whenever the and object is created it also have these attributes
# class Dog():
#     """the attributes are breed: string, name: string, color: string"""
#     def __init__(self, breed, name, color):  # these are parameters
#         self.breed = breed      # these ara attributes like self.breed is a attribute
#         self.name = name
#         self.color = color
    
# my_dog = Dog("lab", "tommy", "brown")
# print(my_dog.breed, my_dog.name, my_dog.color)





# lets create methods in a class

place = "hyd"   # we can use this variable without using self inside a class 
class Dog():
    """the attributes are breed: string, name: string, color: string"""

    # class attribute: it is also called when an obj is created we are using this outside the __init__ initializer 
    # since it is outside the __init__ the value will be same for all the obj created with class
    # so the dog_owner will be same for all the dogs it will be static value for all the obj created
    # we use self.dog_owner to display the value because it is inside the class so we use self 
    dog_owner = "shiva"     # class attribute


    # Instance Attributes:
    # these act as a dynamic value every obj will have different values we can assign them 
    def __init__(self, breed, name, color):  # these are parameters
        # so basically we add attributes inside this to make it accessible to all the methods inside the class
        # we use __init__ it is called as a constructor or initializer it is automatically called when obj is created using this class
        # we use self to make attributes accessible to all the methods inside the class
        self.breed = breed      # these ara attributes like self.breed is a attribute
        self.name = name
        self.color = color

    
    # we create methods same like we create function with def keyword but 
    # since we are inside the func so we use parameter self 
    # and we call this as methods 
    # def bark(self):
    #     print("bow bow")

    # we can add parameters also to this method
    def bark(self, walks):
        # here we did not used self.walks because this parameter is only accessible to this method only we cannot use this parameter to other methods thats why we donot use self.walks
        print(f"bow bow, i walked {walks}km.")  # here we are not using the self.walks because we already in used 
        # we can also use attributes inside the method
        # so basically we use self for the attributes and for methods if they assigned any parameters then we use it without self
        print(f"bow bow, i walked {walks}km and my name is {self.name} and my owner is {self.dog_owner}")  # here we are not using the self.walks because we already assigned in method and we used self.name because it is outside the method

        # we can directly use global variable inside the class without self keyword
        print(f"bow bow, i walked {walks}km and my name is {self.name} and my owner is {self.dog_owner} living in {place}")  # here we are not using the self.walks because we already assigned in method and we used self.name because it is outside the method

    
my_dog = Dog("lab", "tommy", "brown")
print(my_dog.breed, my_dog.name, my_dog.color)

my_dog.bark(walks = 2)   # it is a method so we use parenthesis to display the method




# example for class attributes
# we created two objects with different values 
my_dog1 = Dog("lab", "tom", "brown")
my_dog2 = Dog("husky", "jerry", "white")

# lets see the dog owner of these two objects 
print(my_dog1.dog_owner)
print(my_dog2.dog_owner)








# Lets create another class
class Circle():
    # class attribute
    pi = 3.14

    # adding default value to parameters if they did not enter anything it takes this value by default
    def __init__(self, radius=1):   # radius=1 means if they did not enter any value it takes as 1 instead of showing error message
        self.radius = radius

    
    def get_circumference(self):
        return self.radius * self.pi * 2


my_circle = Circle()
print(f"pi: {my_circle.pi}")
print(f"radius: {my_circle.radius}")
print(f"circumference: {my_circle.get_circumference()}")


# lets add radius value instead of taking 1
my_circle1 = Circle(20)
print(f"circumference: {my_circle1.get_circumference()}")




 


 # Inheritance
 # we are using one class methods and attributes in another class 
 # or we can use one class in another class as a parameter also that we called inheritance
 # and next we initialize the used class also in the current class
 # means we do double initialization one for current class and other is for the inherited class
 # in our case inherited class = Animal() and the current class = Cat()
 # so we are using Animal class methods and attributes in cat class
class Animal():
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an Animal")

    def eat(self):
        print("i am eating")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat Created")

my_cat = Cat()
my_cat.who_am_i()





# Polymorphism(optional)
class Lion():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " Roars"
    
my_lion = Lion("simba")
print(my_lion.speak())





# Special Methods
my_list = [1,2,3]
print(len(my_list))


class Sample():
    pass

my_sample = Sample()
# print(len(my_sample))



class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

my_book = Book("jungle book", "shiva", 300)
# if we print the my_book it displays the object instead of showing the data
print(my_book)  


# so we use special method called __str__
# this will print the result in str format
class Book1():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, no of pages: {self.pages}"


my_book1 = Book1("jungle book", "shiva", 300)
# now if we print this it will show the data
print(my_book1)


# lets use some built in function len()
# but it displays as obj
# print(len(my_book1))

# so to display the len() of the class we use special method called __len__
class Book2():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, no of pages: {self.pages}"

    def __len__(self):
        return self.pages

my_book2 = Book2("jungle book", "shiva", 300)
# now if we print this it will show the data
print(my_book2)
# now we try to print the len() of the book
print(len(my_book2))



# we can use __del__ special method to delete variable
class Book2():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, no of pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        return "object has been deleted"

my_book2 = Book2("jungle book", "shiva", 300)
# now if we print this it will show the data
print(my_book2)
# lets delete the variable
del(my_book2)





# OOPS Problems
# find the distance and the slope of line using coordinates 
# distance formula = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# slope formula = (y2 - y1)/ (x2 - x1)
class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1  # (x1, y1)
        self.coor2 = coor2  # (x2, y2)
    
    def distance(self):
        return ((self.coor2[0] - self.coor1[0]) ** 2 + (self.coor2[1] - self.coor1[1]) ** 2) ** 0.5

    def slope(self):
        return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])

coordinate1 = (3, 2)
coordinate2 = (8, 10)

my_line = Line(coordinate1, coordinate2)
# lets find the distance of the line
print(my_line.distance())

# lets find the slope of the line
print(my_line.slope())





# Find volume and surface_area of cylinder
# pi = 3.14
# volume of cylinder formula = pi r **2 h
# surface area = 2pi*r(r+h)
class Cylinder():
    def __init__(self, radius=1, height_cyl=1):
        self.radius = radius
        self.height_cyl = height_cyl
    
    def volume(self):
        return 3.14 * (self.radius ** 2) * self.height_cyl

    def surface_area(self):
        return 2 * 3.14 * self.radius * (self.radius + self.height_cyl)

my_cylinder = Cylinder(3, 2)
# lets find the volume 
print(my_cylinder.volume())
# lets find the surface area
print(my_cylinder.surface_area())




# Challenge problems
class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        amt_deposit = amount
        self.balance = self.balance + amount
        return f"Amt Deposit: {amt_deposit}, Avl Bal: {self.balance}"

    def withdraw(self, amount):
        amt_withdraw = amount
        if self.balance < amt_withdraw:
            return "sorry not enough funds"
        else:
            self.balance = self.balance - amount
            return f"Amt Withdrawn: {amt_withdraw}, Avl Bal: {self.balance}"

    # user = int(input("Deposit or Withdraw?(0/1): "))
    # if user == 0:
    #     deposit()
    # else:
    #     withdraw()


my_acc = BankAccount("shiva", 100)
print(f"Avl Bal: {my_acc.balance}")

# lets deposit some amount
# amount_after_deposit = my_acc.deposit(500)
print(my_acc.deposit(500))

# lets withdraw some amount
# amount_after_withdraw = my_acc.withdraw(300)
print(my_acc.withdraw(250))

print(f"Avl Bal: {my_acc.balance}")

# print(my_acc.withdraw(400))





# Modules and packages
# using pipy with pip install to install any package from internet
# lets import our newly created file code using import
from my_module import my_func

my_func()   # this will show the code in my_module file



# now to create a package and use it 
# so a folder to be called as a package when it have the __init__.py
# if a folder is having this file we call it package
# lets import the main package and sub package that we have created in the python-revision folder
# from myMainPackage import my_package_script

# my_package_script.my_script()

# from myMainPackage.mySubPackage import my_subpackage_script
# my_subpackage_script.sub_script()




# __name__ and __main__
# if __name__ == "__main__":
# __name__ is a built in variable like a built in function






# Errors and Exception Handling 
# these are used mainly for error handling, when we want to proceed execution even an error occurs 
# example:
# without try, except
# add_num = 10 + '10'
# if add_num == type(int):
#     print(add_num)
# else:
#     print("please assign proper values")


# with try, except
try:
    add_numbers = 10 + '10'
    print(add_numbers)
except:
    print("please enter correctly i am except block")



# we use three keywords for this try, except, finally
# try: 
def add_fun(n1, n2):
    return n1 + n2

print(add_fun(2, 3))

number1 = 10
# number2 = input("enter a number: ")
# print(add_fun(number1, number2))


try:
    result = 10 + 10
except:
    print("please enter numbers")

print("Result from try block: ",result)


# lets add some error like add str with int
try:
    result = 10 + '10'
except:
    print("please enter numbers")

# print("Result from try block: ",result)



# lets do with else
try:
    result = 10 + 10
except:
    print("Error: please enter numbers")
else:
    print("you dont have any errors ")




# lets use finally 
# this is always show even if there is any error or not
try:
    f = open("testfile", 'w')
    f.write("i am writing a new line using try block")
except TypeError:
    print("file not there")
except:
    print("i am errors")
finally:
    f.close()
    print("file is closed")





# example
# def ask_for_int():
#     while True:
#         try:
#             result = int(input("enter a number: "))
#         except:
#             print("thats not a number")
#             continue
#         else:
#             print("thank you")
#             break
#         finally:
#             print("i always run")

# ask_for_int()






# problems
# print('a' * 10)
c_list = ['a',8,'c']
# for char in c_list:
#     print(char ** 2)    # we can multiply but we cannot do the power

# lets handle the exception
for char in c_list:
    try:
        char == int(char)
        print(char ** 2)
    except:
        print("please enter a number list")





# problem: divisible by zero
x = 5
y = 0

try:
    z = x/y
    print(z)
except ZeroDivisionError:
    print("denominator cannot be zero")
finally:
    print("all done")





# problem:  write a func to print square of a number using while loop using try, except finally 
def square_num():
    while True:
        try:
            n = int(input("enter a number: "))
        except:
            print("try again, please enter a number")
            continue
        else:
            break
    print("square number is:",n ** 2)

square_num()






# Unit Testing
# we have several testing tools but we will focus on two
# pylint and unittest
# 1. pylint: it is a library used to check focust reporting possible issues
# 2. unittest: is a built in library used to test our own code and checking whether we are getting desired outputs
# so lets install pylint library
# cmd: pip install pylint
a = 1
b = 2
print(a)
# print(B)
# now lets test this file using the cmd: pylint and the filename
# cmd: pylint test1.py


# lets test a func
def my_func():
    first = 1
    second = 2
    print(first)
    print(second)

my_func()




# Unit testing
# we install library using cmd: pip install unittest
# def cap_let(text):
#     return text.title()     # capitalize first letter of every word

import unittest
import cap_letter


class TextCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap_letter.cap_let(text)
        self.assertEqual(result, 'Python')

    def test_mutltiple_word(self):
        text = 'hello python'
        result = cap_letter.cap_let(text)
        self.assertEqual(result, 'Hello Python')

if __name__ == '__main__':
    unittest.main()








# Project - 2
# card - game 
