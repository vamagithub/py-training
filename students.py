# List
# a = [1, 2, 3, 4]

# Tuple
# a = (1, 2, 3)

# Dict
# student = {
#     "name": "Saptak",
#     "age": 100
# }

subjects = ('Physics', 'Maths', 'English')
student =  {}
name = input("Enter name of the student: ")

student[name] = []
for subject in subjects:
    marks = int(input("Enter marks of %s: " % subject))
    student[name].append(marks)

for name, marks in student.items():
    total = sum(marks)
    print("Total marks for %s is %d" % (name, total))
