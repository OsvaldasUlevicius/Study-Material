# String formating ------------------------------------------------------------------------------------------

# name = 'Osvaldas'
# greeting = f'Hello, {name}'
# print(greeting)

# greeting = 'Hello, {}'
# with_name = greeting.format(name)
# print(with_name)

# Input -----------------------------------------------------------------------------------------------------

# name = input('What\'s your name? ')
# greeting = f'Hello, {name}'
# print(greeting)
#
# size_input = input('How big is your house (in square feet): ')
# square_metres = int(size_input) / 10.8
# print(f'{size_input} feet are equal to {square_metres:.2f} square metres')

# Python app ------------------------------------------------------------------------------------------------

# age = int(input('What\'s your age? '))
# print('Neat! That is equal to ' + str(age * 31556.952) + ' seconds!')

# Lists, tuples, sets --------------------------------------------------------------------------------------

# list = ['Osvaldas', 'Jomante', 'Tobis']
# tuple = ('Osvaldas', 'Jomante', 'Tobis') # similar to list, but not modifiable, cannot add or remove elements from it
# set = {'Osvaldas', 'Jomante', 'Tobis'} # you can add and remove elements, but the set only contains unique values, don't have an indexed order
#
# print(list[0])
# print(tuple[1])
#
# list[2] = 'Lotas'
# print(list[2])
#
# list.append('Tobis')
# print(list[3])
#
# list.remove('Lotas')
# print(list)
#
# set.add('Lotas')
# print(set)

# Advanced set operations --------------------------------------------------------------------------------------

# friends = {'Osvaldas', 'Jomante', 'Tobis'}
# abroad = {'Osvaldas', 'Tobis'}
#
# local_friends = friends.difference(abroad)
# print(local_friends)
#
# friends = local_friends.union(abroad)
# print(friends)
#
# art = {'Bob', 'Jen', 'Rolf', 'Charlie'}
# science = {'Bob', 'Jen', 'Adam', 'Anne'}
#
# both = art.intersection(science)
# print(both)

# Create a tuple, called my_tuple, with a single value in it
#my_tuple = ('single',)

# Booleans --------------------------------------------------------------------------------------

# print(5 == 5)
# print(5 > 5)
# print (10 != 10)
#
# friends = ['Rolf', 'Bob']
# enemies = ['Rolf', 'Bob']
# frenemies = friends
# print(friends == enemies) # true nes lygina abieju listu elementus
# print(friends is enemies) # false nes tikrina ar tai yra tas pats dalykas atmintyje PC
# print(friends is frenemies) # true nes abu nurodo i ta pati lista PC atmintyje

# if statements --------------------------------------------------------------------------------------

# day_of_the_week = input('What day of the week is it today? ').capitalize()
# if day_of_the_week == 'Monday':
#     print('Damn it!')
# elif day_of_the_week == 'Friday':
#     print('Nice!')
# else:
#     print('Full speed ahead!')


# in keyword --------------------------------------------------------------------------------------

# friends = ['Rolf', 'Bob', 'Jen']
# print('Jen' in friends)
# print('Osvaldas' not in friends)
#
# movies_watched = {'The Matrix', 'Green Book', 'Her'}
# user_movie = input('Enter something you\'ve watched recently: ')
# print(user_movie in movies_watched)

# if statements with the in keyword -----------------------------------------------------------------

# movies_watched = {'The Matrix', 'Green Book', 'Her'}
# user_movie = input('Enter something you\'ve watched recently: ')
#
# if user_movie not in movies_watched:
#     movies_watched.add(user_movie)
#     print(movies_watched)
# else:
#     print(f'I\'ve watched {user_movie} too!')

# number = 7
# user_input = input('Enter \'y\' if you would like to play: ') # .lower()
#
# if user_input in ('y', 'Y'):
#     user_number = int(input('Guess our number: '))
#     if user_number == number:
#         print('You guessed correctly!')
#     elif number - user_number in (1, -1): # or elif abs(number - user_number) == 1:
#         print('You were off by 1!')
#     else:
#         print('Sorry, it\'s wrong!')

# LOOPS -----------------------------------------------------------------

# number = 7
#
# while True:
#     user_input = input('Would like to play? (Y/n) ')
#     if user_input not in ('y', 'Y', 'n', 'N'):
#         raise TypeError('That is not a choice!')
#
#     if user_input.lower() == 'n':
#         break
#
#     user_number = int(input('Guess our number: '))
#     if user_number == number:
#         print('You guessed correctly!')
#         break
#     elif number - user_number in (1, -1): # or elif abs(number - user_number) == 1:
#         print('You were off by 1!')
#     else:
#         print('Sorry, it\'s wrong!')

# friends = ['Rolf', 'Jen', 'Bob', 'Anne']
#
# for friend in friends:
#     print(f'{friend} is my good friend.')
#
# for number in range(4):
#     print(number)
#
# grades = [35, 67, 98, 100, 100]
# total = 0
# amount = len(grades)
#
# for grade in grades:
#     total += grade
# print('The grade average is ' + str(total/amount))
#
# total = sum(grades)


# LIST COMPREHENSIONS -----------------------------------------------------------------
# allows to create new lists on the fly from existing lists

# numbers = [1, 3, 5]
# doubled = []
#
# # for num in numbers:
# #   doubled.append(num * 2) #-------- Ilgesnis variantas
#
# doubled = [num * 2 for num in numbers] # -------- Trumpesnis variantas
# print(doubled)
#
# friends = ['Rolf', 'Sam', 'Samantha', 'Saurabh', 'Jen']
# starts_s = [friend for friend in friends if friend.startswith('S')] # first you put what you want to add
# print(starts_s)

# DICTIONARIES -----------------------------------------------------------------

# friend_ages = {'Rolf': 24, 'Adam': 30, 'Anne': 27}
# print(friend_ages['Rolf'])
#
# friend_ages['Bob'] = 20 # add a value
# print(friend_ages)
# friend_ages['Rolf'] = 16 # change a value
# print(friend_ages)
#
# friends = [
#     {'name': 'Rolf', 'age': 24},
#     {'name': 'Adam', 'age': 30},
#     {'name': 'Anne', 'age': 27},
# ]
#
# print(friends[1]['name'])

# student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}
#
# # for student in student_attendance: # LONGER WAY
# #     #print(student)  # returns the keys in the dictionary
# #     print(f'{student}: {student_attendance[student]}')
#
# for student, attendance in student_attendance.items(): # BETTER
#     print(f'{student}: {attendance}')
#
# if 'Bob' in student_attendance:
#     print(f'Bob: {student_attendance["Bob"]}')
# else:
#     print('Bob is not a student')
#
# attendance_values = student_attendance.values()
# print(sum(attendance_values) / len(attendance_values))

# DESTRUCTURING VARIABLES  -----------------------------------------------------------------

# x = 5, 11 - a tuple does not necessarily need brackets ()
#x, y = 5, 11 # x is 5 and y is 11

# tuple = 5, 11
# x, y = tuple
#
# student_attendance = {'Rolf': 96, 'Bob': 80, 'Anne': 100}
#
# print(list(student_attendance.items())) # returns a list of tuples
#
# for tuple in student_attendance.items():
#      print(tuple)
#
# people = [('Bob', 42, 'Mechanic'), ('James', 24, 'Artist'), ('Harry', 32, 'Lecturer')]
#
# for name, age, profession in people:
#     print(f'Name: {name}, Age: {age}, Profession: {profession}')

# person = ('Bob', 42, 'Mechanic')
#
# name, _, profession = person # _ - trash variable
# print(name, profession)

# head, *tail = [1, 2, 3, 4, 5] # head yra pirmoji verte - 1, o *tails surenka likusias vertes
# print(head)
# print(tail)
#
# *head, tail = [1, 2, 3, 4, 5]
# print(head)
# print(tail)


# FUNCTIONS  -----------------------------------------------------------------
#
# def hello():
#     print('Hello')
#
# hello()
#
# def user_age_in_seconds():
#     user_age = int(input('What is your age? '))
#     age_seconds = user_age * 365 * 24 * 60 *60
#     print(age_seconds)
#
# user_age_in_seconds()

# FUNCTION ARGUMENTS AND PARAMETERS -----------------------------------------------------------------

# def add(x, y): # these are the parameters
#     return x + y
#
# print(add(5, 20)) #arguments go here
# print(add(y=55,x=12)) # keyword arguments
#
# def say_hello():
#     print('Hello!')
#
# say_hello()
#
# def divide(dividend, divisor):
#     if divisor != 0:
#         print(dividend / divisor)
#     else:
#         print('You fool!')
#
# divide(dividend=15, divisor=5)

# DEFAULT PARAMETER VALUES -----------------------------------------------------------------

# def add(x, y=8):
#     print(x + y)
#
# add(5)

# DEFAULT PARAMETER VALUES -----------------------------------------------------------------
# all functions return none by default unless specified otherwise

# def add(x, y):
#     return x + y
#
# print(add(5, 8))
# from builtins import print
#
#
# def divide(dividend, divisor):
#     if divisor != 0:
#         return dividend / divisor
#     else:
#         return 'You fool!'
#
# print(divide(dividend=15, divisor=0))

# LAMBDA FUNCTIONS -----------------------------------------------------------------
# a different kind of function which doesn't have a name and is only used to return values not to perform actions
# lambdas are meant to be short functions

#lambda x,y: x + y # x,y - the list of parameters/ x+y - return value of the function ---- This function does not have a name

# add = lambda x, y: x + y
# print(add(5, 7))
#
# print((lambda x, y: x + y)(5,7)) # you are using a 5,7 on the previous lambda function

# def double(x):
#     return x * 2
#
# sequence = [1, 3, 5, 9]
# doubled = [double(x) for x in sequence] # list comprehension
# doubled = map(double, sequence) # does exactly the same as the above list comprehension
# doubled = [(lambda x: x * 2)(x) for x in sequence]
# doubled = list(map(lambda x: x * 2, sequence)) # lambda + map / map returns a map object and not a list of numbers, that's why we convert it to a list
#


# DICTIONARY COMPREHENSIONS -----------------------------------------------------------------

# users = [
#     (0, 'Bob', 'password'),
#     (1, 'Rolf', 'bob123'),
#     (2, 'Jose', 'longp4assword'),
#     (1, 'username', '1234'),
# ]
#
# username_mapping = {user[1]: user for user in users} # associates the username with the entire user tuple
#
# print(username_mapping)
# print(username_mapping['Bob'])
#
# username_input = input('Enter your username: ')
# password_input = input('Enter your password: ')
#
# if password_input in username_mapping[username_input]:
#     print('Good')
#
# _, username, password = username_mapping[username_input]
# if password_input == password:
#     print('Your details are correct')
# else:
#     print('Wrong!')

# UNPACKING ARGUMENTS -----------------------------------------------------------------

# def print_the_args(*args): # the function has a set of arguments that will be collected into a tuple of arguments
#     print(args)
#
# print_the_args(1, 3, 5)
#
# def multiply(*args):
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total
#
# print(multiply(1, 3, 5))
#
# def add(x, y):
#     return x + y
#
# nums = [3, 5]
# print(add(*nums)) # using *args in the call of the function
#
# nums = {'x': 15, 'y': 54}
# print(add(**nums)) # ** - keyword arguments

# def multiply(*args):
#     total = 1
#     for arg in args:
#         total = total * arg
#     return total
#
# def apply(*args, operator): # collects as many values as possible + a named parameter 'operator'
#     if operator == '*':
#         return multiply(*args)
#     elif operator == '+':
#         return sum(args)
#     else:
#         return 'No valid operator provided to apply().'
#
# print(apply(1, 3, 6, 7, operator='+'))
# print(apply(1, 3, 6, 7, operator='*'))
# print(apply(1, 3, 6, 7, operator='a'))

# UNPACKING KEYWORD ARGUMENTS -----------------------------------------------------------------

# def named(**kwargs):
#     print(kwargs)
#
# named(name='Bob', age=25) # prints a dictionary
#
# def named(name, age):
#      print(name, age)
# #
# # details = {'name': 'Bob', 'age': 25}
# # named(**details) # pass in the kwargs in the call
#
# def print_nicely(**kwargs):
#     named(**kwargs)
#     for arg, value in kwargs.items():
#         print(f'{arg}: {value}')
#
# print_nicely(name='Bob', age=25)


# def both(*args, **kwargs): # is normally used to accept an unlimited number of arguments
#     print(args)
#     print(kwargs)
#
# both(1, 3, 5, name='Bob', age=25)

# OBJECT-ORIENTED PROGRAMMING -----------------------------------------------------------------

# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def average(self):
#         return 'The average for ' + self.name + ' is ' +str(sum(self.grades)/len(self.grades))
#         ## return sum(self.grades) / len(self.grades) - jeigu vienintelis parametras yra self
#
# grades = (90, 90, 93, 78, 90)
# name = 'Juozapas'
# student = Student(name=name, grades=grades)
# # student = Student(name, grades)
# print(student.name)
# print(student.average())

# METHODS: __str__ and __repr__  -----------------------------------------------------------------
# used for representing an object as a string

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # def __str__(self):
#     #     # a method allows to turn the object into a string
#     #     return f'Person {self.name}, {self.age} years old.'
#
#     def __repr__(self):
#         # goal is to be unambiguous - AISKUS/ it should return a string that allows us to recreate the original object very easily
#         # it is used in the debugger
#         # by default python will print the str method if they are both in the class
#         return f'<Person(\'{self.name}\', {self.age})>'
#
# bob = Person('Bob', 35)
# print(bob)

# METHODS: @classmethod and @staticmethod  -----------------------------------------------------------------

# class ClassTest:
#
#     def instance_method(self): # it is called instance method because it uses the object parameter (self) as its first parameter and because we call it on a class instance
#         print(f'Called instance_method of {self}')
#     # use it if you need to use the object - when you want to produce an action that uses the data inside the object/ modify data
#
#     @classmethod
#     def class_method(cls): # cls is the Class itself - ClassTest
#         print(f'Called class_method of {cls}')
#     # use it if you need to use the class / used as factories
#
#     @staticmethod
#     def static_method(): #these methods don't get any arguments / it's just a function placed inside the class
#         print('Called static method.')
#     # are used to place a method inside of class
#
# test = ClassTest() # an instance of classtest #  we call the function on a class instance
# test.instance_method()
#
# ClassTest.class_method() # you call this function a class itself, not an instance of it
#
# ClassTest.static_method()
# test.static_method()


# class Book:
#     TYPES = ('hardcover', 'paperback') # you can put variables inside the class and they become class properties
#
#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight
#
#     def __repr__(self):
#         return f'<Book {self.name}, {self.book_type}, weighing {self.weight}g>'
#
#     @classmethod
#     def hard_cover(cls, name, page_weight):
#         return Book(name, Book.TYPES[0], page_weight + 100)
#
#     @classmethod
#     def paperback(cls, name, page_weight):
#         return Book(name, Book.TYPES[1], page_weight)
#     # class methods create clasees inside of the class - factories
#
# print(Book.TYPES)
# book1 = Book.hard_cover('Harry Potter', 1500)
# print(book1)
# book2 = Book.paperback('Eragon', 600)
# print(book2)

# CLASS INHERITENCE -----------------------------------------------------------------
# Inheritence allows one class to take some methods and properties from another class

# class Device:
#
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True
#
#     def __str__(self):
#         return f'Device {self.name!r} ({self.connected_by})' # !r calls the repr method of self.name and puts the quotes around self.name ''
#
#     def disconnect(self):
#         self.connected = False
#         print('Disconnected')
#
# printer = Device('Printer', 'USB')
# print(printer)
# printer.disconnect()
#
# class Printer(Device): # class printer inherits from device and copies all of its methods
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by) # inherits init method from the parent class - Device
#         self.capacity = capacity
#         self.remaining_pages = capacity
#
#     def __str__(self):
#         return f'{super().__str__()} ({self.remaining_pages} pages remaining)'
#
#     def print(self, pages):
#         if not self.connected:
#             print('Your printer is not connected!')
#             return
#         print(f'Printing {pages} pages.')
#         self.remaining_pages -= pages
#
# newprinter = Printer('Printer', 'USB', 500)
# newprinter.print(20)
# print(newprinter)
# newprinter.disconnect()
# newprinter.print(30)

# CLASS COMPOSITION -----------------------------------------------------------------
# Composition allows your classes to be simpler and reduces the complexity of the code
# COMPOSITION - when you have a class that contains other classes

# class Bookshelf:
#
#     def __init__(self, *books):
#         self.books = books
#
#     def __str__(self):
#         return f'Bookshelf with {len(self.books)} books.'
#
# class Book:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f'Book {self.name}'
#
# book = Book('Harry Potter')
# book2 = Book('Python 101')
# shelf = Bookshelf(book, book2)
#
# print(shelf)
# print(shelf.books)

# Inheritance - a book is a bookshelf, composition - a bookshelf has many books

# Type hinting -----------------------------------------------------------------
# the editor will alert you if you pass in the wrong thing

# from typing import List # , Tuple, Set, etc...
#
# def list_avg(sequence: List) -> float: # tells python that sequence should be a list and that the function will return a float
#     return sum(sequence) / len(sequence)
#
# list_avg(123)
#
# class Book:
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count
#
#     @classmethod
#     def hardcover(cls, name: str, page_weight: int) -> 'Book': #will return a Book object if it is the same type of class that you are currently in you have to put it in quotes, else you can signal it without quotes - Bookshelf
#         return Book(name, Book.TYPES[0], page_weight + 100)
#
# class Bookshelf:
#     def __init__(self, books: List[Book]): # the books parameter should be a list of Book object
#         self.books = books
#
#     def __str__(self) -> str:
#         return f'Bookshelf with {len(self.books)} books.'


# Imports in Python -----------------------------------------------------------------

# from mymodulerefresher import divide # import mymodulerefresher
# import sys
# print(divide(10,2))
# print(sys.path)

import mymodulerefresher
# import sys
#
# print(sys.modules)

# Relative Imports in Python -----------------------------------------------------------------
# relative import can import from the current folder that the file is in but it can't import if there is no folder name in the import path

# ERRORS in Python -----------------------------------------------------------------

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError('Divisor cannot be 0')
#     return dividend / divisor
#
# grades = []
# try:
#     average = divide(sum(grades), len(grades))
# except ZeroDivisionError as e:
#     print('There are no grades yet in your list')
#     print(e)
# else: # happens if no error happened
#     print(average)
# finally:
#     print('I will always run :)')

# TypeError - when something was the wrong type
# ValueError - when something had the wrong/unexpected value

# CUSTOM ERROR CLASSES -----------------------------------------------------------------

# class TooManyPagesReadError(ValueError): #errors have to inherit from the most relevant error to work
#     pass
#
# class Book:
#
#     def __init__(self, name: str, page_count: int):
#         self.name = name
#         self.page_count = page_count
#         self.pages_read = 0
#
#     def __repr__(self):
#         return (
#             f'<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>'
#         )
#
#     def read(self, pages:int):
#         if self.pages_read + pages > self.page_count:
#             raise TooManyPagesReadError(
#                 f'You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages.'
#             )
#         self.pages_read += pages
#         print(f'You have now read {self.pages_read} pages out of {self.page_count}')
#
# python101 = Book('Python 101', 50)
# try:
#     python101.read(15)
#     python101.read(50)
# except TooManyPagesReadError as e:
#     print(e)

# FIRST CLASS FUNCTION -----------------------------------------------------------------
# this means that functions are just variables

# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError('Divisor cannot be 0')
#     return dividend / divisor
#
# def calculate(*values, operator):
#     return operator(*values)
#
# result = calculate(20, 4, operator=divide) # passes in the divide function and turns operator into a function
# print(result)


# def search(sequence, expected, finder):
#     for elem in sequence:
#         if finder(elem) == expected:
#             return elem
#     raise RuntimeError(f'Could not find an element with {expected}.')
#
# friends = [
#     {'name': 'Rolf Smith', 'age': 24},
#     {'name': 'Adam Wool', 'age': 30},
#     {'name': 'Anne Pun', 'age': 27}
# ]
#
# def get_friend_name(friend):
#     return friend['name']
#
# print(search(friends, 'Rolf Smith', get_friend_name))
# print(search(friends, 'Rolf Smith', lambda friend: friend['name']))
# print(search(friends, 'Rolf Smith', lambda friend: friend['name']))
# from operator get itemgetter
# print(search(friends, 'Rolf Smith', itemgetter['name']))


# SIMPLE DECORATORS -----------------------------------------------------------------
# They allow to very easily modify functions

# user = {'username': 'jose', 'access_level': 'guest'}
#
# def get_admin_password():
#     return '1234'
#
# def make_secure(func):
#     def secure_function():
#         if user['access_level'] == 'admin':
#             return func()
#         else:
#             return 'Denied'
#     return secure_function()
#
# print(make_secure(get_admin_password()))

#  THE @ SYNTAX FOR DECORATORS-----------------------------------------------------------------

# import functools
#
# user = {'username': 'jose', 'access_level': 'guest'}
#
#
# def make_secure(func):
#     @functools.wraps(func) # secure function doesn't replace get admin password function name
#     def secure_function():
#         if user['access_level'] == 'admin':
#             return func()
#         else:
#             return 'Denied'
#     return secure_function
#
# @make_secure
# def get_admin_password():
#     return '1234'
#
#
# print(get_admin_password())

#  DECORATING FUNCTIONS WITH PARAMETERS -----------------------------------------------------------------
# if you update the original function with parameters you have to do the same to decorators
# the best way is to initialy add *args and **kwargs to decorators

#  DECORATORS WITH PARAMETERS -----------------------------------------------------------------

# import functools
#
# user = {"username": "anna", "access_level": "user"}
#
#
# def make_secure(func):
#     @functools.wraps(func)
#     def secure_function(*args, **kwargs):
#         if user["access_level"] == "admin":
#             return func(*args, **kwargs)
#         else:
#             return f"No admin permissions for {user['username']}."
#
#     return secure_function
#
#
# @make_secure
# def get_admin_password():
#     return "admin: 1234"
#
#
# @make_secure
# def get_dashboard_password():
#     return "user: user_password"
#
#
# # What if we wanted some passwords to be available to "user" and others to "admin" ?
#
# user = {"username": "anna", "access_level": "user"}
#
#
# def make_secure(access_level):
#     def decorator(func):
#         @functools.wraps(func)
#         def secure_function(*args, **kwargs):
#             if user["access_level"] == access_level:
#                 return func(*args, **kwargs)
#             else:
#                 return f"No {access_level} permissions for {user['username']}."
#
#         return secure_function
#
#     return decorator
#
#
# @make_secure(
#     "admin"
# )  # This runs the make_secure function, which returns decorator. Essentially the same to doing `@decorator`, which is what we had before.
# def get_admin_password():
#     return "admin: 1234"
#
#
# @make_secure("user")
# def get_dashboard_password():
#     return "user: user_password"
#
#
# print(get_admin_password())
# print(get_dashboard_password())
#
# user = {"username": "anna", "access_level": "admin"}
#
# print(get_admin_password())
# print(get_dashboard_password())

#  MUTABILITY IN PYTHON -----------------------------------------------------------------
# mutable - values that can be changed
# tuples are immutable, integers, strings, floats and booleans are also immutable

#### Mutable default parameters (and why they re a bad idea)

from typing import List

class Student:

    def __init__(self, name: str, grades: List[int] = []): # This is bad! never make a parameter into a mutable value by default
        self.name = name
        self.grades = grades

    def take_exam(self, result):
        self.grades.append(result)

bob = Student('Bob')
rolf = Student('Rolf')
bob.take_exam(90)
print(bob.grades)
print(rolf.grades) # rolfs grades are 90... even tough he did not take an exam, both of these objects point to the same list....
 
