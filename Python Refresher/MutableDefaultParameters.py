from typing import List
from typing import List, Optional


class Student:
    #!Bad example of type hiting and default parameter.
    #*def __init__(self, name: str, grades: List[int] = []):  
    #!This is bad! Never make a parameter to a mutable object by default, those paramters are made when the function is defined, not when its called. All objects of this class will have the same default grades
    ##Instead set the default to None and use the or function to set the grades list or an empty list. "Optional" is not needed, slightly better way of hendling
    def __init__(self, name: str, grades: Optional[List[int]] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades)
print(rolf.grades)  # Whaaaaaat