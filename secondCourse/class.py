class Student:
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_name(self):
        print(self.name)

    def print_score(self):
        print(self.score)

stud1=Student("Tom",99)
stud1.print_name()