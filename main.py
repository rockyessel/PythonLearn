import math
from random import randint
import re

# print('I am Eoin Carrick')
# print('o----')
# print(' ||||')
# print('*' * 10)
#
# # ///////// Variables //////////
#
# price = 10  # integer
# price = 20  # integer
# rating = 4.5  # float
# name = 'Eoin'  # string
# is_done = True  # boolean
#
# # we check in a patient named Eoin Carrick.
# # He's 30 years old and is a new patient
#
# patient_name = 'Eoin Carrick'  # string
# patient_age = 20  # integer
# is_new_patient = True  # boolean
# print(price)
#
# # ///////// Getting Input //////////
# user_name = input('What is your name? ')
# print('Hi ' + user_name)
#
# # Ex
# users_name = input('Name please? ')
# users_favourite_color = input('What color do you like? ')
# print(users_name + ' likes ' + users_favourite_color)

# //////// Type Conversion //////////
# users_birth_year = input('Birth year: ')
# print(type(users_birth_year))
# users_age = 2022 - int(users_birth_year)
# print(type(users_age
#            ))
# # int()
# # float()
# # bool()
# print(users_age)
#
#
# # Ex
# users_weight = input('What is your weight(lb)? ')
# kilo =float(users_weight) / 2.205
# (kg) = str(' kg')
#
# print(kilo)

# ////  Strings  ////

course = "Python's course for 'beginners'"
paragraph = '''hi
my name is Eoin Carrick'''

# we can access a single letter from a string using "[]"
# to access the first letter, we code "[1]"
# to access the second letter, we code "[2]"
# then it continues in that manner.
# Now, if we want to access the last single letter, we can count the index,
# but that will be a waste of time.
# So we use this method instead, "[-1]". this will return the last letter of a string.
# And if we want to access a RANGE of single letters, we use ":" inside the "[]"
# which will look like this "[0:9]". this will return letters from the zero(0) index to the 9th index,
# but will not return the 9th index letter.
# and to return all the letters, we can code "[0:]"
# print(course[0:9])  # So here, we got "Python's."
# print(paragraph[0:])

# # /// Formatted String. ///
first = 'Eoin'
last = 'Carrick'

msg = f'{first} [{last}] is a coder'
print(msg)

# /// Strings Method. ///
# print(len(paragraph))  # the len() is used to check the total number of letters a string has, or array.
# print(paragraph.upper())  # return a new string in upper case.
# print(course.lower())  # return a new string in lower case.
# print(course.find('beginners'))  # the find() returns the index of a string.
# print('for' in course)  # the "in" method or keyword returns a true or false if a value can be found in a string
# print(course.replace('Python', 'JavaScript'))  # The replace() is used to replace or change a string. And it is case
# sensitive

# print(paragraph.title())  # the title() string a lower case typed string into a upper case string for every first letter


# Arithmetic Operations
# print(10 ** 3)
x = 10
x = x + 3
x -= 3
x += 3
print(x)

# Operator Precedence
x = (10 + 3) * 2 ** 2
print(x)

# parenthesis ()
# exponentiation = 2 ** 3
# multiplication or division = 2 * 3 or  2 / 3
# addition or subtraction = 2 + 3 or 2 - 3

# Math Functions
x = 2.9
print(round(x))  # rounds the number to the nearest integer
x = -1932
print(abs(x))  # the abs always return a positive integer
print(math.floor(43.834))
print(math.ceil(1.8))
print(math.factorial(5))
print(math.log(10, 2))
print(math.isfinite(2332232))

# id Statements
price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')

# Logical Operators
has_high_income = True
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print('You are eligible for loan.')

if has_good_credit or has_high_income:
    print('You are still good to go!')

if has_good_credit and not has_criminal_record:
    print('SEE?')
else:
    print('Sorry! we cannot give you anything loan. Thank you')

#  or  -  one condition must be true.
#  and  -  both condition must true.
#  not  -  it turns true to false and false to true.

#  Comparison Operator

temperature = randint(9, 35)
print(temperature)
if temperature >= 30:
    print("it's a hot day")
elif temperature <= 10:
    print("it's a cold day")
else:
    print("it's neither hot nor cold")

users_name = 'Eoin Carrick'
users_name_length = len(users_name)
print(users_name_length)

if users_name_length < 3:
    print('Name must have at least 3 characters')
elif users_name_length > 50:
    print('Name can have a max of 50 characters.')
else:
    print('Name looks good 👍')

# weight = input('Weight: ')
# unit = input('(L)bs or (K)g: ')
#
# if unit.upper() == "L":
#     convert = int(weight) / 2.205
#     round_up = round(convert)
#     print(f'Your are {round_up} pounds')
# elif unit.upper() == "K":
#     convert = int(weight) * 2.205
#     round_up = round(convert)
#     print(f'You are {round_up} kg.')
# else:
#     print('sorry! Something went wrong. Check again')



#  While loop
i = 1
while i <= 10:
    print('*' * i)
    i += 1

#  Guessing Game
guess_count = 0
guess_limit = 3
rand = randint(1, 10)
secret_number =  rand
print(secret_number)
while guess_count < guess_limit:
    int(input('Guess: '))
    guess_count += 1
    if secret_number == rand:
        print('You Guessed Right')
        break
else:
    print('Sorry, you only guess three times.')


input('Start - to start the car')
input('stop - to stop the car')
input('quit - to exit')