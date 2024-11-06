# Displaying the information
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

# row2[1] = 'X'


# def user_input():
#     while True:
#         user = input("select the row you want to add (row1/row2/row3) OR Enter exit to exit the game: ")
#         if user == "exit":
#             break
#         if user == 'row1':
#             select_index_value = input("select the index value you want to add(0/1/2): ")
#             if select_index_value == '0':
#                 row1[0] = "X"
#             elif select_index_value == '1':
#                 row1[1] = "X"
#             elif select_index_value == '2':
#                 row1[2] = "X"
#             else:
#                 return "please select 0 or 1 or 2"
#             display(row1, row2, row3)
#         elif user == 'row2':
#             select_index_value = input("select the index value you want to add(0/1/2): ")
#             if select_index_value == '0':
#                 row2[0] = "X"
#             elif select_index_value == '1':
#                 row2[1] = "X"
#             elif select_index_value == '2':
#                 row2[2] = "X"
#             else:
#                 return "please select 0 or 1 or 2"
#             display(row1, row2, row3)
#         elif user == 'row3':
#             select_index_value = input("select the index value you want to add(0/1/2): ")
#             if select_index_value == '0':
#                 row3[0] = "X"
#             elif select_index_value == '1':
#                 row3[1] = "X"
#             elif select_index_value == '2':
#                 row3[2] = "X"
#             else:
#                 return "please select 0 or 1 or 2"
#             display(row1, row2, row3)
#         else:
#             print("please select row1 or row2 or row3")

#         play_again = input("would you like to continue playing y or n: ").lower()
#         if play_again == "n":
#             break
#         else:
#             continue
# user_input()



# def user_choice():

#     user = range(1, 10)
#     choice = '100'
#     while choice.isdigit() == False or user == False:
#         choice = input("Enter a number(1-9): ")
#         if choice.isdigit() == False:
#             "please enter number (1, 10)"
#         elif choice >=10:
#             "return False"
#     return choice
# print(user_choice())

def user_choice():
    choice = 'wrong'
    while choice.isdigit() == False or range(1, 10) == False:
        choice = input("enter number between(1-9): ")
        if choice.isdigit() and int(choice) in range(1, 10):
            return choice
        elif choice.isdigit() == True and int(choice) not in range(1, 10):
            return "please enter number b/w 1 to 9"
        else:
            return "sorry, that is not a number, please enter a number b/w 1 to 9"

print(user_choice())



