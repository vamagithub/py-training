import json


def insert_student(data):
    """
    Function to insert a student to the data.

    :arg data: List of students

    :return: Updated list of students
    """
    name = input("Enter name of student: ")
    data[name] = []
    subjects = ('Physics', 'Maths', 'English')
    for subject in subjects:
        marks = int(input("Enter marks for %s: " % subject))
        data[name].append(marks)
    return data

def print_student_total(data, name):
    """
    Function to print the total marks of a student from the data.

    :arg data: List of students
    :arg name: Name of the student
    """
    total = sum(data[name])
    print("%s got toal marks: %d" % (name, total))

def print_all_student(data):
    """
    Function to print the total marks of all student.

    :arg data: List of students
    :arg name: Name of the student
    """
    print("Name\tTotal")
    print("------------")
    for name, marks in data.items():
        total = sum(marks)
        print("%s\t%d" % (name, total))

def read_students(filename):
    """
    Function to read student data from a json file.

    :arg filename: filename to read student data from

    :return: student data
    """
    with open(filename, 'r') as f:
        return json.load(f)

def save_students(data, filename):
    """
    Function to save student data to a json file.

    :arg data: student data
    :arg filename: filename to save student data
    """
    with open(filename, 'w') as f:
        json.dump(data, f)