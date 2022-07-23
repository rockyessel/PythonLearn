

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

one_to_hundred = """
zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four twenty-five twenty-six twenty-seven twenty-eight twenty-nine thirty thirty-one thirty-two thirty-three thirty-four thirty-five thirty-six thirty-seven thirty-eight thirty-nine forty forty-one forty-two forty-three forty-four forty-five forty-six forty-seven forty-eight forty-nine fifty fifty-one fifty-two fifty-three fifty-four fifty-five fifty-six fifty-seven fifty-eight fifty-nine sixty sixty-one sixty-two sixty-three sixty-four sixty-five sixty-six sixty-seven sixty-eight sixty-nine seventy seventy-one seventy-two seventy-three seventy-four seventy-five seventy-six seventy-seven seventy-eight seventy-nine eighty eighty-one eighty-two eighty-three eighty-four eighty-five eighty-six eighty-seven eighty-eight eighty-nine ninety ninety-one ninety-two ninety-three ninety-four ninety-five ninety-six ninety-seven ninety-eight ninety-nine one-hundred one-hundred-one one-hundred-two one-hundred-three one-hundred-four one-hundred-five one-hundred-six one-hundred-seven one-hundred-eight one-hundred-nine one-hundred-ten one-hundred-eleven one-hundred-twelve one-hundred-thirteen one-hundred-fourteen one-hundred-fifteen one-hundred-sixteen one-hundred-seventeen one-hundred-eighteen one-hundred-nineteen one-hundred-twenty one-hundred-twenty-one one-hundred-twenty-two one-hundred-twenty-three one-hundred-twenty-four one-hundred-twenty-five one-hundred-twenty-six one-hundred-twenty-seven one-hundred-twenty-eight one-hundred-twenty-nine one-hundred-thirty one-hundred-thirty-one one-hundred-thirty-two one-hundred-thirty-three one-hundred-thirty-four one-hundred-thirty-five one-hundred-thirty-six one-hundred-thirty-seven one-hundred-thirty-eight one-hundred-thirty-nine one-hundred-forty one-hundred-forty-one one-hundred-forty-two one-hundred-forty-three one-hundred-forty-four one-hundred-forty-five one-hundred-forty-six one-hundred-forty-seven one-hundred-forty-eight one-hundred-forty-nine one-hundred-fifty one-hundred-fifty-one one-hundred-fifty-two one-hundred-fifty-three one-hundred-fifty-four one-hundred-fifty-five one-hundred-fifty-six one-hundred-fifty-seven one-hundred-fifty-eight one-hundred-fifty-nine one-hundred-sixty one-hundred-sixty-one one-hundred-sixty-two one-hundred-sixty-three one-hundred-sixty-four one-hundred-sixty-five one-hundred-sixty-six one-hundred-sixty-seven one-hundred-sixty-eight one-hundred-sixty-nine one-hundred-seventy one-hundred-seventy-one one-hundred-seventy-two one-hundred-seventy-three one-hundred-seventy-four one-hundred-seventy-five one-hundred-seventy-six one-hundred-seventy-seven one-hundred-seventy-eight one-hundred-seventy-nine one-hundred-eighty one-hundred-eighty-one one-hundred-eighty-two one-hundred-eighty-three one-hundred-eighty-four one-hundred-eighty-five one-hundred-eighty-six one-hundred-eighty-seven one-hundred-eighty-eight one-hundred-eighty-nine one-hundred-ninety one-hundred-ninety-one one-hundred-ninety-two one-hundred-ninety-three one-hundred-ninety-four one-hundred-ninety-five one-hundred-ninety-six one-hundred-ninety-seven one-hundred-ninety-eight one-hundred-ninety-nine two-hundred two-hundred-one two-hundred-two two-hundred-three two-hundred-four two-hundred-five two-hundred-six two-hundred-seven two-hundred-eight two-hundred-nine two-hundred-ten two-hundred-eleven two-hundred-twelve two-hundred-thirteen two-hundred-fourteen two-hundred-fifteen two-hundred-sixteen two-hundred-seventeen two-hundred-eighteen two-hundred-nineteen two-hundred-twenty two-hundred-twenty-one two-hundred-twenty-two two-hundred-twenty-three two-hundred-twenty-four two-hundred-twenty-five two-hundred-twenty-six two-hundred-twenty-seven two-hundred-twenty-eight two-hundred-twenty-nine two-hundred-thirty two-hundred-thirty-one two-hundred-thirty-two two-hundred-thirty-three two-hundred-thirty-four two-hundred-thirty-five two-hundred-thirty-six two-hundred-thirty-seven two-hundred-thirty-eight two-hundred-thirty-nine two-hundred-forty two-hundred-forty-one two-hundred-forty-two two-hundred-forty-three two-hundred-forty-four two-hundred-forty-five two-hundred-forty-six two-hundred-forty-seven two-hundred-forty-eight two-hundred-forty-nine two-hundred-fifty two-hundred-fifty-one two-hundred-fifty-two two-hundred-fifty-three two-hundred-fifty-four two-hundred-fifty-five two-hundred-fifty-six two-hundred-fifty-seven two-hundred-fifty-eight two-hundred-fifty-nine two-hundred-sixty two-hundred-sixty-one two-hundred-sixty-two two-hundred-sixty-three two-hundred-sixty-four two-hundred-sixty-five two-hundred-sixty-six two-hundred-sixty-seven two-hundred-sixty-eight two-hundred-sixty-nine two-hundred-seventy two-hundred-seventy-one two-hundred-seventy-two two-hundred-seventy-three two-hundred-seventy-four two-hundred-seventy-five two-hundred-seventy-six two-hundred-seventy-seven two-hundred-seventy-eight two-hundred-seventy-nine two-hundred-eighty two-hundred-eighty-one two-hundred-eighty-two two-hundred-eighty-three two-hundred-eighty-four two-hundred-eighty-five two-hundred-eighty-six two-hundred-eighty-seven two-hundred-eighty-eight two-hundred-eighty-nine two-hundred-ninety two-hundred-ninety-one two-hundred-ninety-two two-hundred-ninety-three two-hundred-ninety-four two-hundred-ninety-five two-hundred-ninety-six two-hundred-ninety-seven two-hundred-ninety-eight two-hundred-ninety-nine three-hundred three-hundred-one three-hundred-two three-hundred-three three-hundred-four three-hundred-five three-hundred-six three-hundred-seven three-hundred-eight three-hundred-nine three-hundred-ten three-hundred-eleven three-hundred-twelve three-hundred-thirteen three-hundred-fourteen three-hundred-fifteen three-hundred-sixteen three-hundred-seventeen three-hundred-eighteen three-hundred-nineteen three-hundred-twenty three-hundred-twenty-one three-hundred-twenty-two three-hundred-twenty-three three-hundred-twenty-four three-hundred-twenty-five three-hundred-twenty-six three-hundred-twenty-seven three-hundred-twenty-eight three-hundred-twenty-nine three-hundred-thirty three-hundred-thirty-one three-hundred-thirty-two three-hundred-thirty-three three-hundred-thirty-four three-hundred-thirty-five three-hundred-thirty-six three-hundred-thirty-seven three-hundred-thirty-eight three-hundred-thirty-nine three-hundred-forty three-hundred-forty-one three-hundred-forty-two three-hundred-forty-three three-hundred-forty-four three-hundred-forty-five three-hundred-forty-six three-hundred-forty-seven three-hundred-forty-eight three-hundred-forty-nine three-hundred-fifty three-hundred-fifty-one three-hundred-fifty-two three-hundred-fifty-three three-hundred-fifty-four three-hundred-fifty-five three-hundred-fifty-six three-hundred-fifty-seven three-hundred-fifty-eight three-hundred-fifty-nine three-hundred-sixty three-hundred-sixty-one three-hundred-sixty-two three-hundred-sixty-three three-hundred-sixty-four three-hundred-sixty-five three-hundred-sixty-six three-hundred-sixty-seven three-hundred-sixty-eight three-hundred-sixty-nine three-hundred-seventy three-hundred-seventy-one three-hundred-seventy-two three-hundred-seventy-three three-hundred-seventy-four three-hundred-seventy-five three-hundred-seventy-six three-hundred-seventy-seven three-hundred-seventy-eight three-hundred-seventy-nine three-hundred-eighty three-hundred-eighty-one three-hundred-eighty-two three-hundred-eighty-three three-hundred-eighty-four three-hundred-eighty-five three-hundred-eighty-six three-hundred-eighty-seven three-hundred-eighty-eight three-hundred-eighty-nine three-hundred-ninety three-hundred-ninety-one three-hundred-ninety-two three-hundred-ninety-three three-hundred-ninety-four three-hundred-ninety-five three-hundred-ninety-six three-hundred-ninety-seven three-hundred-ninety-eight three-hundred-ninety-nine four-hundred four-hundred-one four-hundred-two four-hundred-three four-hundred-four four-hundred-five four-hundred-six four-hundred-seven four-hundred-eight four-hundred-nine four-hundred-ten four-hundred-eleven four-hundred-twelve four-hundred-thirteen four-hundred-fourteen four-hundred-fifteen four-hundred-sixteen four-hundred-seventeen four-hundred-eighteen four-hundred-nineteen four-hundred-twenty four-hundred-twenty-one four-hundred-twenty-two four-hundred-twenty-three four-hundred-twenty-four four-hundred-twenty-five four-hundred-twenty-six four-hundred-twenty-seven four-hundred-twenty-eight four-hundred-twenty-nine four-hundred-thirty four-hundred-thirty-one four-hundred-thirty-two four-hundred-thirty-three four-hundred-thirty-four four-hundred-thirty-five four-hundred-thirty-six four-hundred-thirty-seven four-hundred-thirty-eight four-hundred-thirty-nine four-hundred-forty four-hundred-forty-one four-hundred-forty-two four-hundred-forty-three four-hundred-forty-four four-hundred-forty-five four-hundred-forty-six four-hundred-forty-seven four-hundred-forty-eight four-hundred-forty-nine four-hundred-fifty four-hundred-fifty-one four-hundred-fifty-two four-hundred-fifty-three four-hundred-fifty-four four-hundred-fifty-five four-hundred-fifty-six four-hundred-fifty-seven four-hundred-fifty-eight four-hundred-fifty-nine four-hundred-sixty four-hundred-sixty-one four-hundred-sixty-two four-hundred-sixty-three four-hundred-sixty-four four-hundred-sixty-five four-hundred-sixty-six four-hundred-sixty-seven four-hundred-sixty-eight four-hundred-sixty-nine four-hundred-seventy four-hundred-seventy-one four-hundred-seventy-two four-hundred-seventy-three four-hundred-seventy-four four-hundred-seventy-five four-hundred-seventy-six four-hundred-seventy-seven four-hundred-seventy-eight four-hundred-seventy-nine four-hundred-eighty four-hundred-eighty-one four-hundred-eighty-two four-hundred-eighty-three four-hundred-eighty-four four-hundred-eighty-five four-hundred-eighty-six four-hundred-eighty-seven four-hundred-eighty-eight four-hundred-eighty-nine four-hundred-ninety four-hundred-ninety-one four-hundred-ninety-two four-hundred-ninety-three four-hundred-ninety-four four-hundred-ninety-five four-hundred-ninety-six four-hundred-ninety-seven four-hundred-ninety-eight four-hundred-ninety-nine five-hundred five-hundred-one five-hundred-two five-hundred-three five-hundred-four five-hundred-five five-hundred-six five-hundred-seven five-hundred-eight five-hundred-nine five-hundred-ten five-hundred-eleven five-hundred-twelve five-hundred-thirteen five-hundred-fourteen five-hundred-fifteen five-hundred-sixteen five-hundred-seventeen five-hundred-eighteen five-hundred-nineteen five-hundred-twenty five-hundred-twenty-one five-hundred-twenty-two five-hundred-twenty-three five-hundred-twenty-four five-hundred-twenty-five five-hundred-twenty-six five-hundred-twenty-seven five-hundred-twenty-eight five-hundred-twenty-nine five-hundred-thirty five-hundred-thirty-one five-hundred-thirty-two five-hundred-thirty-three five-hundred-thirty-four five-hundred-thirty-five five-hundred-thirty-six five-hundred-thirty-seven five-hundred-thirty-eight five-hundred-thirty-nine five-hundred-forty five-hundred-forty-one five-hundred-forty-two five-hundred-forty-three five-hundred-forty-four five-hundred-forty-five five-hundred-forty-six five-hundred-forty-seven five-hundred-forty-eight five-hundred-forty-nine five-hundred-fifty five-hundred-fifty-one five-hundred-fifty-two five-hundred-fifty-three five-hundred-fifty-four five-hundred-fifty-five five-hundred-fifty-six five-hundred-fifty-seven five-hundred-fifty-eight five-hundred-fifty-nine five-hundred-sixty five-hundred-sixty-one five-hundred-sixty-two five-hundred-sixty-three five-hundred-sixty-four five-hundred-sixty-five five-hundred-sixty-six five-hundred-sixty-seven five-hundred-sixty-eight five-hundred-sixty-nine five-hundred-seventy five-hundred-seventy-one five-hundred-seventy-two five-hundred-seventy-three five-hundred-seventy-four five-hundred-seventy-five five-hundred-seventy-six five-hundred-seventy-seven five-hundred-seventy-eight five-hundred-seventy-nine five-hundred-eighty five-hundred-eighty-one five-hundred-eighty-two five-hundred-eighty-three five-hundred-eighty-four five-hundred-eighty-five five-hundred-eighty-six five-hundred-eighty-seven five-hundred-eighty-eight five-hundred-eighty-nine five-hundred-ninety five-hundred-ninety-one five-hundred-ninety-two five-hundred-ninety-three five-hundred-ninety-four five-hundred-ninety-five five-hundred-ninety-six five-hundred-ninety-seven five-hundred-ninety-eight five-hundred-ninety-nine six-hundred six-hundred-one six-hundred-two six-hundred-three six-hundred-four six-hundred-five six-hundred-six six-hundred-seven six-hundred-eight six-hundred-nine six-hundred-ten six-hundred-eleven six-hundred-twelve six-hundred-thirteen six-hundred-fourteen six-hundred-fifteen six-hundred-sixteen six-hundred-seventeen six-hundred-eighteen six-hundred-nineteen six-hundred-twenty six-hundred-twenty-one six-hundred-twenty-two six-hundred-twenty-three six-hundred-twenty-four six-hundred-twenty-five six-hundred-twenty-six six-hundred-twenty-seven six-hundred-twenty-eight six-hundred-twenty-nine six-hundred-thirty six-hundred-thirty-one six-hundred-thirty-two six-hundred-thirty-three six-hundred-thirty-four six-hundred-thirty-five six-hundred-thirty-six six-hundred-thirty-seven six-hundred-thirty-eight six-hundred-thirty-nine six-hundred-forty six-hundred-forty-one six-hundred-forty-two six-hundred-forty-three six-hundred-forty-four six-hundred-forty-five six-hundred-forty-six six-hundred-forty-seven six-hundred-forty-eight six-hundred-forty-nine six-hundred-fifty six-hundred-fifty-one six-hundred-fifty-two six-hundred-fifty-three six-hundred-fifty-four six-hundred-fifty-five six-hundred-fifty-six six-hundred-fifty-seven six-hundred-fifty-eight six-hundred-fifty-nine six-hundred-sixty six-hundred-sixty-one six-hundred-sixty-two six-hundred-sixty-three six-hundred-sixty-four six-hundred-sixty-five six-hundred-sixty-six six-hundred-sixty-seven six-hundred-sixty-eight six-hundred-sixty-nine six-hundred-seventy six-hundred-seventy-one six-hundred-seventy-two six-hundred-seventy-three six-hundred-seventy-four six-hundred-seventy-five six-hundred-seventy-six six-hundred-seventy-seven six-hundred-seventy-eight six-hundred-seventy-nine six-hundred-eighty six-hundred-eighty-one six-hundred-eighty-two six-hundred-eighty-three six-hundred-eighty-four six-hundred-eighty-five six-hundred-eighty-six six-hundred-eighty-seven six-hundred-eighty-eight six-hundred-eighty-nine six-hundred-ninety six-hundred-ninety-one six-hundred-ninety-two six-hundred-ninety-three six-hundred-ninety-four six-hundred-ninety-five six-hundred-ninety-six six-hundred-ninety-seven six-hundred-ninety-eight six-hundred-ninety-nine seven-hundred seven-hundred-one seven-hundred-two seven-hundred-three seven-hundred-four seven-hundred-five seven-hundred-six seven-hundred-seven seven-hundred-eight seven-hundred-nine seven-hundred-ten seven-hundred-eleven seven-hundred-twelve seven-hundred-thirteen seven-hundred-fourteen seven-hundred-fifteen seven-hundred-sixteen seven-hundred-seventeen seven-hundred-eighteen seven-hundred-nineteen seven-hundred-twenty seven-hundred-twenty-one seven-hundred-twenty-two seven-hundred-twenty-three seven-hundred-twenty-four seven-hundred-twenty-five seven-hundred-twenty-six seven-hundred-twenty-seven seven-hundred-twenty-eight seven-hundred-twenty-nine seven-hundred-thirty seven-hundred-thirty-one seven-hundred-thirty-two seven-hundred-thirty-three seven-hundred-thirty-four seven-hundred-thirty-five seven-hundred-thirty-six seven-hundred-thirty-seven seven-hundred-thirty-eight seven-hundred-thirty-nine seven-hundred-forty seven-hundred-forty-one seven-hundred-forty-two seven-hundred-forty-three seven-hundred-forty-four seven-hundred-forty-five seven-hundred-forty-six seven-hundred-forty-seven seven-hundred-forty-eight seven-hundred-forty-nine seven-hundred-fifty seven-hundred-fifty-one seven-hundred-fifty-two seven-hundred-fifty-three seven-hundred-fifty-four seven-hundred-fifty-five seven-hundred-fifty-six seven-hundred-fifty-seven seven-hundred-fifty-eight seven-hundred-fifty-nine seven-hundred-sixty seven-hundred-sixty-one seven-hundred-sixty-two seven-hundred-sixty-three seven-hundred-sixty-four seven-hundred-sixty-five seven-hundred-sixty-six seven-hundred-sixty-seven seven-hundred-sixty-eight seven-hundred-sixty-nine seven-hundred-seventy seven-hundred-seventy-one seven-hundred-seventy-two seven-hundred-seventy-three seven-hundred-seventy-four seven-hundred-seventy-five seven-hundred-seventy-six seven-hundred-seventy-seven seven-hundred-seventy-eight seven-hundred-seventy-nine seven-hundred-eighty seven-hundred-eighty-one seven-hundred-eighty-two seven-hundred-eighty-three seven-hundred-eighty-four seven-hundred-eighty-five seven-hundred-eighty-six seven-hundred-eighty-seven seven-hundred-eighty-eight seven-hundred-eighty-nine seven-hundred-ninety seven-hundred-ninety-one seven-hundred-ninety-two seven-hundred-ninety-three seven-hundred-ninety-four seven-hundred-ninety-five seven-hundred-ninety-six seven-hundred-ninety-seven seven-hundred-ninety-eight seven-hundred-ninety-nine eight-hundred eight-hundred-one eight-hundred-two eight-hundred-three eight-hundred-four eight-hundred-five eight-hundred-six eight-hundred-seven eight-hundred-eight eight-hundred-nine eight-hundred-ten eight-hundred-eleven eight-hundred-twelve eight-hundred-thirteen eight-hundred-fourteen eight-hundred-fifteen eight-hundred-sixteen eight-hundred-seventeen eight-hundred-eighteen eight-hundred-nineteen eight-hundred-twenty eight-hundred-twenty-one eight-hundred-twenty-two eight-hundred-twenty-three eight-hundred-twenty-four eight-hundred-twenty-five eight-hundred-twenty-six eight-hundred-twenty-seven eight-hundred-twenty-eight eight-hundred-twenty-nine eight-hundred-thirty eight-hundred-thirty-one eight-hundred-thirty-two eight-hundred-thirty-three eight-hundred-thirty-four eight-hundred-thirty-five eight-hundred-thirty-six eight-hundred-thirty-seven eight-hundred-thirty-eight eight-hundred-thirty-nine eight-hundred-forty eight-hundred-forty-one eight-hundred-forty-two eight-hundred-forty-three eight-hundred-forty-four eight-hundred-forty-five eight-hundred-forty-six eight-hundred-forty-seven eight-hundred-forty-eight eight-hundred-forty-nine eight-hundred-fifty eight-hundred-fifty-one eight-hundred-fifty-two eight-hundred-fifty-three eight-hundred-fifty-four eight-hundred-fifty-five eight-hundred-fifty-six eight-hundred-fifty-seven eight-hundred-fifty-eight eight-hundred-fifty-nine eight-hundred-sixty eight-hundred-sixty-one eight-hundred-sixty-two eight-hundred-sixty-three eight-hundred-sixty-four eight-hundred-sixty-five eight-hundred-sixty-six eight-hundred-sixty-seven eight-hundred-sixty-eight eight-hundred-sixty-nine eight-hundred-seventy eight-hundred-seventy-one eight-hundred-seventy-two eight-hundred-seventy-three eight-hundred-seventy-four eight-hundred-seventy-five eight-hundred-seventy-six eight-hundred-seventy-seven eight-hundred-seventy-eight eight-hundred-seventy-nine eight-hundred-eighty eight-hundred-eighty-one eight-hundred-eighty-two eight-hundred-eighty-three eight-hundred-eighty-four eight-hundred-eighty-five eight-hundred-eighty-six eight-hundred-eighty-seven eight-hundred-eighty-eight eight-hundred-eighty-nine eight-hundred-ninety eight-hundred-ninety-one eight-hundred-ninety-two eight-hundred-ninety-three eight-hundred-ninety-four eight-hundred-ninety-five eight-hundred-ninety-six eight-hundred-ninety-seven eight-hundred-ninety-eight eight-hundred-ninety-nine nine-hundred nine-hundred-one nine-hundred-two nine-hundred-three nine-hundred-four nine-hundred-five nine-hundred-six nine-hundred-seven nine-hundred-eight nine-hundred-nine nine-hundred-ten nine-hundred-eleven nine-hundred-twelve nine-hundred-thirteen nine-hundred-fourteen nine-hundred-fifteen nine-hundred-sixteen nine-hundred-seventeen nine-hundred-eighteen nine-hundred-nineteen nine-hundred-twenty nine-hundred-twenty-one nine-hundred-twenty-two nine-hundred-twenty-three nine-hundred-twenty-four nine-hundred-twenty-five nine-hundred-twenty-six nine-hundred-twenty-seven nine-hundred-twenty-eight nine-hundred-twenty-nine nine-hundred-thirty nine-hundred-thirty-one nine-hundred-thirty-two nine-hundred-thirty-three nine-hundred-thirty-four nine-hundred-thirty-five nine-hundred-thirty-six nine-hundred-thirty-seven nine-hundred-thirty-eight nine-hundred-thirty-nine nine-hundred-forty nine-hundred-forty-one nine-hundred-forty-two nine-hundred-forty-three nine-hundred-forty-four nine-hundred-forty-five nine-hundred-forty-six nine-hundred-forty-seven nine-hundred-forty-eight nine-hundred-forty-nine nine-hundred-fifty nine-hundred-fifty-one nine-hundred-fifty-two nine-hundred-fifty-three nine-hundred-fifty-four nine-hundred-fifty-five nine-hundred-fifty-six nine-hundred-fifty-seven nine-hundred-fifty-eight nine-hundred-fifty-nine nine-hundred-sixty nine-hundred-sixty-one nine-hundred-sixty-two nine-hundred-sixty-three nine-hundred-sixty-four nine-hundred-sixty-five nine-hundred-sixty-six nine-hundred-sixty-seven nine-hundred-sixty-eight nine-hundred-sixty-nine nine-hundred-seventy nine-hundred-seventy-one nine-hundred-seventy-two nine-hundred-seventy-three nine-hundred-seventy-four nine-hundred-seventy-five nine-hundred-seventy-six nine-hundred-seventy-seven nine-hundred-seventy-eight nine-hundred-seventy-nine nine-hundred-eighty nine-hundred-eighty-one nine-hundred-eighty-two nine-hundred-eighty-three nine-hundred-eighty-four nine-hundred-eighty-five nine-hundred-eighty-six nine-hundred-eighty-seven nine-hundred-eighty-eight nine-hundred-eighty-nine nine-hundred-ninety nine-hundred-ninety-one nine-hundred-ninety-two nine-hundred-ninety-three nine-hundred-ninety-four nine-hundred-ninety-five nine-hundred-ninety-six nine-hundred-ninety-seven nine-hundred-ninety-eight nine-hundred-ninety-nine one-thousand one-thousand-one one-thousand-two one-thousand-three one-thousand-four one-thousand-five one-thousand-six one-thousand-seven one-thousand-eight one-thousand-nine one-thousand-ten one-thousand-eleven one-thousand-twelve one-thousand-thirteen one-thousand-fourteen one-thousand-fifteen one-thousand-sixteen one-thousand-seventeen one-thousand-eighteen one-thousand-nineteen one-thousand-twenty one-thousand-twenty-one one-thousand-twenty-two one-thousand-twenty-three one-thousand-twenty-four one-thousand-twenty-five one-thousand-twenty-six one-thousand-twenty-seven one-thousand-twenty-eight one-thousand-twenty-nine one-thousand-thirty one-thousand-thirty-one one-thousand-thirty-two one-thousand-thirty-three one-thousand-thirty-four one-thousand-thirty-five one-thousand-thirty-six one-thousand-thirty-seven one-thousand-thirty-eight one-thousand-thirty-nine one-thousand-forty one-thousand-forty-one one-thousand-forty-two one-thousand-forty-three one-thousand-forty-four one-thousand-forty-five one-thousand-forty-six one-thousand-forty-seven one-thousand-forty-eight one-thousand-forty-nine one-thousand-fifty one-thousand-fifty-one one-thousand-fifty-two one-thousand-fifty-three one-thousand-fifty-four one-thousand-fifty-five one-thousand-fifty-six one-thousand-fifty-seven one-thousand-fifty-eight one-thousand-fifty-nine one-thousand-sixty one-thousand-sixty-one one-thousand-sixty-two one-thousand-sixty-three one-thousand-sixty-four one-thousand-sixty-five one-thousand-sixty-six one-thousand-sixty-seven one-thousand-sixty-eight one-thousand-sixty-nine one-thousand-seventy one-thousand-seventy-one one-thousand-seventy-two one-thousand-seventy-three one-thousand-seventy-four one-thousand-seventy-five one-thousand-seventy-six one-thousand-seventy-seven one-thousand-seventy-eight one-thousand-seventy-nine one-thousand-eighty one-thousand-eighty-one one-thousand-eighty-two one-thousand-eighty-three one-thousand-eighty-four one-thousand-eighty-five one-thousand-eighty-six one-thousand-eighty-seven one-thousand-eighty-eight one-thousand-eighty-nine one-thousand-ninety one-thousand-ninety-one one-thousand-ninety-two one-thousand-ninety-three one-thousand-ninety-four one-thousand-ninety-five one-thousand-ninety-six one-thousand-ninety-seven one-thousand-ninety-eight one-thousand-ninety-nine one-thousand-one-hundred one-thousand-one-hundred-one one-thousand-one-hundred-two one-thousand-one-hundred-three one-thousand-one-hundred-four one-thousand-one-hundred-five one-thousand-one-hundred-six one-thousand-one-hundred-seven one-thousand-one-hundred-eight one-thousand-one-hundred-nine one-thousand-one-hundred-ten one-thousand-one-hundred-eleven one-thousand-one-hundred-twelve one-thousand-one-hundred-thirteen one-thousand-one-hundred-fourteen one-thousand-one-hundred-fifteen one-thousand-one-hundred-sixteen one-thousand-one-hundred-seventeen one-thousand-one-hundred-eighteen one-thousand-one-hundred-nineteen one-thousand-one-hundred-twenty one-thousand-one-hundred-twenty-one one-thousand-one-hundred-twenty-two one-thousand-one-hundred-twenty-three one-thousand-one-hundred-twenty-four one-thousand-one-hundred-twenty-five one-thousand-one-hundred-twenty-six one-thousand-one-hundred-twenty-seven one-thousand-one-hundred-twenty-eight one-thousand-one-hundred-twenty-nine one-thousand-one-hundred-thirty one-thousand-one-hundred-thirty-one one-thousand-one-hundred-thirty-two one-thousand-one-hundred-thirty-three one-thousand-one-hundred-thirty-four one-thousand-one-hundred-thirty-five one-thousand-one-hundred-thirty-six one-thousand-one-hundred-thirty-seven one-thousand-one-hundred-thirty-eight one-thousand-one-hundred-thirty-nine one-thousand-one-hundred-forty one-thousand-one-hundred-forty-one one-thousand-one-hundred-forty-two one-thousand-one-hundred-forty-three one-thousand-one-hundred-forty-four one-thousand-one-hundred-forty-five one-thousand-one-hundred-forty-six one-thousand-one-hundred-forty-seven one-thousand-one-hundred-forty-eight one-thousand-one-hundred-forty-nine one-thousand-one-hundred-fifty one-thousand-one-hundred-fifty-one one-thousand-one-hundred-fifty-two one-thousand-one-hundred-fifty-three one-thousand-one-hundred-fifty-four one-thousand-one-hundred-fifty-five one-thousand-one-hundred-fifty-six one-thousand-one-hundred-fifty-seven one-thousand-one-hundred-fifty-eight one-thousand-one-hundred-fifty-nine one-thousand-one-hundred-sixty one-thousand-one-hundred-sixty-one one-thousand-one-hundred-sixty-two one-thousand-one-hundred-sixty-three one-thousand-one-hundred-sixty-four one-thousand-one-hundred-sixty-five one-thousand-one-hundred-sixty-six one-thousand-one-hundred-sixty-seven one-thousand-one-hundred-sixty-eight one-thousand-one-hundred-sixty-nine one-thousand-one-hundred-seventy one-thousand-one-hundred-seventy-one one-thousand-one-hundred-seventy-two one-thousand-one-hundred-seventy-three one-thousand-one-hundred-seventy-four one-thousand-one-hundred-seventy-five one-thousand-one-hundred-seventy-six one-thousand-one-hundred-seventy-seven one-thousand-one-hundred-seventy-eight one-thousand-one-hundred-seventy-nine one-thousand-one-hundred-eighty one-thousand-one-hundred-eighty-one one-thousand-one-hundred-eighty-two one-thousand-one-hundred-eighty-three one-thousand-one-hundred-eighty-four one-thousand-one-hundred-eighty-five one-thousand-one-hundred-eighty-six one-thousand-one-hundred-eighty-seven one-thousand-one-hundred-eighty-eight one-thousand-one-hundred-eighty-nine one-thousand-one-hundred-ninety one-thousand-one-hundred-ninety-one one-thousand-one-hundred-ninety-two one-thousand-one-hundred-ninety-three one-thousand-one-hundred-ninety-four one-thousand-one-hundred-ninety-five one-thousand-one-hundred-ninety-six one-thousand-one-hundred-ninety-seven one-thousand-one-hundred-ninety-eight one-thousand-one-hundred-ninety-nine one-thousand-two-hundred one-thousand-two-hundred-one one-thousand-two-hundred-two one-thousand-two-hundred-three one-thousand-two-hundred-four one-thousand-two-hundred-five one-thousand-two-hundred-six one-thousand-two-hundred-seven one-thousand-two-hundred-eight one-thousand-two-hundred-nine one-thousand-two-hundred-ten one-thousand-two-hundred-eleven one-thousand-two-hundred-twelve one-thousand-two-hundred-thirteen one-thousand-two-hundred-fourteen one-thousand-two-hundred-fifteen one-thousand-two-hundred-sixteen one-thousand-two-hundred-seventeen one-thousand-two-hundred-eighteen one-thousand-two-hundred-nineteen one-thousand-two-hundred-twenty one-thousand-two-hundred-twenty-one one-thousand-two-hundred-twenty-two one-thousand-two-hundred-twenty-three one-thousand-two-hundred-twenty-four one-thousand-two-hundred-twenty-five one-thousand-two-hundred-twenty-six one-thousand-two-hundred-twenty-seven one-thousand-two-hundred-twenty-eight one-thousand-two-hundred-twenty-nine one-thousand-two-hundred-thirty one-thousand-two-hundred-thirty-one one-thousand-two-hundred-thirty-two one-thousand-two-hundred-thirty-three one-thousand-two-hundred-thirty-four one-thousand-two-hundred-thirty-five one-thousand-two-hundred-thirty-six one-thousand-two-hundred-thirty-seven one-thousand-two-hundred-thirty-eight one-thousand-two-hundred-thirty-nine one-thousand-two-hundred-forty one-thousand-two-hundred-forty-one one-thousand-two-hundred-forty-two one-thousand-two-hundred-forty-three one-thousand-two-hundred-forty-four one-thousand-two-hundred-forty-five one-thousand-two-hundred-forty-six one-thousand-two-hundred-forty-seven one-thousand-two-hundred-forty-eight one-thousand-two-hundred-forty-nine one-thousand-two-hundred-fifty one-thousand-two-hundred-fifty-one one-thousand-two-hundred-fifty-two one-thousand-two-hundred-fifty-three one-thousand-two-hundred-fifty-four one-thousand-two-hundred-fifty-five one-thousand-two-hundred-fifty-six one-thousand-two-hundred-fifty-seven one-thousand-two-hundred-fifty-eight one-thousand-two-hundred-fifty-nine one-thousand-two-hundred-sixty one-thousand-two-hundred-sixty-one one-thousand-two-hundred-sixty-two one-thousand-two-hundred-sixty-three one-thousand-two-hundred-sixty-four one-thousand-two-hundred-sixty-five one-thousand-two-hundred-sixty-six one-thousand-two-hundred-sixty-seven one-thousand-two-hundred-sixty-eight one-thousand-two-hundred-sixty-nine one-thousand-two-hundred-seventy one-thousand-two-hundred-seventy-one one-thousand-two-hundred-seventy-two one-thousand-two-hundred-seventy-three one-thousand-two-hundred-seventy-four one-thousand-two-hundred-seventy-five one-thousand-two-hundred-seventy-six one-thousand-two-hundred-seventy-seven one-thousand-two-hundred-seventy-eight one-thousand-two-hundred-seventy-nine one-thousand-two-hundred-eighty one-thousand-two-hundred-eighty-one one-thousand-two-hundred-eighty-two one-thousand-two-hundred-eighty-three one-thousand-two-hundred-eighty-four one-thousand-two-hundred-eighty-five one-thousand-two-hundred-eighty-six one-thousand-two-hundred-eighty-seven one-thousand-two-hundred-eighty-eight one-thousand-two-hundred-eighty-nine one-thousand-two-hundred-ninety one-thousand-two-hundred-ninety-one one-thousand-two-hundred-ninety-two one-thousand-two-hundred-ninety-three one-thousand-two-hundred-ninety-four one-thousand-two-hundred-ninety-five one-thousand-two-hundred-ninety-six one-thousand-two-hundred-ninety-seven one-thousand-two-hundred-ninety-eight one-thousand-two-hundred-ninety-nine one-thousand-three-hundred one-thousand-three-hundred-one one-thousand-three-hundred-two one-thousand-three-hundred-three one-thousand-three-hundred-four one-thousand-three-hundred-five one-thousand-three-hundred-six one-thousand-three-hundred-seven one-thousand-three-hundred-eight one-thousand-three-hundred-nine one-thousand-three-hundred-ten one-thousand-three-hundred-eleven one-thousand-three-hundred-twelve one-thousand-three-hundred-thirteen one-thousand-three-hundred-fourteen one-thousand-three-hundred-fifteen one-thousand-three-hundred-sixteen one-thousand-three-hundred-seventeen one-thousand-three-hundred-eighteen one-thousand-three-hundred-nineteen one-thousand-three-hundred-twenty one-thousand-three-hundred-twenty-one one-thousand-three-hundred-twenty-two one-thousand-three-hundred-twenty-three one-thousand-three-hundred-twenty-four one-thousand-three-hundred-twenty-five one-thousand-three-hundred-twenty-six one-thousand-three-hundred-twenty-seven one-thousand-three-hundred-twenty-eight one-thousand-three-hundred-twenty-nine one-thousand-three-hundred-thirty one-thousand-three-hundred-thirty-one one-thousand-three-hundred-thirty-two one-thousand-three-hundred-thirty-three one-thousand-three-hundred-thirty-four one-thousand-three-hundred-thirty-five one-thousand-three-hundred-thirty-six one-thousand-three-hundred-thirty-seven one-thousand-three-hundred-thirty-eight one-thousand-three-hundred-thirty-nine one-thousand-three-hundred-forty one-thousand-three-hundred-forty-one one-thousand-three-hundred-forty-two one-thousand-three-hundred-forty-three one-thousand-three-hundred-forty-four one-thousand-three-hundred-forty-five one-thousand-three-hundred-forty-six one-thousand-three-hundred-forty-seven one-thousand-three-hundred-forty-eight one-thousand-three-hundred-forty-nine one-thousand-three-hundred-fifty one-thousand-three-hundred-fifty-one one-thousand-three-hundred-fifty-two one-thousand-three-hundred-fifty-three one-thousand-three-hundred-fifty-four one-thousand-three-hundred-fifty-five one-thousand-three-hundred-fifty-six one-thousand-three-hundred-fifty-seven one-thousand-three-hundred-fifty-eight one-thousand-three-hundred-fifty-nine one-thousand-three-hundred-sixty one-thousand-three-hundred-sixty-one one-thousand-three-hundred-sixty-two one-thousand-three-hundred-sixty-three one-thousand-three-hundred-sixty-four one-thousand-three-hundred-sixty-five one-thousand-three-hundred-sixty-six one-thousand-three-hundred-sixty-seven one-thousand-three-hundred-sixty-eight one-thousand-three-hundred-sixty-nine one-thousand-three-hundred-seventy one-thousand-three-hundred-seventy-one one-thousand-three-hundred-seventy-two one-thousand-three-hundred-seventy-three one-thousand-three-hundred-seventy-four one-thousand-three-hundred-seventy-five one-thousand-three-hundred-seventy-six one-thousand-three-hundred-seventy-seven one-thousand-three-hundred-seventy-eight one-thousand-three-hundred-seventy-nine one-thousand-three-hundred-eighty one-thousand-three-hundred-eighty-one one-thousand-three-hundred-eighty-two one-thousand-three-hundred-eighty-three one-thousand-three-hundred-eighty-four one-thousand-three-hundred-eighty-five one-thousand-three-hundred-eighty-six one-thousand-three-hundred-eighty-seven one-thousand-three-hundred-eighty-eight one-thousand-three-hundred-eighty-nine one-thousand-three-hundred-ninety one-thousand-three-hundred-ninety-one one-thousand-three-hundred-ninety-two one-thousand-three-hundred-ninety-three one-thousand-three-hundred-ninety-four one-thousand-three-hundred-ninety-five one-thousand-three-hundred-ninety-six one-thousand-three-hundred-ninety-seven one-thousand-three-hundred-ninety-eight one-thousand-three-hundred-ninety-nine one-thousand-four-hundred one-thousand-four-hundred-one one-thousand-four-hundred-two one-thousand-four-hundred-three one-thousand-four-hundred-four one-thousand-four-hundred-five one-thousand-four-hundred-six one-thousand-four-hundred-seven one-thousand-four-hundred-eight one-thousand-four-hundred-nine one-thousand-four-hundred-ten one-thousand-four-hundred-eleven one-thousand-four-hundred-twelve one-thousand-four-hundred-thirteen one-thousand-four-hundred-fourteen one-thousand-four-hundred-fifteen one-thousand-four-hundred-sixteen one-thousand-four-hundred-seventeen one-thousand-four-hundred-eighteen one-thousand-four-hundred-nineteen one-thousand-four-hundred-twenty one-thousand-four-hundred-twenty-one one-thousand-four-hundred-twenty-two one-thousand-four-hundred-twenty-three one-thousand-four-hundred-twenty-four one-thousand-four-hundred-twenty-five one-thousand-four-hundred-twenty-six one-thousand-four-hundred-twenty-seven one-thousand-four-hundred-twenty-eight one-thousand-four-hundred-twenty-nine one-thousand-four-hundred-thirty one-thousand-four-hundred-thirty-one one-thousand-four-hundred-thirty-two one-thousand-four-hundred-thirty-three one-thousand-four-hundred-thirty-four one-thousand-four-hundred-thirty-five one-thousand-four-hundred-thirty-six one-thousand-four-hundred-thirty-seven one-thousand-four-hundred-thirty-eight one-thousand-four-hundred-thirty-nine one-thousand-four-hundred-forty one-thousand-four-hundred-forty-one one-thousand-four-hundred-forty-two one-thousand-four-hundred-forty-three one-thousand-four-hundred-forty-four one-thousand-four-hundred-forty-five one-thousand-four-hundred-forty-six one-thousand-four-hundred-forty-seven one-thousand-four-hundred-forty-eight one-thousand-four-hundred-forty-nine one-thousand-four-hundred-fifty one-thousand-four-hundred-fifty-one one-thousand-four-hundred-fifty-two one-thousand-four-hundred-fifty-three one-thousand-four-hundred-fifty-four one-thousand-four-hundred-fifty-five one-thousand-four-hundred-fifty-six one-thousand-four-hundred-fifty-seven one-thousand-four-hundred-fifty-eight one-thousand-four-hundred-fifty-nine one-thousand-four-hundred-sixty one-thousand-four-hundred-sixty-one one-thousand-four-hundred-sixty-two one-thousand-four-hundred-sixty-three one-thousand-four-hundred-sixty-four one-thousand-four-hundred-sixty-five one-thousand-four-hundred-sixty-six one-thousand-four-hundred-sixty-seven one-thousand-four-hundred-sixty-eight one-thousand-four-hundred-sixty-nine one-thousand-four-hundred-seventy one-thousand-four-hundred-seventy-one one-thousand-four-hundred-seventy-two one-thousand-four-hundred-seventy-three one-thousand-four-hundred-seventy-four one-thousand-four-hundred-seventy-five one-thousand-four-hundred-seventy-six one-thousand-four-hundred-seventy-seven one-thousand-four-hundred-seventy-eight one-thousand-four-hundred-seventy-nine one-thousand-four-hundred-eighty one-thousand-four-hundred-eighty-one one-thousand-four-hundred-eighty-two one-thousand-four-hundred-eighty-three one-thousand-four-hundred-eighty-four one-thousand-four-hundred-eighty-five one-thousand-four-hundred-eighty-six one-thousand-four-hundred-eighty-seven one-thousand-four-hundred-eighty-eight one-thousand-four-hundred-eighty-nine one-thousand-four-hundred-ninety one-thousand-four-hundred-ninety-one one-thousand-four-hundred-ninety-two one-thousand-four-hundred-ninety-three one-thousand-four-hundred-ninety-four one-thousand-four-hundred-ninety-five one-thousand-four-hundred-ninety-six one-thousand-four-hundred-ninety-seven one-thousand-four-hundred-ninety-eight one-thousand-four-hundred-ninety-nine one-thousand-five-hundred one-thousand-five-hundred-one one-thousand-five-hundred-two one-thousand-five-hundred-three one-thousand-five-hundred-four one-thousand-five-hundred-five one-thousand-five-hundred-six one-thousand-five-hundred-seven one-thousand-five-hundred-eight one-thousand-five-hundred-nine one-thousand-five-hundred-ten one-thousand-five-hundred-eleven one-thousand-five-hundred-twelve one-thousand-five-hundred-thirteen one-thousand-five-hundred-fourteen one-thousand-five-hundred-fifteen one-thousand-five-hundred-sixteen one-thousand-five-hundred-seventeen one-thousand-five-hundred-eighteen one-thousand-five-hundred-nineteen one-thousand-five-hundred-twenty one-thousand-five-hundred-twenty-one one-thousand-five-hundred-twenty-two one-thousand-five-hundred-twenty-three one-thousand-five-hundred-twenty-four one-thousand-five-hundred-twenty-five one-thousand-five-hundred-twenty-six one-thousand-five-hundred-twenty-seven one-thousand-five-hundred-twenty-eight one-thousand-five-hundred-twenty-nine one-thousand-five-hundred-thirty one-thousand-five-hundred-thirty-one one-thousand-five-hundred-thirty-two one-thousand-five-hundred-thirty-three one-thousand-five-hundred-thirty-four one-thousand-five-hundred-thirty-five one-thousand-five-hundred-thirty-six one-thousand-five-hundred-thirty-seven one-thousand-five-hundred-thirty-eight one-thousand-five-hundred-thirty-nine one-thousand-five-hundred-forty one-thousand-five-hundred-forty-one one-thousand-five-hundred-forty-two one-thousand-five-hundred-forty-three one-thousand-five-hundred-forty-four one-thousand-five-hundred-forty-five one-thousand-five-hundred-forty-six one-thousand-five-hundred-forty-seven one-thousand-five-hundred-forty-eight one-thousand-five-hundred-forty-nine one-thousand-five-hundred-fifty one-thousand-five-hundred-fifty-one one-thousand-five-hundred-fifty-two one-thousand-five-hundred-fifty-three one-thousand-five-hundred-fifty-four one-thousand-five-hundred-fifty-five one-thousand-five-hundred-fifty-six one-thousand-five-hundred-fifty-seven one-thousand-five-hundred-fifty-eight one-thousand-five-hundred-fifty-nine one-thousand-five-hundred-sixty one-thousand-five-hundred-sixty-one one-thousand-five-hundred-sixty-two one-thousand-five-hundred-sixty-three one-thousand-five-hundred-sixty-four one-thousand-five-hundred-sixty-five one-thousand-five-hundred-sixty-six one-thousand-five-hundred-sixty-seven one-thousand-five-hundred-sixty-eight one-thousand-five-hundred-sixty-nine one-thousand-five-hundred-seventy one-thousand-five-hundred-seventy-one one-thousand-five-hundred-seventy-two one-thousand-five-hundred-seventy-three one-thousand-five-hundred-seventy-four one-thousand-five-hundred-seventy-five one-thousand-five-hundred-seventy-six one-thousand-five-hundred-seventy-seven one-thousand-five-hundred-seventy-eight one-thousand-five-hundred-seventy-nine one-thousand-five-hundred-eighty one-thousand-five-hundred-eighty-one one-thousand-five-hundred-eighty-two one-thousand-five-hundred-eighty-three one-thousand-five-hundred-eighty-four one-thousand-five-hundred-eighty-five one-thousand-five-hundred-eighty-six one-thousand-five-hundred-eighty-seven one-thousand-five-hundred-eighty-eight one-thousand-five-hundred-eighty-nine one-thousand-five-hundred-ninety one-thousand-five-hundred-ninety-one one-thousand-five-hundred-ninety-two one-thousand-five-hundred-ninety-three one-thousand-five-hundred-ninety-four one-thousand-five-hundred-ninety-five one-thousand-five-hundred-ninety-six one-thousand-five-hundred-ninety-seven one-thousand-five-hundred-ninety-eight one-thousand-five-hundred-ninety-nine one-thousand-six-hundred one-thousand-six-hundred-one one-thousand-six-hundred-two one-thousand-six-hundred-three one-thousand-six-hundred-four one-thousand-six-hundred-five one-thousand-six-hundred-six one-thousand-six-hundred-seven one-thousand-six-hundred-eight one-thousand-six-hundred-nine one-thousand-six-hundred-ten one-thousand-six-hundred-eleven one-thousand-six-hundred-twelve one-thousand-six-hundred-thirteen one-thousand-six-hundred-fourteen one-thousand-six-hundred-fifteen one-thousand-six-hundred-sixteen one-thousand-six-hundred-seventeen one-thousand-six-hundred-eighteen one-thousand-six-hundred-nineteen one-thousand-six-hundred-twenty one-thousand-six-hundred-twenty-one one-thousand-six-hundred-twenty-two one-thousand-six-hundred-twenty-three one-thousand-six-hundred-twenty-four one-thousand-six-hundred-twenty-five one-thousand-six-hundred-twenty-six one-thousand-six-hundred-twenty-seven one-thousand-six-hundred-twenty-eight one-thousand-six-hundred-twenty-nine one-thousand-six-hundred-thirty one-thousand-six-hundred-thirty-one one-thousand-six-hundred-thirty-two one-thousand-six-hundred-thirty-three one-thousand-six-hundred-thirty-four one-thousand-six-hundred-thirty-five one-thousand-six-hundred-thirty-six one-thousand-six-hundred-thirty-seven one-thousand-six-hundred-thirty-eight one-thousand-six-hundred-thirty-nine one-thousand-six-hundred-forty one-thousand-six-hundred-forty-one one-thousand-six-hundred-forty-two one-thousand-six-hundred-forty-three one-thousand-six-hundred-forty-four one-thousand-six-hundred-forty-five one-thousand-six-hundred-forty-six one-thousand-six-hundred-forty-seven one-thousand-six-hundred-forty-eight one-thousand-six-hundred-forty-nine one-thousand-six-hundred-fifty one-thousand-six-hundred-fifty-one one-thousand-six-hundred-fifty-two one-thousand-six-hundred-fifty-three one-thousand-six-hundred-fifty-four one-thousand-six-hundred-fifty-five one-thousand-six-hundred-fifty-six one-thousand-six-hundred-fifty-seven one-thousand-six-hundred-fifty-eight one-thousand-six-hundred-fifty-nine one-thousand-six-hundred-sixty one-thousand-six-hundred-sixty-one one-thousand-six-hundred-sixty-two one-thousand-six-hundred-sixty-three one-thousand-six-hundred-sixty-four one-thousand-six-hundred-sixty-five one-thousand-six-hundred-sixty-six one-thousand-six-hundred-sixty-seven one-thousand-six-hundred-sixty-eight one-thousand-six-hundred-sixty-nine one-thousand-six-hundred-seventy one-thousand-six-hundred-seventy-one one-thousand-six-hundred-seventy-two one-thousand-six-hundred-seventy-three one-thousand-six-hundred-seventy-four one-thousand-six-hundred-seventy-five one-thousand-six-hundred-seventy-six one-thousand-six-hundred-seventy-seven one-thousand-six-hundred-seventy-eight one-thousand-six-hundred-seventy-nine one-thousand-six-hundred-eighty one-thousand-six-hundred-eighty-one one-thousand-six-hundred-eighty-two one-thousand-six-hundred-eighty-three one-thousand-six-hundred-eighty-four one-thousand-six-hundred-eighty-five one-thousand-six-hundred-eighty-six one-thousand-six-hundred-eighty-seven one-thousand-six-hundred-eighty-eight one-thousand-six-hundred-eighty-nine one-thousand-six-hundred-ninety one-thousand-six-hundred-ninety-one one-thousand-six-hundred-ninety-two one-thousand-six-hundred-ninety-three one-thousand-six-hundred-ninety-four one-thousand-six-hundred-ninety-five one-thousand-six-hundred-ninety-six one-thousand-six-hundred-ninety-seven one-thousand-six-hundred-ninety-eight one-thousand-six-hundred-ninety-nine one-thousand-seven-hundred one-thousand-seven-hundred-one one-thousand-seven-hundred-two one-thousand-seven-hundred-three one-thousand-seven-hundred-four one-thousand-seven-hundred-five one-thousand-seven-hundred-six one-thousand-seven-hundred-seven one-thousand-seven-hundred-eight one-thousand-seven-hundred-nine one-thousand-seven-hundred-ten one-thousand-seven-hundred-eleven one-thousand-seven-hundred-twelve one-thousand-seven-hundred-thirteen one-thousand-seven-hundred-fourteen one-thousand-seven-hundred-fifteen one-thousand-seven-hundred-sixteen one-thousand-seven-hundred-seventeen one-thousand-seven-hundred-eighteen one-thousand-seven-hundred-nineteen one-thousand-seven-hundred-twenty one-thousand-seven-hundred-twenty-one one-thousand-seven-hundred-twenty-two one-thousand-seven-hundred-twenty-three one-thousand-seven-hundred-twenty-four one-thousand-seven-hundred-twenty-five one-thousand-seven-hundred-twenty-six one-thousand-seven-hundred-twenty-seven one-thousand-seven-hundred-twenty-eight one-thousand-seven-hundred-twenty-nine one-thousand-seven-hundred-thirty one-thousand-seven-hundred-thirty-one one-thousand-seven-hundred-thirty-two one-thousand-seven-hundred-thirty-three one-thousand-seven-hundred-thirty-four one-thousand-seven-hundred-thirty-five one-thousand-seven-hundred-thirty-six one-thousand-seven-hundred-thirty-seven one-thousand-seven-hundred-thirty-eight one-thousand-seven-hundred-thirty-nine one-thousand-seven-hundred-forty one-thousand-seven-hundred-forty-one one-thousand-seven-hundred-forty-two one-thousand-seven-hundred-forty-three one-thousand-seven-hundred-forty-four one-thousand-seven-hundred-forty-five one-thousand-seven-hundred-forty-six one-thousand-seven-hundred-forty-seven one-thousand-seven-hundred-forty-eight one-thousand-seven-hundred-forty-nine one-thousand-seven-hundred-fifty one-thousand-seven-hundred-fifty-one one-thousand-seven-hundred-fifty-two one-thousand-seven-hundred-fifty-three one-thousand-seven-hundred-fifty-four one-thousand-seven-hundred-fifty-five one-thousand-seven-hundred-fifty-six one-thousand-seven-hundred-fifty-seven one-thousand-seven-hundred-fifty-eight one-thousand-seven-hundred-fifty-nine one-thousand-seven-hundred-sixty one-thousand-seven-hundred-sixty-one one-thousand-seven-hundred-sixty-two one-thousand-seven-hundred-sixty-three one-thousand-seven-hundred-sixty-four one-thousand-seven-hundred-sixty-five one-thousand-seven-hundred-sixty-six one-thousand-seven-hundred-sixty-seven one-thousand-seven-hundred-sixty-eight one-thousand-seven-hundred-sixty-nine one-thousand-seven-hundred-seventy one-thousand-seven-hundred-seventy-one one-thousand-seven-hundred-seventy-two one-thousand-seven-hundred-seventy-three one-thousand-seven-hundred-seventy-four one-thousand-seven-hundred-seventy-five one-thousand-seven-hundred-seventy-six one-thousand-seven-hundred-seventy-seven one-thousand-seven-hundred-seventy-eight one-thousand-seven-hundred-seventy-nine one-thousand-seven-hundred-eighty one-thousand-seven-hundred-eighty-one one-thousand-seven-hundred-eighty-two one-thousand-seven-hundred-eighty-three one-thousand-seven-hundred-eighty-four one-thousand-seven-hundred-eighty-five one-thousand-seven-hundred-eighty-six one-thousand-seven-hundred-eighty-seven one-thousand-seven-hundred-eighty-eight one-thousand-seven-hundred-eighty-nine one-thousand-seven-hundred-ninety one-thousand-seven-hundred-ninety-one one-thousand-seven-hundred-ninety-two one-thousand-seven-hundred-ninety-three one-thousand-seven-hundred-ninety-four one-thousand-seven-hundred-ninety-five one-thousand-seven-hundred-ninety-six one-thousand-seven-hundred-ninety-seven one-thousand-seven-hundred-ninety-eight one-thousand-seven-hundred-ninety-nine one-thousand-eight-hundred one-thousand-eight-hundred-one one-thousand-eight-hundred-two one-thousand-eight-hundred-three one-thousand-eight-hundred-four one-thousand-eight-hundred-five one-thousand-eight-hundred-six one-thousand-eight-hundred-seven one-thousand-eight-hundred-eight one-thousand-eight-hundred-nine one-thousand-eight-hundred-ten one-thousand-eight-hundred-eleven one-thousand-eight-hundred-twelve one-thousand-eight-hundred-thirteen one-thousand-eight-hundred-fourteen one-thousand-eight-hundred-fifteen one-thousand-eight-hundred-sixteen one-thousand-eight-hundred-seventeen one-thousand-eight-hundred-eighteen one-thousand-eight-hundred-nineteen one-thousand-eight-hundred-twenty one-thousand-eight-hundred-twenty-one one-thousand-eight-hundred-twenty-two one-thousand-eight-hundred-twenty-three one-thousand-eight-hundred-twenty-four one-thousand-eight-hundred-twenty-five one-thousand-eight-hundred-twenty-six one-thousand-eight-hundred-twenty-seven one-thousand-eight-hundred-twenty-eight one-thousand-eight-hundred-twenty-nine one-thousand-eight-hundred-thirty one-thousand-eight-hundred-thirty-one one-thousand-eight-hundred-thirty-two one-thousand-eight-hundred-thirty-three one-thousand-eight-hundred-thirty-four one-thousand-eight-hundred-thirty-five one-thousand-eight-hundred-thirty-six one-thousand-eight-hundred-thirty-seven one-thousand-eight-hundred-thirty-eight one-thousand-eight-hundred-thirty-nine one-thousand-eight-hundred-forty one-thousand-eight-hundred-forty-one one-thousand-eight-hundred-forty-two one-thousand-eight-hundred-forty-three one-thousand-eight-hundred-forty-four one-thousand-eight-hundred-forty-five one-thousand-eight-hundred-forty-six one-thousand-eight-hundred-forty-seven one-thousand-eight-hundred-forty-eight one-thousand-eight-hundred-forty-nine one-thousand-eight-hundred-fifty one-thousand-eight-hundred-fifty-one one-thousand-eight-hundred-fifty-two one-thousand-eight-hundred-fifty-three one-thousand-eight-hundred-fifty-four one-thousand-eight-hundred-fifty-five one-thousand-eight-hundred-fifty-six one-thousand-eight-hundred-fifty-seven one-thousand-eight-hundred-fifty-eight one-thousand-eight-hundred-fifty-nine one-thousand-eight-hundred-sixty one-thousand-eight-hundred-sixty-one one-thousand-eight-hundred-sixty-two one-thousand-eight-hundred-sixty-three one-thousand-eight-hundred-sixty-four one-thousand-eight-hundred-sixty-five one-thousand-eight-hundred-sixty-six one-thousand-eight-hundred-sixty-seven one-thousand-eight-hundred-sixty-eight one-thousand-eight-hundred-sixty-nine one-thousand-eight-hundred-seventy one-thousand-eight-hundred-seventy-one one-thousand-eight-hundred-seventy-two one-thousand-eight-hundred-seventy-three one-thousand-eight-hundred-seventy-four one-thousand-eight-hundred-seventy-five one-thousand-eight-hundred-seventy-six one-thousand-eight-hundred-seventy-seven one-thousand-eight-hundred-seventy-eight one-thousand-eight-hundred-seventy-nine one-thousand-eight-hundred-eighty one-thousand-eight-hundred-eighty-one one-thousand-eight-hundred-eighty-two one-thousand-eight-hundred-eighty-three one-thousand-eight-hundred-eighty-four one-thousand-eight-hundred-eighty-five one-thousand-eight-hundred-eighty-six one-thousand-eight-hundred-eighty-seven one-thousand-eight-hundred-eighty-eight one-thousand-eight-hundred-eighty-nine one-thousand-eight-hundred-ninety one-thousand-eight-hundred-ninety-one one-thousand-eight-hundred-ninety-two one-thousand-eight-hundred-ninety-three one-thousand-eight-hundred-ninety-four one-thousand-eight-hundred-ninety-five one-thousand-eight-hundred-ninety-six one-thousand-eight-hundred-ninety-seven one-thousand-eight-hundred-ninety-eight one-thousand-eight-hundred-ninety-nine one-thousand-nine-hundred one-thousand-nine-hundred-one one-thousand-nine-hundred-two one-thousand-nine-hundred-three one-thousand-nine-hundred-four one-thousand-nine-hundred-five one-thousand-nine-hundred-six one-thousand-nine-hundred-seven one-thousand-nine-hundred-eight one-thousand-nine-hundred-nine one-thousand-nine-hundred-ten one-thousand-nine-hundred-eleven one-thousand-nine-hundred-twelve one-thousand-nine-hundred-thirteen one-thousand-nine-hundred-fourteen one-thousand-nine-hundred-fifteen one-thousand-nine-hundred-sixteen one-thousand-nine-hundred-seventeen one-thousand-nine-hundred-eighteen one-thousand-nine-hundred-nineteen one-thousand-nine-hundred-twenty one-thousand-nine-hundred-twenty-one one-thousand-nine-hundred-twenty-two one-thousand-nine-hundred-twenty-three one-thousand-nine-hundred-twenty-four one-thousand-nine-hundred-twenty-five one-thousand-nine-hundred-twenty-six one-thousand-nine-hundred-twenty-seven one-thousand-nine-hundred-twenty-eight one-thousand-nine-hundred-twenty-nine one-thousand-nine-hundred-thirty one-thousand-nine-hundred-thirty-one one-thousand-nine-hundred-thirty-two one-thousand-nine-hundred-thirty-three one-thousand-nine-hundred-thirty-four one-thousand-nine-hundred-thirty-five one-thousand-nine-hundred-thirty-six one-thousand-nine-hundred-thirty-seven one-thousand-nine-hundred-thirty-eight one-thousand-nine-hundred-thirty-nine one-thousand-nine-hundred-forty one-thousand-nine-hundred-forty-one one-thousand-nine-hundred-forty-two one-thousand-nine-hundred-forty-three one-thousand-nine-hundred-forty-four one-thousand-nine-hundred-forty-five one-thousand-nine-hundred-forty-six one-thousand-nine-hundred-forty-seven one-thousand-nine-hundred-forty-eight one-thousand-nine-hundred-forty-nine one-thousand-nine-hundred-fifty one-thousand-nine-hundred-fifty-one one-thousand-nine-hundred-fifty-two one-thousand-nine-hundred-fifty-three one-thousand-nine-hundred-fifty-four one-thousand-nine-hundred-fifty-five one-thousand-nine-hundred-fifty-six one-thousand-nine-hundred-fifty-seven one-thousand-nine-hundred-fifty-eight one-thousand-nine-hundred-fifty-nine one-thousand-nine-hundred-sixty one-thousand-nine-hundred-sixty-one one-thousand-nine-hundred-sixty-two one-thousand-nine-hundred-sixty-three one-thousand-nine-hundred-sixty-four one-thousand-nine-hundred-sixty-five one-thousand-nine-hundred-sixty-six one-thousand-nine-hundred-sixty-seven one-thousand-nine-hundred-sixty-eight one-thousand-nine-hundred-sixty-nine one-thousand-nine-hundred-seventy one-thousand-nine-hundred-seventy-one one-thousand-nine-hundred-seventy-two one-thousand-nine-hundred-seventy-three one-thousand-nine-hundred-seventy-four one-thousand-nine-hundred-seventy-five one-thousand-nine-hundred-seventy-six one-thousand-nine-hundred-seventy-seven one-thousand-nine-hundred-seventy-eight one-thousand-nine-hundred-seventy-nine one-thousand-nine-hundred-eighty one-thousand-nine-hundred-eighty-one one-thousand-nine-hundred-eighty-two one-thousand-nine-hundred-eighty-three one-thousand-nine-hundred-eighty-four one-thousand-nine-hundred-eighty-five one-thousand-nine-hundred-eighty-six one-thousand-nine-hundred-eighty-seven one-thousand-nine-hundred-eighty-eight one-thousand-nine-hundred-eighty-nine one-thousand-nine-hundred-ninety one-thousand-nine-hundred-ninety-one one-thousand-nine-hundred-ninety-two one-thousand-nine-hundred-ninety-three one-thousand-nine-hundred-ninety-four one-thousand-nine-hundred-ninety-five one-thousand-nine-hundred-ninety-six one-thousand-nine-hundred-ninety-seven one-thousand-nine-hundred-ninety-eight one-thousand-nine-hundred-ninety-nine two-thousand two-thousand-one two-thousand-two two-thousand-three two-thousand-four two-thousand-five two-thousand-six two-thousand-seven two-thousand-eight two-thousand-nine two-thousand-ten two-thousand-eleven two-thousand-twelve two-thousand-thirteen two-thousand-fourteen two-thousand-fifteen two-thousand-sixteen two-thousand-seventeen two-thousand-eighteen two-thousand-nineteen two-thousand-twenty two-thousand-twenty-one two-thousand-twenty-two two-thousand-twenty-three two-thousand-twenty-four two-thousand-twenty-five two-thousand-twenty-six two-thousand-twenty-seven two-thousand-twenty-eight two-thousand-twenty-nine two-thousand-thirty two-thousand-thirty-one two-thousand-thirty-two two-thousand-thirty-three two-thousand-thirty-four two-thousand-thirty-five two-thousand-thirty-six two-thousand-thirty-seven two-thousand-thirty-eight two-thousand-thirty-nine two-thousand-forty two-thousand-forty-one two-thousand-forty-two two-thousand-forty-three two-thousand-forty-four two-thousand-forty-five two-thousand-forty-six two-thousand-forty-seven two-thousand-forty-eight two-thousand-forty-nine two-thousand-fifty two-thousand-fifty-one two-thousand-fifty-two two-thousand-fifty-three two-thousand-fifty-four two-thousand-fifty-five two-thousand-fifty-six two-thousand-fifty-seven two-thousand-fifty-eight two-thousand-fifty-nine two-thousand-sixty two-thousand-sixty-one two-thousand-sixty-two two-thousand-sixty-three two-thousand-sixty-four two-thousand-sixty-five two-thousand-sixty-six two-thousand-sixty-seven two-thousand-sixty-eight two-thousand-sixty-nine two-thousand-seventy two-thousand-seventy-one two-thousand-seventy-two two-thousand-seventy-three two-thousand-seventy-four two-thousand-seventy-five two-thousand-seventy-six two-thousand-seventy-seven two-thousand-seventy-eight two-thousand-seventy-nine two-thousand-eighty two-thousand-eighty-one two-thousand-eighty-two two-thousand-eighty-three two-thousand-eighty-four two-thousand-eighty-five two-thousand-eighty-six two-thousand-eighty-seven two-thousand-eighty-eight two-thousand-eighty-nine two-thousand-ninety two-thousand-ninety-one two-thousand-ninety-two two-thousand-ninety-three two-thousand-ninety-four two-thousand-ninety-five two-thousand-ninety-six two-thousand-ninety-seven two-thousand-ninety-eight two-thousand-ninety-nine two-thousand-one-hundred two-thousand-one-hundred-one two-thousand-one-hundred-two two-thousand-one-hundred-three two-thousand-one-hundred-four two-thousand-one-hundred-five two-thousand-one-hundred-six two-thousand-one-hundred-seven two-thousand-one-hundred-eight two-thousand-one-hundred-nine two-thousand-one-hundred-ten two-thousand-one-hundred-eleven two-thousand-one-hundred-twelve two-thousand-one-hundred-thirteen two-thousand-one-hundred-fourteen two-thousand-one-hundred-fifteen two-thousand-one-hundred-sixteen two-thousand-one-hundred-seventeen two-thousand-one-hundred-eighteen two-thousand-one-hundred-nineteen two-thousand-one-hundred-twenty two-thousand-one-hundred-twenty-one two-thousand-one-hundred-twenty-two two-thousand-one-hundred-twenty-three two-thousand-one-hundred-twenty-four two-thousand-one-hundred-twenty-five two-thousand-one-hundred-twenty-six two-thousand-one-hundred-twenty-seven two-thousand-one-hundred-twenty-eight two-thousand-one-hundred-twenty-nine two-thousand-one-hundred-thirty two-thousand-one-hundred-thirty-one two-thousand-one-hundred-thirty-two two-thousand-one-hundred-thirty-three two-thousand-one-hundred-thirty-four two-thousand-one-hundred-thirty-five two-thousand-one-hundred-thirty-six two-thousand-one-hundred-thirty-seven two-thousand-one-hundred-thirty-eight two-thousand-one-hundred-thirty-nine two-thousand-one-hundred-forty two-thousand-one-hundred-forty-one two-thousand-one-hundred-forty-two two-thousand-one-hundred-forty-three two-thousand-one-hundred-forty-four two-thousand-one-hundred-forty-five two-thousand-one-hundred-forty-six two-thousand-one-hundred-forty-seven two-thousand-one-hundred-forty-eight two-thousand-one-hundred-forty-nine two-thousand-one-hundred-fifty two-thousand-one-hundred-fifty-one two-thousand-one-hundred-fifty-two two-thousand-one-hundred-fifty-three two-thousand-one-hundred-fifty-four two-thousand-one-hundred-fifty-five two-thousand-one-hundred-fifty-six two-thousand-one-hundred-fifty-seven two-thousand-one-hundred-fifty-eight two-thousand-one-hundred-fifty-nine two-thousand-one-hundred-sixty two-thousand-one-hundred-sixty-one two-thousand-one-hundred-sixty-two two-thousand-one-hundred-sixty-three two-thousand-one-hundred-sixty-four two-thousand-one-hundred-sixty-five two-thousand-one-hundred-sixty-six two-thousand-one-hundred-sixty-seven two-thousand-one-hundred-sixty-eight two-thousand-one-hundred-sixty-nine two-thousand-one-hundred-seventy two-thousand-one-hundred-seventy-one two-thousand-one-hundred-seventy-two two-thousand-one-hundred-seventy-three two-thousand-one-hundred-seventy-four two-thousand-one-hundred-seventy-five two-thousand-one-hundred-seventy-six two-thousand-one-hundred-seventy-seven two-thousand-one-hundred-seventy-eight two-thousand-one-hundred-seventy-nine two-thousand-one-hundred-eighty two-thousand-one-hundred-eighty-one two-thousand-one-hundred-eighty-two two-thousand-one-hundred-eighty-three two-thousand-one-hundred-eighty-four two-thousand-one-hundred-eighty-five two-thousand-one-hundred-eighty-six two-thousand-one-hundred-eighty-seven two-thousand-one-hundred-eighty-eight two-thousand-one-hundred-eighty-nine two-thousand-one-hundred-ninety two-thousand-one-hundred-ninety-one two-thousand-one-hundred-ninety-two two-thousand-one-hundred-ninety-three two-thousand-one-hundred-ninety-four two-thousand-one-hundred-ninety-five two-thousand-one-hundred-ninety-six two-thousand-one-hundred-ninety-seven two-thousand-one-hundred-ninety-eight two-thousand-one-hundred-ninety-nine two-thousand-two-hundred two-thousand-two-hundred-one two-thousand-two-hundred-two two-thousand-two-hundred-three two-thousand-two-hundred-four two-thousand-two-hundred-five two-thousand-two-hundred-six two-thousand-two-hundred-seven two-thousand-two-hundred-eight two-thousand-two-hundred-nine two-thousand-two-hundred-ten two-thousand-two-hundred-eleven two-thousand-two-hundred-twelve two-thousand-two-hundred-thirteen two-thousand-two-hundred-fourteen two-thousand-two-hundred-fifteen two-thousand-two-hundred-sixteen two-thousand-two-hundred-seventeen two-thousand-two-hundred-eighteen two-thousand-two-hundred-nineteen two-thousand-two-hundred-twenty two-thousand-two-hundred-twenty-one two-thousand-two-hundred-twenty-two two-thousand-two-hundred-twenty-three two-thousand-two-hundred-twenty-four two-thousand-two-hundred-twenty-five two-thousand-two-hundred-twenty-six two-thousand-two-hundred-twenty-seven two-thousand-two-hundred-twenty-eight two-thousand-two-hundred-twenty-nine two-thousand-two-hundred-thirty two-thousand-two-hundred-thirty-one two-thousand-two-hundred-thirty-two two-thousand-two-hundred-thirty-three two-thousand-two-hundred-thirty-four two-thousand-two-hundred-thirty-five two-thousand-two-hundred-thirty-six two-thousand-two-hundred-thirty-seven two-thousand-two-hundred-thirty-eight two-thousand-two-hundred-thirty-nine two-thousand-two-hundred-forty two-thousand-two-hundred-forty-one two-thousand-two-hundred-forty-two two-thousand-two-hundred-forty-three two-thousand-two-hundred-forty-four two-thousand-two-hundred-forty-five two-thousand-two-hundred-forty-six two-thousand-two-hundred-forty-seven two-thousand-two-hundred-forty-eight two-thousand-two-hundred-forty-nine two-thousand-two-hundred-fifty two-thousand-two-hundred-fifty-one two-thousand-two-hundred-fifty-two two-thousand-two-hundred-fifty-three two-thousand-two-hundred-fifty-four two-thousand-two-hundred-fifty-five two-thousand-two-hundred-fifty-six two-thousand-two-hundred-fifty-seven two-thousand-two-hundred-fifty-eight two-thousand-two-hundred-fifty-nine two-thousand-two-hundred-sixty two-thousand-two-hundred-sixty-one two-thousand-two-hundred-sixty-two two-thousand-two-hundred-sixty-three two-thousand-two-hundred-sixty-four two-thousand-two-hundred-sixty-five two-thousand-two-hundred-sixty-six two-thousand-two-hundred-sixty-seven two-thousand-two-hundred-sixty-eight two-thousand-two-hundred-sixty-nine two-thousand-two-hundred-seventy two-thousand-two-hundred-seventy-one two-thousand-two-hundred-seventy-two two-thousand-two-hundred-seventy-three two-thousand-two-hundred-seventy-four two-thousand-two-hundred-seventy-five two-thousand-two-hundred-seventy-six two-thousand-two-hundred-seventy-seven two-thousand-two-hundred-seventy-eight two-thousand-two-hundred-seventy-nine two-thousand-two-hundred-eighty two-thousand-two-hundred-eighty-one two-thousand-two-hundred-eighty-two two-thousand-two-hundred-eighty-three two-thousand-two-hundred-eighty-four two-thousand-two-hundred-eighty-five two-thousand-two-hundred-eighty-six two-thousand-two-hundred-eighty-seven two-thousand-two-hundred-eighty-eight two-thousand-two-hundred-eighty-nine two-thousand-two-hundred-ninety two-thousand-two-hundred-ninety-one two-thousand-two-hundred-ninety-two two-thousand-two-hundred-ninety-three two-thousand-two-hundred-ninety-four two-thousand-two-hundred-ninety-five two-thousand-two-hundred-ninety-six two-thousand-two-hundred-ninety-seven two-thousand-two-hundred-ninety-eight two-thousand-two-hundred-ninety-nine two-thousand-three-hundred two-thousand-three-hundred-one two-thousand-three-hundred-two two-thousand-three-hundred-three two-thousand-three-hundred-four two-thousand-three-hundred-five two-thousand-three-hundred-six two-thousand-three-hundred-seven two-thousand-three-hundred-eight two-thousand-three-hundred-nine two-thousand-three-hundred-ten two-thousand-three-hundred-eleven two-thousand-three-hundred-twelve two-thousand-three-hundred-thirteen two-thousand-three-hundred-fourteen two-thousand-three-hundred-fifteen two-thousand-three-hundred-sixteen two-thousand-three-hundred-seventeen two-thousand-three-hundred-eighteen two-thousand-three-hundred-nineteen two-thousand-three-hundred-twenty two-thousand-three-hundred-twenty-one two-thousand-three-hundred-twenty-two two-thousand-three-hundred-twenty-three two-thousand-three-hundred-twenty-four two-thousand-three-hundred-twenty-five two-thousand-three-hundred-twenty-six two-thousand-three-hundred-twenty-seven two-thousand-three-hundred-twenty-eight two-thousand-three-hundred-twenty-nine two-thousand-three-hundred-thirty two-thousand-three-hundred-thirty-one two-thousand-three-hundred-thirty-two two-thousand-three-hundred-thirty-three two-thousand-three-hundred-thirty-four two-thousand-three-hundred-thirty-five two-thousand-three-hundred-thirty-six two-thousand-three-hundred-thirty-seven two-thousand-three-hundred-thirty-eight two-thousand-three-hundred-thirty-nine two-thousand-three-hundred-forty two-thousand-three-hundred-forty-one two-thousand-three-hundred-forty-two two-thousand-three-hundred-forty-three two-thousand-three-hundred-forty-four two-thousand-three-hundred-forty-five two-thousand-three-hundred-forty-six two-thousand-three-hundred-forty-seven two-thousand-three-hundred-forty-eight two-thousand-three-hundred-forty-nine two-thousand-three-hundred-fifty two-thousand-three-hundred-fifty-one two-thousand-three-hundred-fifty-two two-thousand-three-hundred-fifty-three two-thousand-three-hundred-fifty-four two-thousand-three-hundred-fifty-five two-thousand-three-hundred-fifty-six two-thousand-three-hundred-fifty-seven two-thousand-three-hundred-fifty-eight two-thousand-three-hundred-fifty-nine two-thousand-three-hundred-sixty two-thousand-three-hundred-sixty-one two-thousand-three-hundred-sixty-two two-thousand-three-hundred-sixty-three two-thousand-three-hundred-sixty-four two-thousand-three-hundred-sixty-five two-thousand-three-hundred-sixty-six two-thousand-three-hundred-sixty-seven two-thousand-three-hundred-sixty-eight two-thousand-three-hundred-sixty-nine two-thousand-three-hundred-seventy two-thousand-three-hundred-seventy-one two-thousand-three-hundred-seventy-two two-thousand-three-hundred-seventy-three two-thousand-three-hundred-seventy-four two-thousand-three-hundred-seventy-five two-thousand-three-hundred-seventy-six two-thousand-three-hundred-seventy-seven two-thousand-three-hundred-seventy-eight two-thousand-three-hundred-seventy-nine two-thousand-three-hundred-eighty two-thousand-three-hundred-eighty-one two-thousand-three-hundred-eighty-two two-thousand-three-hundred-eighty-three two-thousand-three-hundred-eighty-four two-thousand-three-hundred-eighty-five two-thousand-three-hundred-eighty-six two-thousand-three-hundred-eighty-seven two-thousand-three-hundred-eighty-eight two-thousand-three-hundred-eighty-nine two-thousand-three-hundred-ninety two-thousand-three-hundred-ninety-one two-thousand-three-hundred-ninety-two two-thousand-three-hundred-ninety-three two-thousand-three-hundred-ninety-four two-thousand-three-hundred-ninety-five two-thousand-three-hundred-ninety-six two-thousand-three-hundred-ninety-seven two-thousand-three-hundred-ninety-eight two-thousand-three-hundred-ninety-nine two-thousand-four-hundred two-thousand-four-hundred-one two-thousand-four-hundred-two two-thousand-four-hundred-three two-thousand-four-hundred-four two-thousand-four-hundred-five two-thousand-four-hundred-six two-thousand-four-hundred-seven two-thousand-four-hundred-eight two-thousand-four-hundred-nine two-thousand-four-hundred-ten two-thousand-four-hundred-eleven two-thousand-four-hundred-twelve two-thousand-four-hundred-thirteen two-thousand-four-hundred-fourteen two-thousand-four-hundred-fifteen two-thousand-four-hundred-sixteen two-thousand-four-hundred-seventeen two-thousand-four-hundred-eighteen two-thousand-four-hundred-nineteen two-thousand-four-hundred-twenty two-thousand-four-hundred-twenty-one two-thousand-four-hundred-twenty-two two-thousand-four-hundred-twenty-three two-thousand-four-hundred-twenty-four two-thousand-four-hundred-twenty-five two-thousand-four-hundred-twenty-six two-thousand-four-hundred-twenty-seven two-thousand-four-hundred-twenty-eight two-thousand-four-hundred-twenty-nine two-thousand-four-hundred-thirty two-thousand-four-hundred-thirty-one two-thousand-four-hundred-thirty-two two-thousand-four-hundred-thirty-three two-thousand-four-hundred-thirty-four two-thousand-four-hundred-thirty-five two-thousand-four-hundred-thirty-six two-thousand-four-hundred-thirty-seven two-thousand-four-hundred-thirty-eight two-thousand-four-hundred-thirty-nine two-thousand-four-hundred-forty two-thousand-four-hundred-forty-one two-thousand-four-hundred-forty-two two-thousand-four-hundred-forty-three two-thousand-four-hundred-forty-four two-thousand-four-hundred-forty-five two-thousand-four-hundred-forty-six two-thousand-four-hundred-forty-seven two-thousand-four-hundred-forty-eight two-thousand-four-hundred-forty-nine two-thousand-four-hundred-fifty two-thousand-four-hundred-fifty-one two-thousand-four-hundred-fifty-two two-thousand-four-hundred-fifty-three two-thousand-four-hundred-fifty-four two-thousand-four-hundred-fifty-five two-thousand-four-hundred-fifty-six two-thousand-four-hundred-fifty-seven two-thousand-four-hundred-fifty-eight two-thousand-four-hundred-fifty-nine two-thousand-four-hundred-sixty two-thousand-four-hundred-sixty-one two-thousand-four-hundred-sixty-two two-thousand-four-hundred-sixty-three two-thousand-four-hundred-sixty-four two-thousand-four-hundred-sixty-five two-thousand-four-hundred-sixty-six two-thousand-four-hundred-sixty-seven two-thousand-four-hundred-sixty-eight two-thousand-four-hundred-sixty-nine two-thousand-four-hundred-seventy two-thousand-four-hundred-seventy-one two-thousand-four-hundred-seventy-two two-thousand-four-hundred-seventy-three two-thousand-four-hundred-seventy-four two-thousand-four-hundred-seventy-five two-thousand-four-hundred-seventy-six two-thousand-four-hundred-seventy-seven two-thousand-four-hundred-seventy-eight two-thousand-four-hundred-seventy-nine two-thousand-four-hundred-eighty two-thousand-four-hundred-eighty-one two-thousand-four-hundred-eighty-two two-thousand-four-hundred-eighty-three two-thousand-four-hundred-eighty-four two-thousand-four-hundred-eighty-five two-thousand-four-hundred-eighty-six two-thousand-four-hundred-eighty-seven two-thousand-four-hundred-eighty-eight two-thousand-four-hundred-eighty-nine two-thousand-four-hundred-ninety two-thousand-four-hundred-ninety-one two-thousand-four-hundred-ninety-two two-thousand-four-hundred-ninety-three two-thousand-four-hundred-ninety-four two-thousand-four-hundred-ninety-five two-thousand-four-hundred-ninety-six two-thousand-four-hundred-ninety-seven two-thousand-four-hundred-ninety-eight two-thousand-four-hundred-ninety-nine two-thousand-five-hundred two-thousand-five-hundred-one two-thousand-five-hundred-two two-thousand-five-hundred-three two-thousand-five-hundred-four two-thousand-five-hundred-five two-thousand-five-hundred-six two-thousand-five-hundred-seven two-thousand-five-hundred-eight two-thousand-five-hundred-nine two-thousand-five-hundred-ten two-thousand-five-hundred-eleven two-thousand-five-hundred-twelve two-thousand-five-hundred-thirteen two-thousand-five-hundred-fourteen two-thousand-five-hundred-fifteen two-thousand-five-hundred-sixteen two-thousand-five-hundred-seventeen two-thousand-five-hundred-eighteen two-thousand-five-hundred-nineteen two-thousand-five-hundred-twenty two-thousand-five-hundred-twenty-one two-thousand-five-hundred-twenty-two two-thousand-five-hundred-twenty-three two-thousand-five-hundred-twenty-four two-thousand-five-hundred-twenty-five two-thousand-five-hundred-twenty-six two-thousand-five-hundred-twenty-seven two-thousand-five-hundred-twenty-eight two-thousand-five-hundred-twenty-nine two-thousand-five-hundred-thirty two-thousand-five-hundred-thirty-one two-thousand-five-hundred-thirty-two two-thousand-five-hundred-thirty-three two-thousand-five-hundred-thirty-four two-thousand-five-hundred-thirty-five two-thousand-five-hundred-thirty-six two-thousand-five-hundred-thirty-seven two-thousand-five-hundred-thirty-eight two-thousand-five-hundred-thirty-nine two-thousand-five-hundred-forty two-thousand-five-hundred-forty-one two-thousand-five-hundred-forty-two two-thousand-five-hundred-forty-three two-thousand-five-hundred-forty-four two-thousand-five-hundred-forty-five two-thousand-five-hundred-forty-six two-thousand-five-hundred-forty-seven two-thousand-five-hundred-forty-eight two-thousand-five-hundred-forty-nine two-thousand-five-hundred-fifty two-thousand-five-hundred-fifty-one two-thousand-five-hundred-fifty-two two-thousand-five-hundred-fifty-three two-thousand-five-hundred-fifty-four two-thousand-five-hundred-fifty-five two-thousand-five-hundred-fifty-six two-thousand-five-hundred-fifty-seven two-thousand-five-hundred-fifty-eight two-thousand-five-hundred-fifty-nine two-thousand-five-hundred-sixty two-thousand-five-hundred-sixty-one two-thousand-five-hundred-sixty-two two-thousand-five-hundred-sixty-three two-thousand-five-hundred-sixty-four two-thousand-five-hundred-sixty-five two-thousand-five-hundred-sixty-six two-thousand-five-hundred-sixty-seven two-thousand-five-hundred-sixty-eight two-thousand-five-hundred-sixty-nine two-thousand-five-hundred-seventy two-thousand-five-hundred-seventy-one two-thousand-five-hundred-seventy-two two-thousand-five-hundred-seventy-three two-thousand-five-hundred-seventy-four two-thousand-five-hundred-seventy-five two-thousand-five-hundred-seventy-six two-thousand-five-hundred-seventy-seven two-thousand-five-hundred-seventy-eight two-thousand-five-hundred-seventy-nine two-thousand-five-hundred-eighty two-thousand-five-hundred-eighty-one two-thousand-five-hundred-eighty-two two-thousand-five-hundred-eighty-three two-thousand-five-hundred-eighty-four two-thousand-five-hundred-eighty-five two-thousand-five-hundred-eighty-six two-thousand-five-hundred-eighty-seven two-thousand-five-hundred-eighty-eight two-thousand-five-hundred-eighty-nine two-thousand-five-hundred-ninety two-thousand-five-hundred-ninety-one two-thousand-five-hundred-ninety-two two-thousand-five-hundred-ninety-three two-thousand-five-hundred-ninety-four two-thousand-five-hundred-ninety-five two-thousand-five-hundred-ninety-six two-thousand-five-hundred-ninety-seven two-thousand-five-hundred-ninety-eight two-thousand-five-hundred-ninety-nine two-thousand-six-hundred two-thousand-six-hundred-one two-thousand-six-hundred-two two-thousand-six-hundred-three two-thousand-six-hundred-four two-thousand-six-hundred-five two-thousand-six-hundred-six two-thousand-six-hundred-seven two-thousand-six-hundred-eight two-thousand-six-hundred-nine two-thousand-six-hundred-ten two-thousand-six-hundred-eleven two-thousand-six-hundred-twelve two-thousand-six-hundred-thirteen two-thousand-six-hundred-fourteen two-thousand-six-hundred-fifteen two-thousand-six-hundred-sixteen two-thousand-six-hundred-seventeen two-thousand-six-hundred-eighteen two-thousand-six-hundred-nineteen two-thousand-six-hundred-twenty two-thousand-six-hundred-twenty-one two-thousand-six-hundred-twenty-two two-thousand-six-hundred-twenty-three two-thousand-six-hundred-twenty-four two-thousand-six-hundred-twenty-five two-thousand-six-hundred-twenty-six two-thousand-six-hundred-twenty-seven two-thousand-six-hundred-twenty-eight two-thousand-six-hundred-twenty-nine two-thousand-six-hundred-thirty two-thousand-six-hundred-thirty-one two-thousand-six-hundred-thirty-two two-thousand-six-hundred-thirty-three two-thousand-six-hundred-thirty-four two-thousand-six-hundred-thirty-five two-thousand-six-hundred-thirty-six two-thousand-six-hundred-thirty-seven two-thousand-six-hundred-thirty-eight two-thousand-six-hundred-thirty-nine two-thousand-six-hundred-forty two-thousand-six-hundred-forty-one two-thousand-six-hundred-forty-two two-thousand-six-hundred-forty-three two-thousand-six-hundred-forty-four two-thousand-six-hundred-forty-five two-thousand-six-hundred-forty-six two-thousand-six-hundred-forty-seven two-thousand-six-hundred-forty-eight two-thousand-six-hundred-forty-nine two-thousand-six-hundred-fifty two-thousand-six-hundred-fifty-one two-thousand-six-hundred-fifty-two two-thousand-six-hundred-fifty-three two-thousand-six-hundred-fifty-four two-thousand-six-hundred-fifty-five two-thousand-six-hundred-fifty-six two-thousand-six-hundred-fifty-seven two-thousand-six-hundred-fifty-eight two-thousand-six-hundred-fifty-nine two-thousand-six-hundred-sixty two-thousand-six-hundred-sixty-one two-thousand-six-hundred-sixty-two two-thousand-six-hundred-sixty-three two-thousand-six-hundred-sixty-four two-thousand-six-hundred-sixty-five two-thousand-six-hundred-sixty-six two-thousand-six-hundred-sixty-seven two-thousand-six-hundred-sixty-eight two-thousand-six-hundred-sixty-nine two-thousand-six-hundred-seventy two-thousand-six-hundred-seventy-one two-thousand-six-hundred-seventy-two two-thousand-six-hundred-seventy-three two-thousand-six-hundred-seventy-four two-thousand-six-hundred-seventy-five two-thousand-six-hundred-seventy-six two-thousand-six-hundred-seventy-seven two-thousand-six-hundred-seventy-eight two-thousand-six-hundred-seventy-nine two-thousand-six-hundred-eighty two-thousand-six-hundred-eighty-one two-thousand-six-hundred-eighty-two two-thousand-six-hundred-eighty-three two-thousand-six-hundred-eighty-four two-thousand-six-hundred-eighty-five two-thousand-six-hundred-eighty-six two-thousand-six-hundred-eighty-seven two-thousand-six-hundred-eighty-eight two-thousand-six-hundred-eighty-nine two-thousand-six-hundred-ninety two-thousand-six-hundred-ninety-one two-thousand-six-hundred-ninety-two two-thousand-six-hundred-ninety-three two-thousand-six-hundred-ninety-four two-thousand-six-hundred-ninety-five two-thousand-six-hundred-ninety-six two-thousand-six-hundred-ninety-seven two-thousand-six-hundred-ninety-eight two-thousand-six-hundred-ninety-nine two-thousand-seven-hundred two-thousand-seven-hundred-one two-thousand-seven-hundred-two two-thousand-seven-hundred-three two-thousand-seven-hundred-four two-thousand-seven-hundred-five two-thousand-seven-hundred-six two-thousand-seven-hundred-seven two-thousand-seven-hundred-eight two-thousand-seven-hundred-nine two-thousand-seven-hundred-ten two-thousand-seven-hundred-eleven two-thousand-seven-hundred-twelve two-thousand-seven-hundred-thirteen two-thousand-seven-hundred-fourteen two-thousand-seven-hundred-fifteen two-thousand-seven-hundred-sixteen two-thousand-seven-hundred-seventeen two-thousand-seven-hundred-eighteen two-thousand-seven-hundred-nineteen two-thousand-seven-hundred-twenty two-thousand-seven-hundred-twenty-one two-thousand-seven-hundred-twenty-two two-thousand-seven-hundred-twenty-three two-thousand-seven-hundred-twenty-four two-thousand-seven-hundred-twenty-five two-thousand-seven-hundred-twenty-six two-thousand-seven-hundred-twenty-seven two-thousand-seven-hundred-twenty-eight two-thousand-seven-hundred-twenty-nine two-thousand-seven-hundred-thirty two-thousand-seven-hundred-thirty-one two-thousand-seven-hundred-thirty-two two-thousand-seven-hundred-thirty-three two-thousand-seven-hundred-thirty-four two-thousand-seven-hundred-thirty-five two-thousand-seven-hundred-thirty-six two-thousand-seven-hundred-thirty-seven two-thousand-seven-hundred-thirty-eight two-thousand-seven-hundred-thirty-nine two-thousand-seven-hundred-forty two-thousand-seven-hundred-forty-one two-thousand-seven-hundred-forty-two two-thousand-seven-hundred-forty-three two-thousand-seven-hundred-forty-four two-thousand-seven-hundred-forty-five two-thousand-seven-hundred-forty-six two-thousand-seven-hundred-forty-seven two-thousand-seven-hundred-forty-eight two-thousand-seven-hundred-forty-nine two-thousand-seven-hundred-fifty two-thousand-seven-hundred-fifty-one two-thousand-seven-hundred-fifty-two two-thousand-seven-hundred-fifty-three two-thousand-seven-hundred-fifty-four two-thousand-seven-hundred-fifty-five two-thousand-seven-hundred-fifty-six two-thousand-seven-hundred-fifty-seven two-thousand-seven-hundred-fifty-eight two-thousand-seven-hundred-fifty-nine two-thousand-seven-hundred-sixty two-thousand-seven-hundred-sixty-one two-thousand-seven-hundred-sixty-two two-thousand-seven-hundred-sixty-three two-thousand-seven-hundred-sixty-four two-thousand-seven-hundred-sixty-five two-thousand-seven-hundred-sixty-six two-thousand-seven-hundred-sixty-seven two-thousand-seven-hundred-sixty-eight two-thousand-seven-hundred-sixty-nine two-thousand-seven-hundred-seventy two-thousand-seven-hundred-seventy-one two-thousand-seven-hundred-seventy-two two-thousand-seven-hundred-seventy-three two-thousand-seven-hundred-seventy-four two-thousand-seven-hundred-seventy-five two-thousand-seven-hundred-seventy-six two-thousand-seven-hundred-seventy-seven two-thousand-seven-hundred-seventy-eight two-thousand-seven-hundred-seventy-nine two-thousand-seven-hundred-eighty two-thousand-seven-hundred-eighty-one two-thousand-seven-hundred-eighty-two two-thousand-seven-hundred-eighty-three two-thousand-seven-hundred-eighty-four two-thousand-seven-hundred-eighty-five two-thousand-seven-hundred-eighty-six two-thousand-seven-hundred-eighty-seven two-thousand-seven-hundred-eighty-eight two-thousand-seven-hundred-eighty-nine two-thousand-seven-hundred-ninety two-thousand-seven-hundred-ninety-one two-thousand-seven-hundred-ninety-two two-thousand-seven-hundred-ninety-three two-thousand-seven-hundred-ninety-four two-thousand-seven-hundred-ninety-five two-thousand-seven-hundred-ninety-six two-thousand-seven-hundred-ninety-seven two-thousand-seven-hundred-ninety-eight two-thousand-seven-hundred-ninety-nine two-thousand-eight-hundred two-thousand-eight-hundred-one two-thousand-eight-hundred-two two-thousand-eight-hundred-three two-thousand-eight-hundred-four two-thousand-eight-hundred-five two-thousand-eight-hundred-six two-thousand-eight-hundred-seven two-thousand-eight-hundred-eight two-thousand-eight-hundred-nine two-thousand-eight-hundred-ten two-thousand-eight-hundred-eleven two-thousand-eight-hundred-twelve two-thousand-eight-hundred-thirteen two-thousand-eight-hundred-fourteen two-thousand-eight-hundred-fifteen two-thousand-eight-hundred-sixteen two-thousand-eight-hundred-seventeen two-thousand-eight-hundred-eighteen two-thousand-eight-hundred-nineteen two-thousand-eight-hundred-twenty two-thousand-eight-hundred-twenty-one two-thousand-eight-hundred-twenty-two two-thousand-eight-hundred-twenty-three two-thousand-eight-hundred-twenty-four two-thousand-eight-hundred-twenty-five two-thousand-eight-hundred-twenty-six two-thousand-eight-hundred-twenty-seven two-thousand-eight-hundred-twenty-eight two-thousand-eight-hundred-twenty-nine two-thousand-eight-hundred-thirty two-thousand-eight-hundred-thirty-one two-thousand-eight-hundred-thirty-two two-thousand-eight-hundred-thirty-three two-thousand-eight-hundred-thirty-four two-thousand-eight-hundred-thirty-five two-thousand-eight-hundred-thirty-six two-thousand-eight-hundred-thirty-seven two-thousand-eight-hundred-thirty-eight two-thousand-eight-hundred-thirty-nine two-thousand-eight-hundred-forty two-thousand-eight-hundred-forty-one two-thousand-eight-hundred-forty-two two-thousand-eight-hundred-forty-three two-thousand-eight-hundred-forty-four two-thousand-eight-hundred-forty-five two-thousand-eight-hundred-forty-six two-thousand-eight-hundred-forty-seven two-thousand-eight-hundred-forty-eight two-thousand-eight-hundred-forty-nine two-thousand-eight-hundred-fifty two-thousand-eight-hundred-fifty-one two-thousand-eight-hundred-fifty-two two-thousand-eight-hundred-fifty-three two-thousand-eight-hundred-fifty-four two-thousand-eight-hundred-fifty-five two-thousand-eight-hundred-fifty-six two-thousand-eight-hundred-fifty-seven two-thousand-eight-hundred-fifty-eight two-thousand-eight-hundred-fifty-nine two-thousand-eight-hundred-sixty two-thousand-eight-hundred-sixty-one two-thousand-eight-hundred-sixty-two two-thousand-eight-hundred-sixty-three two-thousand-eight-hundred-sixty-four two-thousand-eight-hundred-sixty-five two-thousand-eight-hundred-sixty-six two-thousand-eight-hundred-sixty-seven two-thousand-eight-hundred-sixty-eight two-thousand-eight-hundred-sixty-nine two-thousand-eight-hundred-seventy two-thousand-eight-hundred-seventy-one two-thousand-eight-hundred-seventy-two two-thousand-eight-hundred-seventy-three two-thousand-eight-hundred-seventy-four two-thousand-eight-hundred-seventy-five two-thousand-eight-hundred-seventy-six two-thousand-eight-hundred-seventy-seven two-thousand-eight-hundred-seventy-eight two-thousand-eight-hundred-seventy-nine two-thousand-eight-hundred-eighty two-thousand-eight-hundred-eighty-one two-thousand-eight-hundred-eighty-two two-thousand-eight-hundred-eighty-three two-thousand-eight-hundred-eighty-four two-thousand-eight-hundred-eighty-five two-thousand-eight-hundred-eighty-six two-thousand-eight-hundred-eighty-seven two-thousand-eight-hundred-eighty-eight two-thousand-eight-hundred-eighty-nine two-thousand-eight-hundred-ninety two-thousand-eight-hundred-ninety-one two-thousand-eight-hundred-ninety-two two-thousand-eight-hundred-ninety-three two-thousand-eight-hundred-ninety-four two-thousand-eight-hundred-ninety-five two-thousand-eight-hundred-ninety-six two-thousand-eight-hundred-ninety-seven two-thousand-eight-hundred-ninety-eight two-thousand-eight-hundred-ninety-nine two-thousand-nine-hundred two-thousand-nine-hundred-one two-thousand-nine-hundred-two two-thousand-nine-hundred-three two-thousand-nine-hundred-four two-thousand-nine-hundred-five two-thousand-nine-hundred-six two-thousand-nine-hundred-seven two-thousand-nine-hundred-eight two-thousand-nine-hundred-nine two-thousand-nine-hundred-ten two-thousand-nine-hundred-eleven two-thousand-nine-hundred-twelve two-thousand-nine-hundred-thirteen two-thousand-nine-hundred-fourteen two-thousand-nine-hundred-fifteen two-thousand-nine-hundred-sixteen two-thousand-nine-hundred-seventeen two-thousand-nine-hundred-eighteen two-thousand-nine-hundred-nineteen two-thousand-nine-hundred-twenty two-thousand-nine-hundred-twenty-one two-thousand-nine-hundred-twenty-two two-thousand-nine-hundred-twenty-three two-thousand-nine-hundred-twenty-four two-thousand-nine-hundred-twenty-five two-thousand-nine-hundred-twenty-six two-thousand-nine-hundred-twenty-seven two-thousand-nine-hundred-twenty-eight two-thousand-nine-hundred-twenty-nine two-thousand-nine-hundred-thirty two-thousand-nine-hundred-thirty-one two-thousand-nine-hundred-thirty-two two-thousand-nine-hundred-thirty-three two-thousand-nine-hundred-thirty-four two-thousand-nine-hundred-thirty-five two-thousand-nine-hundred-thirty-six two-thousand-nine-hundred-thirty-seven two-thousand-nine-hundred-thirty-eight two-thousand-nine-hundred-thirty-nine two-thousand-nine-hundred-forty two-thousand-nine-hundred-forty-one two-thousand-nine-hundred-forty-two two-thousand-nine-hundred-forty-three two-thousand-nine-hundred-forty-four two-thousand-nine-hundred-forty-five two-thousand-nine-hundred-forty-six two-thousand-nine-hundred-forty-seven two-thousand-nine-hundred-forty-eight two-thousand-nine-hundred-forty-nine two-thousand-nine-hundred-fifty two-thousand-nine-hundred-fifty-one two-thousand-nine-hundred-fifty-two two-thousand-nine-hundred-fifty-three two-thousand-nine-hundred-fifty-four two-thousand-nine-hundred-fifty-five two-thousand-nine-hundred-fifty-six two-thousand-nine-hundred-fifty-seven two-thousand-nine-hundred-fifty-eight two-thousand-nine-hundred-fifty-nine two-thousand-nine-hundred-sixty two-thousand-nine-hundred-sixty-one two-thousand-nine-hundred-sixty-two two-thousand-nine-hundred-sixty-three two-thousand-nine-hundred-sixty-four two-thousand-nine-hundred-sixty-five two-thousand-nine-hundred-sixty-six two-thousand-nine-hundred-sixty-seven two-thousand-nine-hundred-sixty-eight two-thousand-nine-hundred-sixty-nine two-thousand-nine-hundred-seventy two-thousand-nine-hundred-seventy-one two-thousand-nine-hundred-seventy-two two-thousand-nine-hundred-seventy-three two-thousand-nine-hundred-seventy-four two-thousand-nine-hundred-seventy-five two-thousand-nine-hundred-seventy-six two-thousand-nine-hundred-seventy-seven two-thousand-nine-hundred-seventy-eight two-thousand-nine-hundred-seventy-nine two-thousand-nine-hundred-eighty two-thousand-nine-hundred-eighty-one two-thousand-nine-hundred-eighty-two two-thousand-nine-hundred-eighty-three two-thousand-nine-hundred-eighty-four two-thousand-nine-hundred-eighty-five two-thousand-nine-hundred-eighty-six two-thousand-nine-hundred-eighty-seven two-thousand-nine-hundred-eighty-eight two-thousand-nine-hundred-eighty-nine two-thousand-nine-hundred-ninety two-thousand-nine-hundred-ninety-one two-thousand-nine-hundred-ninety-two two-thousand-nine-hundred-ninety-three two-thousand-nine-hundred-ninety-four two-thousand-nine-hundred-ninety-five two-thousand-nine-hundred-ninety-six two-thousand-nine-hundred-ninety-seven two-thousand-nine-hundred-ninety-eight two-thousand-nine-hundred-ninety-nine three-thousand
"""

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
# So when we take the input from the user, we want to split the " , " coma, the since split, returns a new array. eg, the user inputs "12,434,423,21,999,1993,329,2999,3000", we get ['12','434','423','21','999','1993','329','2999','3000']. Then we call "for loop" and for every number inside the array, and every word in the "one_to_hundred_arr".





# Function in Python

# "def name () :"
# "def" is used to, when you're or want to use a function
# """"def func() :
#     print('function')""""
# where "func" is the "name" of the function, which can be anything at all.

def greet_user():
  print('Hi there')
  print('Hello')

greet_user()

# Function - Parameters
def get_users(name):
    print(f'Hello there, have you seen {name}')
get_users('Eoin')
get_users('Carrick')

# Difference between "parameters" and "arguments"
# "Parameters" are the holes or placeholders we define in our function when we want to receive information.
# "Arguments" are the actual pieces of information we supply to the functions.
# Examples

#       "Parameters" is more like a placeholder
#             ▼
# def people(name):
#       print(name)

#       "Arguments" is the value for the placeholder
#            ▼
#  people('john')

# Keyword Arguments
# Note Positional Argument, means that orders matters, but in Keyword Arguments, the order is very much less important, since we assign the parameter to the arguments when we call the out the function.

day_mode_in_number = 4 # from 0:00 to 23:00
set_time = 4

def greet_the_user(state, time):
    if state >= 0 <= 12:
        print("Good morning")
    elif state > 12 <= 15:
        print('Good Afternoon')
    else:
        print('Good Evening')
    
    if time == state:
        print('Time to wake up, and play the alarm')
    else:
        print("Don't play the alarm")

#          Keyword Arguments          Keyword Arguments
#               ▼                           ▼
greet_the_user(time = day_mode_in_number, state = set_time)
# greet_the_user(day_mode_in_number, state = set_time) # This is also possible.

# it checks for an input that has a letter vowel inside of it.
user_name =  input('Type your name here ')
vowel = ['a', 'e', 'i', 'o', 'u','y']
def user_checking_name(user_name):
     for every_letter in user_name:
        for every_vowel_letter in vowel:
          if every_letter == every_vowel_letter:
            print(f'There is an {every_vowel_letter} in your name ,{user_name}')
        #   else:
        #     print(f'There is no vowel letter in your name: {user_name}')

user_checking_name(user_name)
user_checking_name('john')
user_checking_name('sarpong')
user_checking_name('sarpslogistics')


def get_arg(arg_name, arg_number):
    print(f'The argument name is {arg_name}, and the number is {arg_number} ')
get_arg(arg_number = 10, arg_name ='value')

# Return Statements
counting_number = 0
def return_user():
    if counting_number > 0:
        for i in range(100,150):
            counting_number += i
    return counting_number
        
return_user()

a = 2
b = 3

print(f'a:{a}& b:{b}')

b,a = a,b

print(f'a:{a} & b:{b}')