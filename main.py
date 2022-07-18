from argparse import ONE_OR_MORE
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

users_input_pair_values = input('Input a pair number e.g: 12,23,45 > ')


one_to_hundred= """zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six twenty-seven twenty-eight twenty-nine thirty thirty-one thirty-two thirty-three thirty-four thirty-five thirty-six thirty-seven thirty-eight thirty-nine forty forty-one forty-two forty-three forty-four forty-five forty-six forty-seven forty-eight forty-nine fifty fifty-one fifty-two fifty-three fifty-four fifty-five fifty-six fifty-seven fifty-eight fifty-nine sixty sixty-one sixty-two sixty-three sixty-four sixty-five sixty-six sixty-seven sixty-eight sixty-nine seventy seventy-one seventy-two seventy-three seventy-four seventy-five seventy-six seventy-seven seventy-eight seventy-nine eighty eighty-one eighty-two eighty-three eighty-four eighty-five eighty-six eighty-seven eighty-eight eighty-nine ninety ninety-one ninety-two ninety-three ninety-four ninety-five ninety-six ninety-seven ninety-eight ninety-nine one-hundred one-hundred-one one-hundred-two one-hundred-three one-hundred-four one-hundred-five one-hundred-six one-hundred-seven one-hundred-eight one-hundred-nine one-hundred-ten one-hundred-eleven one-hundred-twelve one-hundred-thirteen one-hundred-fourteen one-hundred-fifteen one-hundred-sixteen one-hundred-seventeen one-hundred-eighteen one-hundred-nineteen one-hundred-twenty one-hundred-twenty-one one-hundred-twenty-two one-hundred-twenty-three one-hundred-twenty-four one-hundred-twenty-five one-hundred-twenty-six one-hundred-twenty-seven one-hundred-twenty-eight one-hundred-twenty-nine one-hundred-thirty one-hundred-thirty-one one-hundred-thirty-two one-hundred-thirty-three one-hundred-thirty-four one-hundred-thirty-five one-hundred-thirty-six one-hundred-thirty-seven one-hundred-thirty-eight one-hundred-thirty-nine one-hundred-forty one-hundred-forty-one one-hundred-forty-two one-hundred-forty-three one-hundred-forty-four one-hundred-forty-five one-hundred-forty-six one-hundred-forty-seven one-hundred-forty-eight one-hundred-forty-nine one-hundred-fifty one-hundred-fifty-one one-hundred-fifty-two one-hundred-fifty-three one-hundred-fifty-four one-hundred-fifty-five one-hundred-fifty-six one-hundred-fifty-seven one-hundred-fifty-eight one-hundred-fifty-nine one-hundred-sixty one-hundred-sixty-one one-hundred-sixty-two one-hundred-sixty-three one-hundred-sixty-four one-hundred-sixty-five one-hundred-sixty-six one-hundred-sixty-seven one-hundred-sixty-eight one-hundred-sixty-nine one-hundred-seventy one-hundred-seventy-one one-hundred-seventy-two one-hundred-seventy-three one-hundred-seventy-four one-hundred-seventy-five one-hundred-seventy-six one-hundred-seventy-seven one-hundred-seventy-eight one-hundred-seventy-nine one-hundred-eighty one-hundred-eighty-one one-hundred-eighty-two one-hundred-eighty-three one-hundred-eighty-four one-hundred-eighty-five one-hundred-eighty-six one-hundred-eighty-seven one-hundred-eighty-eight one-hundred-eighty-nine one-hundred-ninety one-hundred-ninety-one one-hundred-ninety-two one-hundred-ninety-three one-hundred-ninety-four one-hundred-ninety-five one-hundred-ninety-six one-hundred-ninety-seven one-hundred-ninety-eight one-hundred-ninety-nine two-hundred two-hundred-one two-hundred-two two-hundred-three two-hundred-four two-hundred-five two-hundred-six two-hundred-seven two-hundred-eight two-hundred-nine two-hundred-ten two-hundred-eleven two-hundred-twelve two-hundred-thirteen two-hundred-fourteen two-hundred-fifteen two-hundred-sixteen two-hundred-seventeen two-hundred-eighteen two-hundred-nineteen two-hundred-twenty two-hundred-twenty-one two-hundred-twenty-two two-hundred-twenty-three two-hundred-twenty-four two-hundred-twenty-five two-hundred-twenty-six two-hundred-twenty-seven two-hundred-twenty-eight two-hundred-twenty-nine two-hundred-thirty two-hundred-thirty-one two-hundred-thirty-two two-hundred-thirty-three two-hundred-thirty-four two-hundred-thirty-five two-hundred-thirty-six two-hundred-thirty-seven two-hundred-thirty-eight two-hundred-thirty-nine two-hundred-forty two-hundred-forty-one two-hundred-forty-two two-hundred-forty-three two-hundred-forty-four two-hundred-forty-five two-hundred-forty-six two-hundred-forty-seven two-hundred-forty-eight two-hundred-forty-nine two-hundred-fifty two-hundred-fifty-one two-hundred-fifty-two two-hundred-fifty-three two-hundred-fifty-four two-hundred-fifty-five two-hundred-fifty-six two-hundred-fifty-seven two-hundred-fifty-eight two-hundred-fifty-nine two-hundred-sixty two-hundred-sixty-one two-hundred-sixty-two two-hundred-sixty-three two-hundred-sixty-four two-hundred-sixty-five two-hundred-sixty-six two-hundred-sixty-seven two-hundred-sixty-eight two-hundred-sixty-nine two-hundred-seventy two-hundred-seventy-one two-hundred-seventy-two two-hundred-seventy-three two-hundred-seventy-four two-hundred-seventy-five two-hundred-seventy-six two-hundred-seventy-seven two-hundred-seventy-eight two-hundred-seventy-nine two-hundred-eighty two-hundred-eighty-one two-hundred-eighty-two two-hundred-eighty-three two-hundred-eighty-four two-hundred-eighty-five two-hundred-eighty-six two-hundred-eighty-seven two-hundred-eighty-eight two-hundred-eighty-nine two-hundred-ninety two-hundred-ninety-one two-hundred-ninety-two two-hundred-ninety-three two-hundred-ninety-four two-hundred-ninety-five two-hundred-ninety-six two-hundred-ninety-seven two-hundred-ninety-eight two-hundred-ninety-nine three-hundred three-hundred-one three-hundred-two three-hundred-three three-hundred-four three-hundred-five three-hundred-six three-hundred-seven three-hundred-eight three-hundred-nine three-hundred-ten three-hundred-eleven three-hundred-twelve three-hundred-thirteen three-hundred-fourteen three-hundred-fifteen three-hundred-sixteen three-hundred-seventeen three-hundred-eighteen three-hundred-nineteen three-hundred-twenty three-hundred-twenty-one three-hundred-twenty-two three-hundred-twenty-three three-hundred-twenty-four three-hundred-twenty-five three-hundred-twenty-six three-hundred-twenty-seven three-hundred-twenty-eight three-hundred-twenty-nine three-hundred-thirty three-hundred-thirty-one three-hundred-thirty-two three-hundred-thirty-three three-hundred-thirty-four three-hundred-thirty-five three-hundred-thirty-six three-hundred-thirty-seven three-hundred-thirty-eight three-hundred-thirty-nine three-hundred-forty three-hundred-forty-one three-hundred-forty-two three-hundred-forty-three three-hundred-forty-four three-hundred-forty-five three-hundred-forty-six three-hundred-forty-seven three-hundred-forty-eight three-hundred-forty-nine three-hundred-fifty three-hundred-fifty-one three-hundred-fifty-two three-hundred-fifty-three three-hundred-fifty-four three-hundred-fifty-five three-hundred-fifty-six three-hundred-fifty-seven three-hundred-fifty-eight three-hundred-fifty-nine three-hundred-sixty three-hundred-sixty-one three-hundred-sixty-two three-hundred-sixty-three three-hundred-sixty-four three-hundred-sixty-five three-hundred-sixty-six three-hundred-sixty-seven three-hundred-sixty-eight three-hundred-sixty-nine three-hundred-seventy three-hundred-seventy-one three-hundred-seventy-two three-hundred-seventy-three three-hundred-seventy-four three-hundred-seventy-five three-hundred-seventy-six three-hundred-seventy-seven three-hundred-seventy-eight three-hundred-seventy-nine three-hundred-eighty three-hundred-eighty-one three-hundred-eighty-two three-hundred-eighty-three three-hundred-eighty-four three-hundred-eighty-five three-hundred-eighty-six three-hundred-eighty-seven three-hundred-eighty-eight three-hundred-eighty-nine three-hundred-ninety three-hundred-ninety-one three-hundred-ninety-two three-hundred-ninety-three three-hundred-ninety-four three-hundred-ninety-five three-hundred-ninety-six three-hundred-ninety-seven three-hundred-ninety-eight three-hundred-ninety-nine four-hundred four-hundred-one four-hundred-two four-hundred-three four-hundred-four four-hundred-five four-hundred-six four-hundred-seven four-hundred-eight four-hundred-nine four-hundred-ten four-hundred-eleven four-hundred-twelve four-hundred-thirteen four-hundred-fourteen four-hundred-fifteen four-hundred-sixteen four-hundred-seventeen four-hundred-eighteen four-hundred-nineteen four-hundred-twenty four-hundred-twenty-one four-hundred-twenty-two four-hundred-twenty-three four-hundred-twenty-four four-hundred-twenty-five four-hundred-twenty-six four-hundred-twenty-seven four-hundred-twenty-eight four-hundred-twenty-nine four-hundred-thirty four-hundred-thirty-one four-hundred-thirty-two four-hundred-thirty-three four-hundred-thirty-four four-hundred-thirty-five four-hundred-thirty-six four-hundred-thirty-seven four-hundred-thirty-eight four-hundred-thirty-nine four-hundred-forty four-hundred-forty-one four-hundred-forty-two four-hundred-forty-three four-hundred-forty-four four-hundred-forty-five four-hundred-forty-six four-hundred-forty-seven four-hundred-forty-eight four-hundred-forty-nine four-hundred-fifty four-hundred-fifty-one four-hundred-fifty-two four-hundred-fifty-three four-hundred-fifty-four four-hundred-fifty-five four-hundred-fifty-six four-hundred-fifty-seven four-hundred-fifty-eight four-hundred-fifty-nine four-hundred-sixty four-hundred-sixty-one four-hundred-sixty-two four-hundred-sixty-three four-hundred-sixty-four four-hundred-sixty-five four-hundred-sixty-six four-hundred-sixty-seven four-hundred-sixty-eight four-hundred-sixty-nine four-hundred-seventy four-hundred-seventy-one four-hundred-seventy-two four-hundred-seventy-three four-hundred-seventy-four four-hundred-seventy-five four-hundred-seventy-six four-hundred-seventy-seven four-hundred-seventy-eight four-hundred-seventy-nine four-hundred-eighty four-hundred-eighty-one four-hundred-eighty-two four-hundred-eighty-three four-hundred-eighty-four four-hundred-eighty-five four-hundred-eighty-six four-hundred-eighty-seven four-hundred-eighty-eight four-hundred-eighty-nine four-hundred-ninety four-hundred-ninety-one four-hundred-ninety-two four-hundred-ninety-three four-hundred-ninety-four four-hundred-ninety-five four-hundred-ninety-six four-hundred-ninety-seven four-hundred-ninety-eight four-hundred-ninety-nine five-hundred five-hundred-one five-hundred-two five-hundred-three five-hundred-four five-hundred-five five-hundred-six five-hundred-seven five-hundred-eight five-hundred-nine five-hundred-ten five-hundred-eleven five-hundred-twelve five-hundred-thirteen five-hundred-fourteen five-hundred-fifteen five-hundred-sixteen five-hundred-seventeen five-hundred-eighteen five-hundred-nineteen five-hundred-twenty five-hundred-twenty-one five-hundred-twenty-two five-hundred-twenty-three five-hundred-twenty-four five-hundred-twenty-five five-hundred-twenty-six five-hundred-twenty-seven five-hundred-twenty-eight five-hundred-twenty-nine five-hundred-thirty five-hundred-thirty-one five-hundred-thirty-two five-hundred-thirty-three five-hundred-thirty-four five-hundred-thirty-five five-hundred-thirty-six five-hundred-thirty-seven five-hundred-thirty-eight five-hundred-thirty-nine five-hundred-forty five-hundred-forty-one five-hundred-forty-two five-hundred-forty-three five-hundred-forty-four five-hundred-forty-five five-hundred-forty-six five-hundred-forty-seven five-hundred-forty-eight five-hundred-forty-nine five-hundred-fifty five-hundred-fifty-one five-hundred-fifty-two five-hundred-fifty-three five-hundred-fifty-four five-hundred-fifty-five five-hundred-fifty-six five-hundred-fifty-seven five-hundred-fifty-eight five-hundred-fifty-nine five-hundred-sixty five-hundred-sixty-one five-hundred-sixty-two five-hundred-sixty-three five-hundred-sixty-four five-hundred-sixty-five five-hundred-sixty-six five-hundred-sixty-seven five-hundred-sixty-eight five-hundred-sixty-nine five-hundred-seventy five-hundred-seventy-one five-hundred-seventy-two five-hundred-seventy-three five-hundred-seventy-four five-hundred-seventy-five five-hundred-seventy-six five-hundred-seventy-seven five-hundred-seventy-eight five-hundred-seventy-nine five-hundred-eighty five-hundred-eighty-one five-hundred-eighty-two five-hundred-eighty-three five-hundred-eighty-four five-hundred-eighty-five five-hundred-eighty-six five-hundred-eighty-seven five-hundred-eighty-eight five-hundred-eighty-nine five-hundred-ninety five-hundred-ninety-one five-hundred-ninety-two five-hundred-ninety-three five-hundred-ninety-four five-hundred-ninety-five five-hundred-ninety-six five-hundred-ninety-seven five-hundred-ninety-eight five-hundred-ninety-nine six-hundred six-hundred-one six-hundred-two six-hundred-three six-hundred-four six-hundred-five six-hundred-six six-hundred-seven six-hundred-eight six-hundred-nine six-hundred-ten six-hundred-eleven six-hundred-twelve six-hundred-thirteen six-hundred-fourteen six-hundred-fifteen six-hundred-sixteen six-hundred-seventeen six-hundred-eighteen six-hundred-nineteen six-hundred-twenty six-hundred-twenty-one six-hundred-twenty-two six-hundred-twenty-three six-hundred-twenty-four six-hundred-twenty-five six-hundred-twenty-six six-hundred-twenty-seven six-hundred-twenty-eight six-hundred-twenty-nine six-hundred-thirty six-hundred-thirty-one six-hundred-thirty-two six-hundred-thirty-three six-hundred-thirty-four six-hundred-thirty-five six-hundred-thirty-six six-hundred-thirty-seven six-hundred-thirty-eight six-hundred-thirty-nine six-hundred-forty six-hundred-forty-one six-hundred-forty-two six-hundred-forty-three six-hundred-forty-four six-hundred-forty-five six-hundred-forty-six six-hundred-forty-seven six-hundred-forty-eight six-hundred-forty-nine six-hundred-fifty six-hundred-fifty-one six-hundred-fifty-two six-hundred-fifty-three six-hundred-fifty-four six-hundred-fifty-five six-hundred-fifty-six six-hundred-fifty-seven six-hundred-fifty-eight six-hundred-fifty-nine six-hundred-sixty six-hundred-sixty-one six-hundred-sixty-two six-hundred-sixty-three six-hundred-sixty-four six-hundred-sixty-five six-hundred-sixty-six six-hundred-sixty-seven six-hundred-sixty-eight six-hundred-sixty-nine six-hundred-seventy six-hundred-seventy-one six-hundred-seventy-two six-hundred-seventy-three six-hundred-seventy-four six-hundred-seventy-five six-hundred-seventy-six six-hundred-seventy-seven six-hundred-seventy-eight six-hundred-seventy-nine six-hundred-eighty six-hundred-eighty-one six-hundred-eighty-two six-hundred-eighty-three six-hundred-eighty-four six-hundred-eighty-five six-hundred-eighty-six six-hundred-eighty-seven six-hundred-eighty-eight six-hundred-eighty-nine six-hundred-ninety six-hundred-ninety-one six-hundred-ninety-two six-hundred-ninety-three six-hundred-ninety-four six-hundred-ninety-five six-hundred-ninety-six six-hundred-ninety-seven six-hundred-ninety-eight six-hundred-ninety-nine seven-hundred seven-hundred-one seven-hundred-two seven-hundred-three seven-hundred-four seven-hundred-five seven-hundred-six seven-hundred-seven seven-hundred-eight seven-hundred-nine seven-hundred-ten seven-hundred-eleven seven-hundred-twelve seven-hundred-thirteen seven-hundred-fourteen seven-hundred-fifteen seven-hundred-sixteen seven-hundred-seventeen seven-hundred-eighteen seven-hundred-nineteen seven-hundred-twenty seven-hundred-twenty-one seven-hundred-twenty-two seven-hundred-twenty-three seven-hundred-twenty-four seven-hundred-twenty-five seven-hundred-twenty-six seven-hundred-twenty-seven seven-hundred-twenty-eight seven-hundred-twenty-nine seven-hundred-thirty seven-hundred-thirty-one seven-hundred-thirty-two seven-hundred-thirty-three seven-hundred-thirty-four seven-hundred-thirty-five seven-hundred-thirty-six seven-hundred-thirty-seven seven-hundred-thirty-eight seven-hundred-thirty-nine seven-hundred-forty seven-hundred-forty-one seven-hundred-forty-two seven-hundred-forty-three seven-hundred-forty-four seven-hundred-forty-five seven-hundred-forty-six seven-hundred-forty-seven seven-hundred-forty-eight seven-hundred-forty-nine seven-hundred-fifty seven-hundred-fifty-one seven-hundred-fifty-two seven-hundred-fifty-three seven-hundred-fifty-four seven-hundred-fifty-five seven-hundred-fifty-six seven-hundred-fifty-seven seven-hundred-fifty-eight seven-hundred-fifty-nine seven-hundred-sixty seven-hundred-sixty-one seven-hundred-sixty-two seven-hundred-sixty-three seven-hundred-sixty-four seven-hundred-sixty-five seven-hundred-sixty-six seven-hundred-sixty-seven seven-hundred-sixty-eight seven-hundred-sixty-nine seven-hundred-seventy seven-hundred-seventy-one seven-hundred-seventy-two seven-hundred-seventy-three seven-hundred-seventy-four seven-hundred-seventy-five seven-hundred-seventy-six seven-hundred-seventy-seven seven-hundred-seventy-eight seven-hundred-seventy-nine seven-hundred-eighty seven-hundred-eighty-one seven-hundred-eighty-two seven-hundred-eighty-three seven-hundred-eighty-four seven-hundred-eighty-five seven-hundred-eighty-six seven-hundred-eighty-seven seven-hundred-eighty-eight seven-hundred-eighty-nine seven-hundred-ninety seven-hundred-ninety-one seven-hundred-ninety-two seven-hundred-ninety-three seven-hundred-ninety-four seven-hundred-ninety-five seven-hundred-ninety-six seven-hundred-ninety-seven seven-hundred-ninety-eight seven-hundred-ninety-nine eight-hundred eight-hundred-one eight-hundred-two eight-hundred-three eight-hundred-four eight-hundred-five eight-hundred-six eight-hundred-seven eight-hundred-eight eight-hundred-nine eight-hundred-ten eight-hundred-eleven eight-hundred-twelve eight-hundred-thirteen eight-hundred-fourteen eight-hundred-fifteen eight-hundred-sixteen eight-hundred-seventeen eight-hundred-eighteen eight-hundred-nineteen eight-hundred-twenty eight-hundred-twenty-one eight-hundred-twenty-two eight-hundred-twenty-three eight-hundred-twenty-four eight-hundred-twenty-five eight-hundred-twenty-six eight-hundred-twenty-seven eight-hundred-twenty-eight eight-hundred-twenty-nine eight-hundred-thirty eight-hundred-thirty-one eight-hundred-thirty-two eight-hundred-thirty-three eight-hundred-thirty-four eight-hundred-thirty-five eight-hundred-thirty-six eight-hundred-thirty-seven eight-hundred-thirty-eight eight-hundred-thirty-nine eight-hundred-forty eight-hundred-forty-one eight-hundred-forty-two eight-hundred-forty-three eight-hundred-forty-four eight-hundred-forty-five eight-hundred-forty-six eight-hundred-forty-seven eight-hundred-forty-eight eight-hundred-forty-nine eight-hundred-fifty eight-hundred-fifty-one eight-hundred-fifty-two eight-hundred-fifty-three eight-hundred-fifty-four eight-hundred-fifty-five eight-hundred-fifty-six eight-hundred-fifty-seven eight-hundred-fifty-eight eight-hundred-fifty-nine eight-hundred-sixty eight-hundred-sixty-one eight-hundred-sixty-two eight-hundred-sixty-three eight-hundred-sixty-four eight-hundred-sixty-five eight-hundred-sixty-six eight-hundred-sixty-seven eight-hundred-sixty-eight eight-hundred-sixty-nine eight-hundred-seventy eight-hundred-seventy-one eight-hundred-seventy-two eight-hundred-seventy-three eight-hundred-seventy-four eight-hundred-seventy-five eight-hundred-seventy-six eight-hundred-seventy-seven eight-hundred-seventy-eight eight-hundred-seventy-nine eight-hundred-eighty eight-hundred-eighty-one eight-hundred-eighty-two eight-hundred-eighty-three eight-hundred-eighty-four eight-hundred-eighty-five eight-hundred-eighty-six eight-hundred-eighty-seven eight-hundred-eighty-eight eight-hundred-eighty-nine eight-hundred-ninety eight-hundred-ninety-one eight-hundred-ninety-two eight-hundred-ninety-three eight-hundred-ninety-four eight-hundred-ninety-five eight-hundred-ninety-six eight-hundred-ninety-seven eight-hundred-ninety-eight eight-hundred-ninety-nine nine-hundred nine-hundred-one nine-hundred-two nine-hundred-three nine-hundred-four nine-hundred-five nine-hundred-six nine-hundred-seven nine-hundred-eight nine-hundred-nine nine-hundred-ten nine-hundred-eleven nine-hundred-twelve nine-hundred-thirteen nine-hundred-fourteen nine-hundred-fifteen nine-hundred-sixteen nine-hundred-seventeen nine-hundred-eighteen nine-hundred-nineteen nine-hundred-twenty nine-hundred-twenty-one nine-hundred-twenty-two nine-hundred-twenty-three nine-hundred-twenty-four nine-hundred-twenty-five nine-hundred-twenty-six nine-hundred-twenty-seven nine-hundred-twenty-eight nine-hundred-twenty-nine nine-hundred-thirty nine-hundred-thirty-one nine-hundred-thirty-two nine-hundred-thirty-three nine-hundred-thirty-four nine-hundred-thirty-five nine-hundred-thirty-six nine-hundred-thirty-seven nine-hundred-thirty-eight nine-hundred-thirty-nine nine-hundred-forty nine-hundred-forty-one nine-hundred-forty-two nine-hundred-forty-three nine-hundred-forty-four nine-hundred-forty-five nine-hundred-forty-six nine-hundred-forty-seven nine-hundred-forty-eight nine-hundred-forty-nine nine-hundred-fifty nine-hundred-fifty-one nine-hundred-fifty-two nine-hundred-fifty-three nine-hundred-fifty-four nine-hundred-fifty-five nine-hundred-fifty-six nine-hundred-fifty-seven nine-hundred-fifty-eight nine-hundred-fifty-nine nine-hundred-sixty nine-hundred-sixty-one nine-hundred-sixty-two nine-hundred-sixty-three nine-hundred-sixty-four nine-hundred-sixty-five nine-hundred-sixty-six nine-hundred-sixty-seven nine-hundred-sixty-eight nine-hundred-sixty-nine nine-hundred-seventy nine-hundred-seventy-one nine-hundred-seventy-two nine-hundred-seventy-three nine-hundred-seventy-four nine-hundred-seventy-five nine-hundred-seventy-six nine-hundred-seventy-seven nine-hundred-seventy-eight nine-hundred-seventy-nine nine-hundred-eighty nine-hundred-eighty-one nine-hundred-eighty-two nine-hundred-eighty-three nine-hundred-eighty-four nine-hundred-eighty-five nine-hundred-eighty-six nine-hundred-eighty-seven nine-hundred-eighty-eight nine-hundred-eighty-nine nine-hundred-ninety nine-hundred-ninety-one nine-hundred-ninety-two nine-hundred-ninety-three nine-hundred-ninety-four nine-hundred-ninety-five nine-hundred-ninety-six nine-hundred-ninety-seven nine-hundred-ninety-eight nine-hundred-ninety-nine one-thousand"""

one_to_hundred_arr = one_to_hundred.split(' ')
# print(one_to_hundred_arr)
# print(len(one_to_hundred_arr))

input_arr = users_input_pair_values.split(',')
print(input_arr)

for every_pair_num in input_arr:
    for word in one_to_hundred_arr:
        num = one_to_hundred_arr.index(word)
        if int(every_pair_num) == int(num):
           number_result = one_to_hundred_arr[num]
           print(number_result)







# Function in Python
# "def name () :"
# "def" is used to, when you're or want to use a function
# """"def func() :
#     print('function')""""
# where "func" is the "name" of the function, which can be anything at all.

