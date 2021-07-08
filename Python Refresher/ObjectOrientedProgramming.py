student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))
## __OOP__ ##
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades  = grades
    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (89, 90, 93, 78, 90) )
print(student.average())
print(student.name)
## __OR__ ##
print(Student.average(student))