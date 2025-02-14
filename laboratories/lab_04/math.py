import math

print("\n"," -------------- 1 ---------------------", "\n")

pi = math.pi
x = int(input("Input degree: "))
rad = x * (pi / 180)
print(round(rad, 10))

print("\n"," -------------- 2 ---------------------", "\n")

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print(f'Expected Output: {h*(a + b)/2}')

print("\n"," -------------- 3 ---------------------", "\n")

n = float(input("Input number of sides: "))
a = float( input("Input the length of a side: "))
each_degree = (math.pi*(n-2))/(2*n)
each_area = math.tan(each_degree)* (a*a/4)
print(each_area * n)

print("\n"," -------------- 4 ---------------------", "\n")

a = float(input("Length of base: ") )
b = float(input("Height of parallelogram: "))
print("Expected Output: ", a * b)