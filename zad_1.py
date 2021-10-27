# Zadanie 1 lab_4
class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        return self.marks > 50



if __name__ == '__main__':
    student_1 = Student("adam", 79)
    student_2 = Student("kacper", 39)
    print(student_1.is_passed())
    print(student_2.is_passed())