from utils.student import insert_student, find_student
from utils.file_helper import read_students, save_students

if __name__ == '__main__':
    filename = 'db.json'
    data = read_students(filename)
    while(True):
        print("Choices:\n1. Insert student\n2. Print marks of a student\n3. Print all student marks\n4. Save and exit")
        choice = int(input("Enter choice: "))
        match(choice):
            case 1:
                insert_student(data)
            case 2:
                name = input("Enter name of student to search: ")
                student = find_student(data, name)
                if student:
                    student.print_details()
                else:
                    print("No student found!")
            case 3:
                for student in data:
                    student.print_details()
            case 4:
                save_students(data, filename)
                print("Data has been saved successfully!!")
                exit()
            case _:
                print("Invalid choice")
