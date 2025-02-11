print("  -------------- 1 ---------------------" , "\n")
N = int(input("print N: "))

def gen():
    finish = 0
    while(finish <= N):
        n = finish**2
        print(n)
        finish = finish + 1
gen()

print("\n"," -------------- 2 ---------------------", "\n")