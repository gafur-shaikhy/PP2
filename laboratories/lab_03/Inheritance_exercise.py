class Synyp:
    def __init__(self, letter, curator, student):
        self.let = letter
        self.cur = curator
        self.stu = student

    def print1(self):
        print(f"Letter: {self.let}, Curator: {self.cur}, Student: {self.stu}")


class General(Synyp):
    def __init__(self, letter, curator, student, graduation):
        super().__init__(letter, curator, student)
        self.gra = graduation

    def print_all(self):
        print("2nd part")
        print(f"Letter: {self.let}, Curator: {self.cur}, Student: {self.stu}, Graduation: {self.gra}")

x = General("b", "Raya_Bodykova", "Gafur_Shaikhy", 2024)
x.print1()
x.print_all()
