# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# I created new line for already exist file
f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "a")
f.write("Now the file has more content!")

print("-----------------------------------")
#open and read the file after the appending:
f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "r")
print(f.read())


# Полностью удвлить содержащий и перезапишет
# f = open("/Users/Lenovo/Desktop/PP2/laboratories/lab_06/lecture_06/demofile.txt", "w")
# f.write("Now the file has more content!")

