from datetime import date
import math
from random import randint

# import re

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
paragraph = '''hi my name is Eoin Carrick'''

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
# and to return all the letters, we can do this with "[0:]"
# print(course[0:9])  # So here, we got "Python's."
# print(paragraph[0:])

# # /// Formatted String. ///
first = 'Eoin'
last = 'Carrick'
othersFinds = course.find('for')
msg = f'{first} [{last}] is a coder'
print(msg)
print(f'our findings: {othersFinds}')

# /// Strings Method. /// print(len(paragraph))  # the len() is used to check the total number of elements or items a string
# has, or array. 
# print(paragraph.upper())  # return a new string in upper case. 
# print(course.lower())  # return a new string in lower case.
# print(course.find('beginners'))  # the find() returns the index of a string. print('for' in
# course)  # the "in" method or keyword returns a true or false if a value can be found in a string print(
# course.replace('Python', 'JavaScript'))  # The replace() is used to replace or change a string.And it is
# case-sensitive

# A print(paragraph.title())  # the title() string a lower case typed string into an upper case string for every
# first letter


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
# unit = input('(L)lbs or (K)g: ')

# if unit.upper() == "L":
#     convert = (int(weight) / 2.205)
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
#  guess_count = 0
#  guess_limit = 3
#  rand = randint(1, 10)
#  secret_number =  rand
#  print(secret_number)
#  while guess_count < guess_limit:
#      int(input('Guess: '))
#      guess_count += 1
#      if secret_number == rand:
#          print('You Guessed Right')
#          break
#  else:
#      print('Sorry, you only guess three times.')


#  users_choices = input('''
#  start - to start the car
#  stop - to stop the car
#  quit - to exit
#  ''')
#
#  print(users_choices)
#
#  is_to_start_car = 'start'
#  is_to_stop_car = 'stop'
#  is_to_quit_car = 'quit'
#
#  while users_choices:
#      if users_choices.upper() == is_to_start_car:
#          print('The car is ready to go!')
#          break
#      elif users_choices.upper() == is_to_stop_car:
#          print('The car has stopped!')
#          break
#      elif users_choices.upper() == is_to_quit_car:
#          print('Quiting...')
#          break
#  else:
#      print('It is not working')

# print(users_input)
#
# if users_input.upper() == 'HELP':
#       print('''start - to start the car
#       stop - to stop the car
#       quit - to exit ''')
#       users_selection = input('')
#
#       if users_selection.upper() == 'START':
#           print('The car is ready to go!')
#       elif users_selection.upper() == 'STOP':
#           print('The car has stopped!')
#       else:
#           print('Quiting')

limit = 3
starting_number = 0
start_already = False
stopped_already = False

#  while True:
#      users_input = input('> ').upper()
#      if users_input == 'HELP':
#         print('''
#  start - to start the car
#  stop - to stop the car
#  quit - to exit the terminal''')
#      elif users_input == 'START':
#             if start_already:
#                 print('The car has already started!')
#             else:
#                 start_already = True
#                 print('The car is ready to go!')
#
#      elif users_input == 'STOP':
#          if stopped_already:
#              print('The car has already stopped!')
#          else:
#              stopped_already = True
#              print('The car has stopped!')
#      elif users_input == 'QUIT':
#             break
#      else:
#        print('Sorry! Unable to recognize keyword. Please check your spellings')
#        break
# 1:41:24

#  number_at_zero = 0
#
#  while number_at_zero < 10:
#      number_at_zero += 1
#      print(number_at_zero)
#

# For Loops
for every_letter in 'Eoin Carrick':
    print(every_letter)
for every_number in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(every_number)
for every_item in ['Eoin', 'Carrick', 'John', 'Bismark']:
    print(every_item)

#   range python built-in function for providing number from 0 to the required to be ranged.
#   range(10), will provide number between 0 and 10.

for numbers in range(10):
    print(numbers)

for number_intervals in range(5, 9):
    print(number_intervals)

prices = [10, 20, 30]
total = 0
for add_price in prices:
    total += add_price
    print(f'Total: {total}')

# Nested Loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

f_number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
x = 'x'
for f in f_number:
    for ff in x:
        print(ff * f)

# Lists
first_name_only = ['John Doe', 'Eoin Carrick', 'Matte Carrick', 'kiki Sarong', 'Mz Aka', 'Uncle Sarong',
                   'Emera YoYo', 'Jeff Driver', 'Sam Arranger']
taken_names = first_name_only[:]
taken_names[0] = 'Easel'

# for largest in first_name_only:
#     larger = len(largest)
#     if True:
#         print(largest)
#         print(max(larger))
#     else:
#         print('no de')


random_numbers = [1, 4, 8, 10, 34, 65, 34, 89, 23, 23, 12, 32, 43, 12, 32, 43, 12]
max_num = random_numbers[0]
print(f'max_num: {max_num}')

for number in random_numbers:
    if number > max_num:
        max_num = number
        print(max_num)
print(f'The largest number here is: {max_num}')

# for each_num in random_numbers:
#     max_number = len(max(random_numbers))
#     if len(each_num) == max_number:
#         print(each_num)


# 2D Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0] = 'Y'

print(matrix)

for row in matrix:
    for items in row:
        print(items)

# List Method or Function
number_list = [2, 4, 2,1,46,2,12,3,76,56,19,7,8,0,32,43,54,65,76,87,98,99,199,12,13,115, 76, 43, 4, 20]
print(number_list.append(1212121212121212))
# The append() method or function add an element at the end of a list


number_list.insert(1, 200)
print(number_list)
# The insert() method or function add an element at the start or middle or the end of a list
# since it takes two argument insert(index, object). So, therefore you can add any number you want
# at any place using the insert() method or function

number_list.remove(200)
print(number_list)
# The remove() method or function is used to remove an int or string from a list, and it takes in only one
# argument.

number_list.pop()
print(number_list)
# The pop() method or function removes an element or item at the ending of a list or the last value on a list.

checking_for_index = number_list.index(19, 3, 12)
print(f'checking_for_index: {checking_for_index}')
# It takes 3 parameters, the first parameter is the value of the list we are checking
# the second parameter is the "start" index, there, we tell it where to start looking for the value
# and the third parameter is the "end" index. This tell it where to end the search fot the value.
# The index() method or function is used in order to check the index, or position of a value or items in a list.
# To check if a particular value exist in a list.
# If the value is not found, it throws an error.
# When checking to see if a value exist, using the "in" will since it returns true or false.
# print('for' in course)  # the "in" method or keyword returns a true or false if a value can be found in a string or
# int

checking_for_frequency = number_list.count(2)
print(f'checking_for_frequency: {checking_for_frequency}')
# The count() method or function, counts the number of times, value or string or int appeared in a list.

number_list.sort()
print(number_list)
# The sort() method or function, re-arrange a value from lower to upper (Ascending)

number_list.reverse()
print(number_list)
# The reverse() method or function, re-arrange a value from upper to  lower (Descending)

number_list_copy = number_list.copy()
print(number_list_copy)
# The copy() method or function is used, when you want to copy a list. And it doesn't take any
# parameters.

number_list.clear()
print(number_list)
# The clear() method or function is used, when you want to clear a list of items. And it doesn't take any
# parameters.

alphabet_letters = ['q', 'e', 'd', 's', 'f', 'r', 'g', 'v', 'b', 'n', 'm', 'h', 'k', 'l', 'p', 'o', 'i', 'u', 'h', 'y',
                    'g', 't', 'v', 'b', 'n', 'm', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'd', 's',
                    'e', 'r', 't', 'y', 'u', 'h', 'v', 'c', 'd', 'z', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'i', 'u',
                    'y', 't', 'r', 'e']
unique = []
# Thi is the way to remove duplicates
for every_letter in alphabet_letters:
    if every_letter not in unique:
        unique.append(every_letter)
print(unique)

num_list = [1, 12, 3, 43, 51, 52, 3, 3]
the_max_num = num_list[0]

for x in num_list:
    if x > the_max_num:
        the_max_num = x
print(the_max_num)


# Tuple
tuple_list = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
print(tuple_list[3])

# Tuple are not re-assignable/mutable/changeable once they have been already assigned.
# eg: my_list = (1,2,3,4,5,5,6,7)
# Doing this " my_list[2] = 100" will return an error message
# Note that, it is almost the same as "my_list = [1,2,3,4,5,6,7]", but this one here, is mutable.
# And we use tuple when we know or dont want a list to be mutable in your code in the future.


# Unpacking
co_ordinate = (1,2,3)
x,y,z = co_ordinate
print(f'{x} {z} {y}')

# Dictionaries
customers = {
        'name': 'Essel Rocky',
        'age': 123
    }

# Methods Of Accessing Information or Value From A Dictionary

# 1. Using this "[ 'the_value_name' ]" The Square brackets notation
print(customers['age'])
# But using this, the value will return a error "saying it don't exist" if the value is not in the dictionary.

# 2. Using the ".get()" method
print(customers.get('age'))
#  Note on the "get()" method,
# it doesn't return a error even if the value is not in existent, but rather a None.

# Re-assigning values
reCustomers = customers['age'] = 1 # re-assigning values from the initial to final value
customers['created_at'] = date.today() # Adding another pair value here
print(reCustomers)
print(customers)

# user__input = input('Input a number > ')

# numbers_in_words = ('zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
#                  #    0      1      2       3        4      5       6       7       8         9
    
# # for every_word in numbers_in_words: 
# #  num = numbers_in_words.index(every_word)
# #  for i in user__input:
# #     if int(i) == int(num):
# #         print(f'{numbers_in_words[num]}')

# words_arr = []
# this_arr = ''

# for i in user__input:
#     for every_word in numbers_in_words:
#      num = numbers_in_words.index(every_word)
#      if int(i) == int(num):
#         this_arr = [numbers_in_words[num]]
#         print(this_arr)

# # Trying to put all the words into an array.
# # for every_single_word in this_arr:
# #  if every_single_word not in words_arr:
# #     words_arr.append(every_single_word)
# #     print(words_arr)


# message = input('> ')
# words = message.split(' ')
# emoji = {
#     ':)' : 'happy',
#     ':(': 'sad',
# }

# word_out = ''
# for word in words:
#     word_out += emoji.get(word, word) + ' '
# print(word)
# # The split method, when used like this " .split(' ') ", it return every single element as array that has space.
# # eg.  split_letter = 'a b c d e f g h i j k l m n o  p q r s t u v w x y z'
# #  split_letter.split(' ') returns ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# split_letter = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
# l = split_letter.split(' ')
# print(l)



# Function in Python

