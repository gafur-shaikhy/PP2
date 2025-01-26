thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

fruits = ("apple", "banana", "cherry")
print(fruits[1])

print(11111111111111111111)

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

print(11111111111111111111)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print(1111111111111111111111)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

print(11111111111111)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

print(1111111111111)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)


thistuple = ("aa", "bb", "cc")
print(thistuple.count("aa"))

