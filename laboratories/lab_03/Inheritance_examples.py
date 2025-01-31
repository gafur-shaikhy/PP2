class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
       super().__init__(fname, lname)
       

x = Student("Mike", "Olsen")
x.printname()

print("***********************")

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, grade):
        super().__init__(fname, lname) 
        self.grade = grade 

    def printinfo(self):
        print(f"Name: {self.firstname} {self.lastname}, Grade: {self.grade}")

s1 = Student("Mike", "Olsen", "B")
s1.printname()  # Mike Olsen
s1.printinfo()  # Name: Mike Olsen, Grade: B

print("***********************")

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()