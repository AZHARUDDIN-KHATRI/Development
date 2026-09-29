
class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Marks: {self.marks}")

class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, name, roll_no, marks):
        std = Student(name, roll_no, marks)
        self.students.append(std)
        print("Student added successfully.")

    def show_students(self):
        if not self.students:
            print("No records found.")
        for std in self.students:
            std.display()

    def search_student(self, roll_no):
        for std in self.students:
            if std.roll_no == roll_no:
                print("Record Found:")
                std.display()
                return std
        print("Student not found.")
        return None

    def delete_student(self, roll_no):
        std = self.search_student(roll_no)
        if std:
            self.students.remove(std)
            print("Student deleted successfully.")
