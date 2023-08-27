from utils import (
    insert_student,
    print_student_total,
    print_all_student,
    save_students,
    read_students,
)

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
                name = input("Enter name of student: ")
                print_student_total(data, name)
            case 3:
                print_all_student(data)
            case 4:
                save_students(data, filename)
                print("Data has been saved successfully!!")
                exit()
            case _:
                print("Invalid choice")
