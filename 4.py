print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
  print(isinstance(x, int))

  print(100 + ~3)

  """
  Bitwise NOT has higher precedence than addition, and needs to be evaluated first.
  The calculation above reads 100 + -4 = 96
  """
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)

thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)
#['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)

#['apple', 'watermelon']

thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist)

#['apple', 'banana', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist)
#['apple', 'banana',  'cherr', 'orange']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#['apple', 'cherry', 'banana', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#['apple', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#['banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#[]

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#['apple', 'banana', 'mango']
#same thing, same thing, but differrent
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#['banana', 'kiwi', 'mango', 'orange', 'pineapple']

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#['pineapple', 'orange', 'mango', 'kiwi', 'banana']

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#['banana', 'cherry', 'Kiwi', 'Orange']

thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist)
#['cherry', 'Kiwi', 'Orange', 'banana']

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#['a', 'b', 'c', 1, 2, 3]

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
# _2

thistuple = ("apple",)
print(type(thistuple))
#<class 'tuple'>


#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#<class 'str'>

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
#('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#('orange', 'kiwi', 'melon')

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
# Yes, 'apple' is in the fruits tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#("apple", "kiwi", "cherry")

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)

#('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#('banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#cherry

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#apple
#banana
#['cherry', 'strawberry', 'raspberry']

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
#apple
#['mango', 'papaya', 'pineapple']
#cherry

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
#('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)
#_2

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#_3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)
#{'cherry', 'apple', 'banana'}
#{1, 3, 5, 7, 9}
#{False, True}

set1 = {"abc", 34, True, 40, "male"}

print(set1)
#{True, 34, 40, 'male', 'abc'}

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#banana
#cherry
#apple

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#True

thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)
#False

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#{'cherry', 'banana', 'apple', 'orange'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
#{'banana', 'cherry', 'apple', 'orange', 'kiwi'}

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#{'apple', 'cherry'}

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#{'cherry', 'apple'}

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal
#apple
#{'banana', 'cherry'}

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
#set()

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
#NameError: name 'thisset' is not defined

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#{'c', 2, 'b', 3, 1, 'a'}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#{'c', 'b', 1, 'a', 2, 3}

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#{Elena, cherry, 2, 'c', apple, 'b', 'a', John, banana, 3, 1}

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#{'apple'}

set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

#{'banana', 'cherry'}

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
#frozenset({'cherry', 'apple', 'banana'})
#<class 'frozenset'>

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))
#True
#False

#Subset
a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)
#True
#True
#True

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#Mustang

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
#Mustang

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#dict_keys(['brand', 'model', 'year'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#dict_keys(['brand', 'model', 'year'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

#dict_keys(['brand', 'model', 'year'])
#dict_keys(['brand', 'model', 'year', 'color'])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#dict_values(['Ford', 'Mustang', 1964])
#dict_values(['Ford', 'Mustang', 2020])

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Yes, 'model' is one of the keys in the thisdict dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#{'brand': 'Ford', 'year': 1964}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
#{'brand': 'Ford', 'model': 'Mustang'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#{'brand': 'Ford', 'year': 1964}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#{}

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
#Ford
#Mustang
#1964

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
#brand
#model
#year

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
#brand Ford
#model Mustang
#year 1964

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

if a > b: print("a is greater than b")
#"a is greater than b"

a = 2
b = 330
print("A") if a > b else print("B")
#B

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")
#=

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
#Thursday

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
#Looking forward to the Weekend

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
#A weekday in May

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''
1
2
3
4
5
i is no longer less than 6
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''
1
2
4
5
6
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#apple