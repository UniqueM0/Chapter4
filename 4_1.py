


# def get_number():
#     return 5

# def set_number(num):
#     number = num
#     print("From set_number, num is:", str(num))
#     return number 

# num = get_number()
# set_number(6)

# print("End of program. Num is:", str(num))


# def add_number(num1, num2):
#     print("num1: ", str(num1))
#     print("num2: ", str(num2))
#     val = num1 + num2
#     print("from add_number, val is: ", str(val))

# output = add_number(5,2)

# print("Output of {} is {}.".format(str(2), str(5), output))


# def get_firstname(full_name):
#     space = full_name.index(" ")
#     first_name = full_name[:space]
#     return first_name

# my_name = get_firstname("Unique B")

# print("Hello, my name is " + my_name + ".")

# def get_firstname(full_name):
#     my_name = get_firstname(name)

# names =[
#     "John Doe"
#     "James Brown"
#     "Mike Lowe"
#     "Jose Lopez"
#     "Tom Brady"
#     "Mike Tyson"]

# for name in names:
#     my_name = get_firstname(name)
#     if name == "Tom":
#         print(my_name + "plays football!" )
#     elif my_name == "Colby":
#         print(my_name + "plays basketball")
#     elif my_name == "Mike":
#         print(my_name + "is into boxing")
#     else:
#         print(my_name + "is not into sports")



# def pay(wage, hours):
#     if hours<= 40:
#         amount = wage * hours
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#     return amount

# hourly_wage = eval(input("Enter the hourly wage: "))
# hours_worked = eval(input("Enter the number of hours worked: "))
# print("Earnings: ${0:,.2f}".format(pay(hourly_wage, hours_worked)))




# def pay(wage, hours):
#     amount = 0
#     if hours <= 40:
#         print("Here!")
#         amount = wage + hours
#     else:
#         amount = (wage * 40) + ((1.5) * wage * (hours - 40))
#         return amount
    
# wage = eval(input("Enter the hourly wages: "))
# hours = eval(input("Enter the numbers of the hours worked: "))

# result = pay(wage, hours)
# print("Earnings: ${0:,.2f}".format(result))





# def is_Vowel_Word(word):
#     word = word.upper()
#     vowels = ('A', 'E', 'I', 'O', 'U')
#     for vowel in vowels:
#     #     if vowel not in word:
#     #         return False
#     # return True
#         vowel in word



# word = input("Enter a word: ")
# if is_Vowel_Word(word):
#     print(word, "contains every vowel.")
# else:
#     print(word, "does not contain every vowel.")

#or

# test_word = "Education"

# # if is_Vowel_Word(test_word):
# #     print(test_word, "contains every vowel.")
# # else:
# #     print(test_word, "does not contain every vowel")


# word = input("Enter a word: ")

# if is_Vowel_Word(word):
#     print(word, "contains vowel.")
# else:
#     print(word, "does not contain vowel")




def main():

    x = 2
    print(str(x) + ": function main")
    trivial()
    print(str(x) + ": function main")

def trivial():
    x = 3 
    print(str(x) + ": function trivial")

main()