x = 10
y = "folorunso"

print(x)
print(y)

name, age, pi, bool = "mayowa", 20, 36.14, True

print(name, age, pi, bool)

z = "agboola"
z = 4

print(z)

x = 5 
x = "carer"

print(x)

#Variable Names task

myvar = "agboola"
my_var = "folorunso"
_my_var = "emmanuel"
myVAR = "michael"
MYVAR = "cecilia"
myvar2 = "damilola"

print(myvar)
print(my_var)
print(_my_var)
print(myVAR)
print(MYVAR)
print(myvar2)

name, full_name, pi = "james", "j james", 3.14

print(name, full_name, pi)

name, full_name, pi = "michael", "A emmanuel", 3.14

print(name, full_name, pi)

#Python data type<>(())

x = int(6)
y = str(3)
z = float(3)
q = bool

print(x)
print(y)
print(z)
print(bool)

c = float(9)
b = int(4)
n = str(12)

print(c)
print(b)
print(n)

y = 10
z = "emmanuel"

print(type(y))
print(type(z))

t = 40
q = "school"

print(type(t))
print(type(q))

brand = "amigoscode"
age = 23
pi = 3.14 
numbers = []
isAdult = True

print(type(brand))
print(type(age))
print(type(numbers))
print(type(isAdult))

k = 50
u = "cottbus"
r = 30.56

print(type(k))
print(type(u))
print(type(r))

#Case-Sensitive<>Variable names are case-sensitive.This will create two variables

m = 8
M = "damilola"

print(M)
print(m)

u = 9
Q = "willi_budich"

print(u)
print(Q)

#Many Values to Multiple Variables task

x, y, z, f = "grape", "apple", "banana", "blue_berry"

print(x)
print(y)
print(z)
print(f)

l, v, d, w = "orange", "melon", "blue_berry", "mango"

print(l)
print(v)
print(d)
print(w)

#One Value to Multiple Variables

k = l = w = "cherry"

print(k)
print(l)
print(w)

r = t = q = j = "avocado"

print(r)
print(q)
print(j)

#Unpack a Collection inside the list

fruits = ["melon", "cherry_wood", "banana"]
y, z, x = fruits

print(y)
print(z)
print(x)

foods = ["rice", "eba", "beans","yam","garri","spaghetti","indomine"]
w, s, q, v, t, g, n, = foods

print(w)
print(q)
print(s)
print(v)
print(g)
print(n)

brands = ["tommy", "gucci", "zara", "all_star", "nike", "mango", "iphone", "Samsung"]
t, i, v, b, n, k, m, f = brands

#Python - Output Variables

y = "folorunso is awesome"

print(y)

z = "python"
x = "is"
y = "awesome"
p = "love"
k = "rootings"

print(z, x, y, p, k)

y = "python "
z = "is "
x = "awesome "
g = "favourite "
h = "matters "
s = "sweet "

print(y+z+x+g+h+s)

y = 10
x = 90

print(y+x)

v = 1000
m = 4500

print(v-m)

w = 718
b = 806

print(w+b)

z = 24
y = "folorunso"

print(z, y)

a = 33
j = "emmanuel"

print(a, j)

#Python - Global Variables

y = "awesome"

def myfunc():
    
    print("python is " + y)

myfunc()

z = "awesome"

def myfunc():
    z = "fantastic"
    print("python is " + z)
    
myfunc()

print("python is " + z)

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("python is " + x)

x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    
myfunc()

print("python is " + x)

#Python Data Types

#a = "Hello World"   str 
#b = 20  int 
#c = 20.5    float   
#d = 1j  complex 
#e = ["apple", "banana", "cherry"]   list    
#f = ("apple", "banana", "cherry")   tuple   
#g = range(6)    range   
#h = {"name" : "John", "age" : 36}   dict    
#i = {"apple", "banana", "cherry"}   set 
#j = frozenset({"apple", "banana", "cherry"})    frozenset   
#k = True    bool    
#l = b"Hello"    bytes   
#m = bytearray(5)   bytearray   
#n = memoryview(bytes(5))    memoryview  
#o = None    NoneType

#Setting the Specific Data Type
#1 = str("Hello World")  str 
#2 = int(20) int 
#3 = float(20.5) float   
#4 = complex(1j) complex 
#5 = list(("apple", "banana", "cherry")) list    
#6 = tuple(("apple", "banana", "cherry"))    tuple   
#7 = range(6)    range   
#8 = dict(name="John", age=36)   dict    
#9 = set(("apple", "banana", "cherry"))  set 
#10 = frozenset(("apple", "banana", "cherry"))    frozenset   
#11 = bool(5) bool    
#12 = bytes(5)    bytes   
#13 = bytearray(5)    bytearray   
#14 = memoryview(bytes(5))    memoryview

#Python Numbers

x = 1
z = 2.8
y = 1j

print(type(x))
print(type(z))
print(type(y))

#Integers:

s = 0
x = 1
z = 35656222554887711
y = -3255522

print(type(s))
print(type(x))
print(type(z))
print(type(y))

#Float<>Float, or "floating point number" 
#is a number, positive or negative, containing one or more decimals.

y = 1.10
x = 1.0
z = -35.59

print(type(y))
print(type(x))
print(type(z))

#float<>Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
z = 12E4
y = -87.7e100
p = 45e6

print(type(x))
print(type(z))
print(type(y))
print(type(p))

#Complex<>Complex numbers are written with a "j" as the imaginary part:

z = 3+5j
x = 5j
y = -5j

print(type(z))
print(type(x))
print(type(y))

#Type Conversion in python

x = float(1)

y = int(2.8)

z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

q = complex(10)

s = float(7000)

g = int(36.13)

print(q)
print(s)
print(g)

print(type(q))
print(type(s))
print(type(y))

z = float(30.44)

print(int(z))

y = int(5000)

print(float(y))

x = (9)

print(complex(x))

#Random Number<>Python does not have a random() function to make a random number but
#Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1, 9))

import random

print(random.randrange(2, 8))

import random

print(random.randrange(5, 20))

#Python Casting<>intergers

y = int(1)
x = int(2.8)
z = int("3")
g = int(0)

print(y)
print(x)
print(z)
print(g)

#Python Casting<>floats

y = float(0) 
x = float(1.8)
z = float("3")
w = float("4.2")

print(y)
print(x)
print(z)
print(w)

g = float(4)
h = float(4.18)
k = float("16")
l = float("28.8")

print(g)
print(h)
print(k)
print(l)

#Python Casting<>strings

x = str("s1")
z = str(2)
y = str(3.0)

print(x)
print(z)
print(y)

o = ("s10")
b = (18)
f = (6.0)

print(o)
print(b)
print(f)

#Strings are Arrays<>

a = "Hello, world!"

print(a[4])
print(a[11])
print(a[9])

x = "good, morning!"

print(x[3])
print(x[2])
print(x[6])

brand = "amigoscode"

print(brand)

brand = "Amigoscode"

print(brand.replace("A", "a"))
print(brand.replace("A", "40"))
print(len(brand))
print(brand == "Amigoscode")
print(brand == "amigoscode")
print(brand != "amigoscode")
print("code" in brand)
print("code" not in brand)

x = "Good, morning!"

print(x[12])

z = "cottbus_train_station!"
 
print(z[20])

import array as arr 

numbers = ('i', [10, 20, 30])

print(numbers)

from array import *

numbers = ('d', [10.0, 20.0, 30.0])

print(numbers)

import array as arr

numbers = arr.array('q',[10,20,30])

print(numbers[:2])
print(numbers[-2:])

import array as arr 

numbers = arr.array('i',[10,20,30,40,50,60,70,80,90])

print(numbers[:-6])

#Looping Through a String<>Since strings are arrays, we 
#can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x)

  for z in "school":
    print(z)

  for y in "education":
    print(y)

#String Length<>To get the length of a string, use the len() function.

a = "Hello, world!"
 
print(len(a))

z = "cottbus_train_station!"
 
print(len(z))

brand = "amigoscode"
 
print(brand == "amigoscode")

house = "willi_budich"
 
print(house != "willi_budich")

city = "Cottbus"
 
print(city != "cottbus")

#Check String<>To check if a certain phrase or character 
#is present in a string, we can use the keyword in.

txt = "the best things in life is free!"
print("free" in txt)

py = "the best things to learn in life is python code"
print("code" in py)

#Use it in an if statement

txt = "the best things to learn in life is python code!"
if "code" in txt:
    print("yes, 'python' is present.")

    name = "my name is michael to the best in this world is to code!"
if "code" in name:
    print("yes, 'micheal' is present.")

#Check if NOT<>To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#Use it in an if statement:

txt = "the best thing in life is free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")  

    life = "hard things last for ever and ever in human hands!"
if "expensive" not in life:
    print("YES, 'expensive' is NOT present.")

    txtco = "The most of things in life they are not for free!"
if "expensive" not in txtco:
    print("No, 'expensive' is NOT Present.")

#Slicing<>You can return a range of characters by using the slice syntax.Specify
#the start index and the end index,separated by a colon, to return a part of the string.

y = "Hello, world!"
print(y[2:5])

x = "cottbus, station!"
print(x[2:7])

z = "Transportion!"
print(z[4:20])

#Slice From the Start<>By leaving out the start index, the rang

b = "folorunso!"
print(b[:9])

p = "cottbus, germany!"
print(p[:7])

#Slice To the End<>By leaving out the end index, the range 
#will go to the end:Get the characters from position 2, and all

b = "Hello, world!"
print(b[3:])

v = "determination, mind!"
print(v[5:])

#Negative Indexing<>Use negative indexes to start the slice from the end of the string:
#Get the characters From "o" in "World!" (position -5)To, but not included: "d" in "World!" (position -2):

b = "Hello, world!"
print(b[-5:-2])

z = "jupyter, python!"
print(z[-5:-2])

#Python - Modify Strings<>Python has a set of built-in methods that you can use on strings.
#Upper Caseyour own Python ServerThe upper() method returns the string in upper case:

a = "Hello, world!"
print(a.upper())

x = "python, code!"
print(x.upper())

#Lower Case<>The lower() method returns the string in lower case:

c = "Hello, jupyter!"
print(c.lower())

y = "folorunso, python!"
print(y.lower())

#Remove Whitespace<>Whitespace is the space before and/or after the actual text, and very often you 
#want to remove this space.The strip() method removes any whitespace from the beginning or the end:

a = "Hello, world!"
print(a.strip())

b = "python, code!"
print(b.strip())

#Replace String<>The replace() method replaces a string with another string:

a = "Hello, world!"
print(a.replace("H", "J"))

x = "Python, world!"
print(x.replace("P", "Q"))

y = "Good, morning!"
print(y.replace("G", "L"))

#split String<>The split() method returns a list where the text between the specified separator becomes the list items.
#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello"
b = "world"
c = a + b
print(c)

y = "konigs"
z = "cottbus"
x = y + " " + z
print(x)

#String Format<>As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
#But we can combine strings and numbers by using the format() method!
#The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is john, and  i am {}"
print(txt.format(age))

age = 23
code = "python code is the best, i am interested in {}"
print(code.format(age))

name = "jamila"

email = """

hello {},
how are you doing?
it was nice talking to you here

"""
print(email.format(name))

name = "Folorunso"

email = f""" 

blessed morning to you my very good friend {name}, 
nice learing in your homework keep it up bro?
never stop learing your python code everyday bro...
age {10 + 13}!
"""
print(email)

#The format() method takes unlimited number of arguments,
#and are placed into the respective placeholders:

quntity = 3
itemno = 567
price = 49.95
myorder = " i want {} pieces of item {} for {} dollars."
print(myorder.format(quntity, itemno, price))

high_level = 15
seria_number = 1876
price = 200.99
checkout = "i want {} pieces of nivea_body_cream {} for {} euros."
print(checkout.format(high_level, seria_number, price))

#You can use index numbers {0} to be sure the arguments
#are placed in the correct placeholders:

quntity = 3 
itemno = 567
price = 450.98
my_order_is = "i want pay {2} pounds for {4} piece of Chocolate_milkshake {7}."
print(myorder.format(quntity, itemno, price))

quntity = 20
itemno = 567
price = 49.95
my_order_is = "i want to pay {2} dollars for {3} piece of justice_enegry_drinks {5}."
print(myorder.format(quntity, itemno, price))

#Python - Escape Characters<> To insert characters that are illegal in a string, use an escape character.
#An escape character is a backslash (\" \") followed by the character you want to insert.
#An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
#You will get an error if you use double quotes inside a string that is surrounded by double quotes:

txt = "we ara so-called \"vikings\" from the north."
print(txt)

txt = "we are so-called \"blackafrican\" from the south and north and west and east."
print(txt)

#Escape Characters<> Other escape characters used in Python:
#Code    Result  Try it
#\'  Single Quote    
#\\  Backslash   
#\n  New Line    
#\r  Carriage Return 
#\t  Tab 
#\b  Backspace   
#\f  Form Feed   
#\ooo    Octal value 
#\xhh    Hex value   
#Python Booleans<>Booleans represent one of two values: True or False.
#Boolean Values In programming you often need to know if an expression is True or False.
#You can evaluate any expression in Python, and get one of two answers, True or False.
#When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(10 > 9)
print(10 == 9)
print(10 < 9)

print(50 > 40)
print(50 != 30)
print(50 < 40)

#When you run a condition in an if statement, Python returns True or False:
#Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
    print("b is greater than a")
    
else:
    print("b is not greater than a")

    z = 1500
x = 100

if b > z:
    print("x is greater than z")
else:
    print("x is not greater than z")

#Functions can Return a Boolean<>You can create functions that returns a Boolean Value:
#ExamplePrint the answer of a function:

def  myFunction() :
  return True

print(myFunction())

def  myFunction() :
  return False

print(myFunction())

#You can execute code based on the Boolean answer of a function:
#Example<>Print "YES!" if the function returns True, otherwise print "NO!":

def  myFunction() :
   return True

if myFunction():
    print("YES!")
else:
    print("NO!")

    def myFuction() :
     return False

if myFunction():
    print("NO!")  
else:
    print("YES!")

#Python also has many built-in functions that return a boolean value, like the isinstance() function, 
#which can be used to determine if an object is of a certain data type:
#ExampleCheck if an object is an integer or not:

x = 200

print(isinstance(x, int))

z = 36

print(isinstance(z, int))

y = 36.14

print(isinstance(y, float))

w = 10+5j

print(isinstance(w, complex))

#Python Operators<>Operators are used to perform operations on variables and values.
#In the example below, we use the + operator to add together two values:

print(10 + 5)

print(100 + 40)

#Python divides the operators in the following groups:
#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators

x = 5
z = 3
y = 15
v = 5
d = 10
j = 5
f = 12
t = 3
b = 9
h = 2
l = 2
c = 5
s = 15
n = 2
a = 5
u = 3
print(x + z) #Addition
print(y - v) #Subtraction
print(d * j) #Multiplication
print(f / t) #Division
print(b % h) #Modulus
print(l ** c) #same as 2*2*2*2*2
print(s // n) #Exponentiation
print(a != u) # Floor division

#Assignment operators

number = 0
number +=1 

print(number)

number = 5
number +=30

print(number)

number = 4

number **=3

print(number)

#logicala operators

print(10 > 5)
print(20 > 10)
print(30 >= 30)
print(40 < 30)
print(40 < 35)
print(50 <= 50)
print(60 != 59)
print(70 == 69)
print(100 + 5 * 3)

#If statement

number = 10 

if number > 0:
    print(f"{number} is Positive")
elif number == 0:
    print(number)
else:
    print(f"{number} is negative")

    number = - 100
if number > 0:
    print(f"{number} is positive")
elif number ==0:
    print(number)
else:
    print(f"{number} is negative")

    number = 1000

if number > 0:
    print(f"{number} is positive")
elif number ==0:
    print(number)
elif number ==0:
    print(number)
elif number ==0:
    print(number)
    
print("hello")
print("how are you doing")
print("it was nice nice talking to you here")

number = -1
message = "positive" if number > 0 else "0 or negative"

print(message)

number = 10
message = "negative" if number > 20 else "10 or positive"

print(message)

#If two operators have the same precedence, the expression is evaluated from left to right.
#ExampleAddition + and subtraction - has the same precedence, and therefor we evaluate the expression from left to right:

print(5 + 4 - 7 + 3) 

#Python Listsare used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets ExampleGet your own Python ServerCreate a List:

#List

print(([]))

numbers = [1, 2, 3, 4, -1, -20]

print(numbers)

numbers = [1, 2, 3, 4, -1, -20]

print(numbers[5])

numbers = [9, 8, 7, -4, -10, ["A", "B"]]

print(numbers[4])
print(numbers[5])

#Useful List methods

#numbers = [1, 1, 2, 3, 4, -1, -20]

numbers = [1, 2, 3, 4, -1, -20]

numbers.sort()
numbers.reverse()
numbers.append(1500)

print(len(numbers))
numbers.clear()
print(5 not in numbers)
print(- 20 in numbers)

#Deleting iterms from list#

#numbers.remove(1)
#numbers.remove(-20)
#numbers.remove(1)
#numbers.pop()
#numbers.pop()
#del numbers[0:7]
print(numbers)

thislist = ["apple","banana","cherry"]

print(len(thislist))

firstlist = ["orange","pawpaw","lemon_orange","plantain","grape"]

print(firstlist[0:5])

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#Ordered When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.
#Note: There are some list methods that will change the order, but in general: the order of the items will not change.
#Changeable The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow DuplicatesSince lists are indexed, lists can have items with the same value:
#ExampleLists allow duplicate values:

thislist = ["apple","banana","cherry","apple","cherry"]

print(thislist[1])

food_duplicate = ["rice","spaghetti","bread","garri","yam","indomine","yam","Spaghetti","rice"]

print(food_duplicate[9:9])

fruit_duplicate = ["water_melon","orange","black_grape","apple","water_melon","apple"]

print(fruit_duplicate[-4:-1])

#List Length<>To determine how many items a list has, use the len() function:
#ExamplePrint the number of items in the list

thislist = ["cherry","banana","apple"]

print(len(thislist))

all_list = ["grape","pawpaw","lemon","Avocado","mango","apple"]

print(len(all_list))

#List Items - Data Types
#List items can be of any data type:ExampleString, int and boolean data types:

list1 = ("apple","banana","cherry")
list2 = [1, 9, 3,  8, 6, 2]
list3 = {True, False, True, False}

print(type(list1))
print(type(list2))
print(type(list3))


number_list3 = ["mango","water_melon","pawpaw"]
number_list4 = [15,20, 30, 40, 50]
number_list5 = [False, True, False, True]

print(number_list3)
print(number_list4)
print(number_list5)

#A list can contain different data types:ExampleA list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

print(list1)

list1 = ["female", 50,"banana", False]

print(list1)

#type()From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>
#Example
#What is the data type of a list?

mylist = ["aplle","banana","cherry"]

print(type(mylist))

mylist = ["water_melon", 23, "beans"]

print(type(mylist))

myList = [1,3,True,6.5]

print(myList)
print(type(myList))

myList = [1, 2, 3, 4]
A = [myList]*3
print(A)
myList[2]=45
print(A)

myList.insert(2,4.5)
print(myList)

#The list() Constructor
#It is also possible to use the list() constructor when creating a new list.
#Example Using the list() constructor to make a List:

thislist = list(("apple","banana","cherry"))

print(thislist)

thislist = list(("water_melon","orange","grape"))

print(thislist)

thisfood =list(("rice","beans","eba","spaghetti","bread","indomine","garri","amala","fufu","yam","Dodo","Akara"))

print(thisfood)

# Set# 

numbersList = [1, 1]

numbersSet = {1, 1} 

print(numbersList)

print(numbersSet)

lettersSet = {"A", "A", "B", "C", "C"}

print(lettersSet)

# Set union intersection and differeence

lettersA = {"A","B", "C", "D", "H", "G"}
lettersB = {"A", "E", "C","F", "G"}
union = lettersA |lettersB
intersection  = lettersA & lettersB
difference = lettersA - lettersB

print(f"union = {union}")
print(f"intersection = {intersection}")
print(f"differnce = {difference}")
print(lettersA | lettersB)

#Diction

person = {
    
    "name": "jamal",
    "age": "20",
    "address": "USA"
    
}
print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())

#second steps 

print(person.get("age"))
print(person.get("name"))
print(person.get("address"))

myList = [1,3,True,6.5]

print(myList)
print(type(myList))

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:
#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
################################################################

def gcd(m,n):
     while m%n != 0:
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
     return n
    
print(gcd(20,10))

def abc(j,u):
    while j%u != 0:
        bkkj = j
        bkku = u
        
        j = bkku
        u = bkkj%bkku
        
    return j

print(abc(70,30))

import random

class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value

my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)

counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

    from urllib import request

r = request.urlopen("http://www.google.com")
print(r.getcode())
print(r.read())






