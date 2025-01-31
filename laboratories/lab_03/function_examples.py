def my_function():
  print("Hello from a function")
my_function() 


def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

def my_function(*kids): # при обратной вызове функции может принять не произвольное количество функции
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid): # две ** значить при вызове должен быть ключ значение
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function(x, y):
  print(x, y)
my_function(3, 7)


def my_function(a, b, /, c, *, d):
    print(a, b, c, d)
my_function(1, 2, 3, d=4)  # ✅ Работает
my_function(1, 2, c=3, d=4)  # ✅ Работает
# my_function(a=1, b=2, c=3, d=4)  # ❌ Ошибка (a и b должны быть только позиционными)
# my_function(1, 2, 3, 4)  # ❌ Ошибка (d должно быть только именованным)

def my_function(*, x): #все оргументы после должны передавтся только по ключ = значение
    print(x)
my_function(x=3)  # ✅ Работает
#my_function(3)   ❌ Ошибка!

print("*********************************************")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
    print(result)
  return result
print("Recursion Example Results:")
tri_recursion(6)