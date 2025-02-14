N = int(input("print N: "))

print("  -------------- 1 ---------------------" , "\n")

def gen1():
    finish = 0
    while(finish <= N):
        n = finish**2
        print(n)
        finish = finish + 1
gen1()

print("\n"," -------------- 2 ---------------------", "\n")

def gen2():
     for x in range(N):
        if x % 2 == 0:
            print(x)

gen2()

print("\n"," -------------- 3 ---------------------", "\n")

def gen3():
    for y in range(N):
        if (y % 3 == 0) or (y % 4 == 0):
            print(y)

gen3()

print("\n"," -------------- 4 ---------------------", "\n")

a = int(input("print a: "))
b = int(input("print b: "))

def gen4():
    for z in range(a, b + 1):
        print(z**2)

gen4()

print("\n"," -------------- 5 ---------------------", "\n")

n = int(input("print n: "))
numbers = []
def gen5():
    for i in range(n + 1):
        numbers.append(i)

gen5()
numbers = numbers[::-1]

for j in range(len(numbers)):
    print(numbers[j])