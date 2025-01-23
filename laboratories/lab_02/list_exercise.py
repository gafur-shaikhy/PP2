# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets

print(thislist)

mylist = ['apple', 'banana', 'banana 2', 'cherry']
print(mylist[2]) # ans : banana 2

# List items cannot be removed after the list has been created.
# ans : False
# examples : 
numbers = [1, 2, 3, 4, 5]
numbers.remove(2)
print(numbers) # ans : [1, 2, 4, 5]


list1 = [7, 8, 9, 10, 11]
deleted = list1.pop(2)
print(deleted) # ans : 9
print(list1) #ans : [7, 8, 10, 11]


# for count number of element
list2 = ['apple', 'banana', 'cherry']
print(len(list2)) # ans : 3  

list3 = ['apple', 'banana', 'cherry']
print(list3[-1]) # ans : cherry

list4 = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(list4[1:4]) # ans : ['banana', 'cherry', 'orange']

list5 = ['sport', 'football', 'tennis', 'Gym', 'Aim']
print(list5[1: 4]) # ans : ['football', 'tennis', 'Gym']

fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'

mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

list6 = ['ggg', 'hhh', 'aaa', 'sss']
list6.append('gafur')
print(list6)

list7 =  ['ggg', 'hhh', 'aaa', 'sss']
list7.insert(2, 'PP2')
print(list7)

list8 =  ['ggg', 'hhh', 'aaa', 'sss']
list9 = ['fff', 'bbb', 'kkk']
list8.extend(list9)
print(list8)


list10 = ['nnn', 'kk', 'hj', 'djf']
list10.remove('nnn')
print(list10)

list11 = ['jj', 'dhd', 'kds', 'yyy']
list11.pop(2)

list12 = ['kkk', 'ttt', 'nnn', 'cr7']
list12.pop()
print(list12)
