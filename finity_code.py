for n in range(2, 10):
    for x in range(2, n):
        if n % x ==0:
            print(n,'equals', x, '*', n//x)
            break
    else:
         print(n, 'is a prime number')

words = ["cat", "window", "defenestrate", "Hamburg", "Iphone- 15-pro-max"]

for w in words:
    print(w, len(w))

House = ["Television", "sound-bar", "lenvovo-computer", "printer-HP", "food-stuff", "working-office"]

for H in House:
    print(H,  len(H))

a = ["Mary", "Had", "a", "little", "lamb"]

for i in range(len(a)):
    print(i, a[i])

txt = "the best things to learn in life is python code!"
if "code" in txt:
    print("yes, 'python' is present.")

z = "awesome"

def myfunc():
    z = "fantastic"
    print("python is " + z)
    
myfunc()

print("python is " + z)

def is_prime(number):
    if number > 1:
        for num in range(2, int(number**0.5) + 1):
            if number % num == 0:
                return False
        return True
    return False

print(is_prime(2011))

def is_prime(number):
    if number > 1:
        for num in range(2, number // 2 + 1):
            if number % num == 0:
                return False
        return True
    return False

print(is_prime(941))

def is_prime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                return False
        return True
    return False

print(is_prime(4))

def abc(x,y,h):
    while  x%y%h !=0:
        nice = x
        age = y
        two = h
        
        x = nice
        y = age
        h = nice%age%two
        
    return y,h,x
print(abc(40,20,10))

worldlist = ['dog','cat','rabbit']
letterlist = []
for aworld in worldlist:
    for aletter in aworld:
        letterlist.append(aletter)
print(letterlist)

aBuilding_number = input("please enter your building_number ")

print("your house_buiding in all capital is",aBuilding_number.upper(),
      "and has length", len(aBuilding_number))

thistuple = ("apple", "banana", "cherry")
print(thistuple)
 
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

x = 10
y = "folorunso"

print(x)
print(y)

thistupple = ("apple", "banana", "cherry")

print(thistuple[-1])

thistuple = ("apple","banana","cherry","orange","mango","melon","kiwi")

print(thistuple[2:5])

thistuple = ("apple",)
print(type(thistuple))
thistuple = ("apple")
print(type(thistuple))

tuple2 = ("apple","banana","cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(tuple1)
print(tuple2)
print(tuple3)

mytuple = ("apple","banana","cheery")
print(mytuple)
print(type(mytuple))

thistuple = tuple(("apple","grape-fruit","lemon-range"))
print(thistuple)
print(type(thistuple))