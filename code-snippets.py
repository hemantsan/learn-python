# name = input("Enter your name : ")
# age = input("Your age : ")
# print("Hello " + name + ", Your are is : " + age)

# friends = ["Kevin", "Karen", "Tim", "Crap", "Meh", "Tim"]
# friends.reverse()
# print(friends)

# coordinates = (4, 5)
# print(coordinates)

# def sayHi(name): print("Hi " + name)
# sayHi("Hemant")
#
# def cube(num):
#     return num*num*num
#
# print(cube(8))

# is_male = False
# is_tall = False
#
# if is_male and not(is_tall):
#     print('You are a male.')
# elif not(is_male) and is_tall:
#     print("You are tall boi")
# else:
#     print("You are female")

# def max_num(num1, num2):
#     if num1 > num2:
#         return "Num1 is big"
#     elif num1 < num2:
#         return "Num2 is big"
#     else:
#         return "Same number"
#
# print(max_num(1,1))
#
# num1 = float(input("Enter one number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "*":
#     print(num1 * num2)

# monthConversion = {
#     "jan": "January",
#     "feb": "February",
#     "mar": "March",
# }
#
# print(monthConversion.get("janu",  "Not a valid key"))


# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with while loop")

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("guess the correct word: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("You are out of guesses, YOU LOST")
# else:
#     print("YOU WIN!!")

# friends = ["Tim", "Dim", "Harry"]
# for friend in friends:
#     print(friend)
#
# for index in range(len(friends)):
#     print(friends[index])

# def raise_to_power(base_num, pow):
#     result = 1
#     for index in range(pow):
#         result = result * base_num
#     return result
#
# print(raise_to_power(5, 10))

# number_grid = [
#     [1, 2, 3],
#     [5, 7, 8],
#     [59, 63, 45],
#     [20, 30],
# ]
#
# for row in number_grid:
#     for r in row:
#         print(r)

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation
#
# print(translate(input("Enter a phrase: ")))

# try:
#     # value = 10 / 0
#     num = int(input("Enter a nubmer: "))
#     print(num)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError as err:
#     print(err)

from Student import Student

st = Student("Hemant", "Business", 5.2, False)
print(st.name)
print(st.gpa)
print(st.major)
print(st.is_on_probation)


