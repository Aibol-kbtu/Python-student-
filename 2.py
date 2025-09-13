#1 Python Home
print("Hello, World!")
#2 Python Intro
import sys
print(sys.version)
#3 Python Syntax
#right syntax
if 5 > 2:
    print("Five is greater than two!")

#error syntax
if 5 > 2:
print("Five is greater than two!") ## didn't have a space from to the tuple !!! Tuple is the 4 spaces in tab button

if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
    print("Five is greater than two!") #we can cut this code of peace and rename like

#Right syntax
if 5 > 2:
    print("Five is greater than two!")
    print("Five is greater than two!")
#error  syntax
if 5 > 2:
    print("Five is greater than two!")
        print("Five is greater than two!") # this syntax does not correct because main function in the code "if" , at the moment this function will be case and this case might be exist all additional functions which support algorithm of the function
#Variables in Python:
x = 5
y = "Hello, World!"
#This is a comment.
print("Hello, World!")
#4 Python Comments
#print("Hello, World!")
print("Cheers, Mate!")
#5 Python Variables
x = 5
y = "John"
print(x)
print(y)
"""
In terminal: 5
            John
"""
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a #same alphabet but different symbol in ASCII code

#legal variable
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#illegal variable (Because when we write this  syntex it will be error  in the terminal )
2myvar = "John"
my-var = "John"
my var = "John"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
""" in terminal:  Orange
                    Banana
                    Cherry
"""

x = y = z = "Orange"
print(x)
print(y)
print(z)

""" in terminal:  Orange
                    Orange
                    Orange  :) Same think ,same think ,but different
"""
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# fruits is the massive which each variable initialize x,y and z step by step
""" in terminal:  Orange
                    Orange
                    Orange  :) Same think ,same think ,but different
"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) # global variable is a variable which  usable all the function. Second   one private variable onle use function which exist

#5 Python Date Types
x = 5
print(type(x)) #in terminal : <class 'int'>

x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x))
"""
int terminal:
        Hello World
        <class 'str'>
"""
x = "Hello World" # in terminal <class 'str'>
x = 20 # in terminal <class 'int'>
x = 20.5 # in terminal <class 'float'>
x = 1j # in terminal <class 'complex'>
x = ["apple", "banana", "cherry"] # in terminal <class 'list'>
x = ("apple", "banana", "cherry") # in terminal <class 'tuple'>
x = range(6) # in terminal <class 'range'>
x = {"name" : "John", "age" : 36} # in terminal <class 'dict'>
x = {"apple", "banana", "cherry"} # in terminal <class 'set'>
x = frozenset({"apple", "banana", "cherry"}) # in terminal <class 'frozenset'>
x = True # in terminal <class 'bool'>
x = b"Hello" # in terminal <class 'bytes'>
x = bytearray(5) # in terminal <class 'bytearray'>
x = memoryview(bytes(5)) # in terminal <class 'memoryview'>
x = None # in terminal <class 'NoneType'>
#Python Numbers
x = 35e3
y = 12E4
z = -87.7e100

print(type(x)) # <class 'float'>
print(type(y)) # <class 'float'>
print(type(z)) # <class 'float'>

x = 3+5j
y = 5j
z = -5j

print(type(x)) # <class 'complex'>
print(type(y)) # <class 'complex'>
print(type(z)) # <class 'complex'>

import random

print(random.randrange(1, 10)) #This function can be use random number

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#Python Strings
b = "Hello, World!"
print(b[2:5])
# in terminal llo

b = "Hello, World!"
print(b[-5:-2])
# in terminal: orl

a = "Hello, World!"
print(a.upper())
# in terminal: HELLO, WORLD!

a = "Hello, World!"
print(a.lower())
# in terminal: hello, world!

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" #remove right and left  space if we join r or l letters behind strip words we take same words but change  by removing  left or right spaces

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

a = "Hello"
b = "World"
c = a + b
print(c) # in terminal: HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c) # in terminal: Hello World

#wrong syntax
age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

#right syntax
age = 36
#This will produce an error:
txt = f"My name is John, I am {age}" #when we use f letter beginnig of the word in case program did not think wrong to be concatenate two different value  in one word but another situation if we did not use f letter beginnig of the word in case program say hold on, wait a second  this situation must be never useless because we can't concatenate two different type of variable among themselves
print(txt)
""""
price = 59
txt = f"The price is {price:.2f} dollars" # to be honest first time i will watch this function
print(txt)
#in terminal The price is 59.00 dollars
"""

txt = f"The price is {20 * 59} dollars"
print(txt)
#in terminal The price is 1180 dollars

#wrong syntax
txt = "We are the so-called "Vikings" from the north."

#right syntax
txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt)
# in terminal: It's alright.

txt = "This will insert one \\ (backslash)."
print(txt)
# in terminal: This will insert one \ (backslash).

txt = "Hello\rWorld!"
print(txt)
# in terminal: Hello
#               World!

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
# in terminal: HelloWorld!

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

#in terminal: Hello

#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt)

#in terminal: Hello
