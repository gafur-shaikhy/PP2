# 1
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]


print(list1)
print(list2)
print(list3)
print(list4)

# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

print(thislist)


list5 = ["apple", "banana", "cherry"]
print(list5[-1]) #last element

list6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list6[:4])
# ans : ['apple', 'banana', 'cherry', 'orange']


list7 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list7[2:])
# ans : ['cherry', 'orange', 'kiwi', 'melon', 'mango']

list8 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # от 4 по счету с конца до последнего елемента не включительно
# ans : ['orange', 'kiwi', 'melon']

list9 = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist10 = ["apple", "banana", "cherry"]
thislist10[1] = "blackcurrant"
print(thislist10) # ans : ['apple', 'blackcurrant', 'cherry']


thislist11 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist11[1:3] = ["blackcurrant", "watermelon"]
print(thislist11) # ans : ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist12 = ["apple", "banana", "cherry"]
thislist12[1:2] = ["blackcurrant", "watermelon"]
print(thislist12) # ans : ['apple', 'blackcurrant', 'watermelon', 'cherry']


thislist13 = ["apple", "banana", "cherry"]
thislist13[1:3] = ["watermelon"]
print(thislist13) # ans : ['apple', 'watermelon']


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # ans : ['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # ans : ['apple', 'orange', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # ans : ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

thislist111 = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist111.extend(thistuple)
print(thislist111)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana") # only first banana
print(thislist)

thislist = ["apple", "banana", "cherry", "banana"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print(len(thislist))  

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("*********************")


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("*********************")

list87 =  ["apple", "banana", "cherry"]
list88 = [x for x in list87]
for l in list88 :
  print(l)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

# newlist = [expression for item in iterable if condition == True]

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist.reverse()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# append()	Adds an element at the end of the list
# clear()	  Removes all the elements from the list
# copy()	  Returns a copy of the list
# count()	  Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	  Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	  Sorts the list