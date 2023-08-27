import json

from utils.student import Student


def read_students(filename):
    """
    Function to read student data from a json file.

    :arg filename: filename to read student data from

    :return: student data
    """
    data = []
    json_data = []
    with open(filename, 'r') as f:
        json_data = json.load(f)

    for student_json in json_data:
        student = Student(
            student_json['name'],
            student_json['age'],
            [
                student_json['physics'],
                student_json['maths'],
                student_json['english'],
            ]
        )
        data.append(student)

    return data

def save_students(data, filename):
    """
    Function to save student data to a json file.

    :arg data: student data
    :arg filename: filename to save student data
    """
    json_data = []
    for student in data:
        json_data.append(student.to_json())
    with open(filename, 'w') as f:
        json.dump(json_data, f)