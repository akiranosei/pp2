"""
a=5
b=3
if (a>b):
   print("True")
else:
   print("False")

print(bool("Hello"))
True

print(bool())
False

print(bool(0))
False

print(bool("None"))
False

def myFunction() :
  return True

print(myFunction())
True

x = 200.0
print(isinstance(x, int))
False

print((6 + 3) - (6 + 3))
0

x = 5
x += 3
print(x)
8

mylist = ["apple", "banana", "cherry","cherry","apple"]
print(mylist)
print(len(thislist))
5

mylist = ["apple", "banana", "cherry"]
print(type(mylist))
<class 'list'>

thislist = ["apple", "banana", "cherry"]
print(thislist[1])
banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
['apple', 'blackcurrant', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
['apple', 'banana', 'cherry', 'orange']

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
['apple', 'cherry', 'banana', 'kiwi']

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
['apple', 'banana']

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
[]

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
apple
banana
cherry

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #instead of for

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

newlist = [x for x in fruits if x != "apple"]

newlist = [x for x in range(10)]
print(newlist)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
['apple', 'orange', 'cherry', 'kiwi', 'mango']

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #descending

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) #slice copy operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.append(list2)
list1.extend(list2)
print(list1)

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

x = ("apple", "banana", "cherry") #convert to list beforehand
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
apple
banana
cherry

asterisk to assign as a list, not only variable

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #the same tuple x2
print(mytuple)

myset = {"apple", "banana", "cherry"} #any order of printing

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #od discard()
print(thisset)

x = thisset.pop() #random value deleting

thisset.clear()
del thisset

union() + update() #all items join |
intersection() #only duplicates &
difference() #only values not in another set -
symmetric_difference() all except duplicates ^

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} #no duplicates
print(thisdict["brand"]) Ford or get()

x = thisdict.keys()
dict_keys(['brand', 'model', 'year'])

car["color"] = "white" #to add

x = thisdict.values()
dict_values(['Ford', 'Mustang', 1964])

x = thisdict.items()
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

thisdict["year"] = 2018

thisdict.popitem() #delete last

myfamily = { #nested dictionary
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

if a > b: print("a is greater than b")
print("A") if a > b else print("B")
and or not 
if false, print pass

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
  case _: #becomes default answer
  
for x in range(6):
  print(x)
else:
  print("Finally finished!")
0
1
2
3
4
5
Finally finished!
#if put break, no else text

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry

for x in [0, 1, 2]:
  pass
#if empty loop, make error without pass

"""