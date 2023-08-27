class Student:
    """
    Returns a student object with name and other details
    """
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.physics, self.maths, self.english = marks

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "physics": self.physics,
            "maths": self.maths,
            "english": self.english,
        }

    def total_marks(self):
        return self.physics + self.maths + self.english
    
    def print_details(self):
        print("Total mark of %s aged %d is %d" % (self.name, self.age, self.total_marks()))


def insert_student(data):
    """
    Function to insert a student to the data.

    :arg data: List of students

    :return: Updated list of students
    """
    name = input("Enter name of student: ")
    age = int(input("Enter age of student: "))
    subjects = ('Physics', 'Maths', 'English')
    all_marks = []
    for subject in subjects:
        marks = int(input("Enter marks for %s: " % subject))
        all_marks.append(marks)

    student = Student(name, age, all_marks)
    data.append(student)
    return data

def find_student(data, name):
    """
    Function to search a student in data.

    :arg data: List of students
    :arg name: Name of stuent to be searched

    :return: if the student is found, else None
    """
    for student in data:
        if student.name == name:
            return student
        
    return None