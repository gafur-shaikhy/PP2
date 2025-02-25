f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "r")
print(f.read())

print("------------------------- 1 ----------------------------")

f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "r")
print(f.read())

print("------------------------------ 2 -------------------------")

# Return the 5 first characters of the file:
f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "r")
print(f.read(5))

print("-------------------------- 3 ----------------------------")
# --------------------------------------------------------- #

# Read one line of the file:
print("----------------------------- 4 -------------------------------")
f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "r")
print((f.readline()))

print("---------------------------- 5 ---------------------------")
# Read all lines in file
f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "r")
for i in f:
    print(i)


