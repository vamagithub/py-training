a = input("Enter a number: ")
b = input("Enter another number: ")

print("Choices\n1. for addition\n2. for multiplication\n3. for power\n4. for dividing")
choice = input("Enter choice: ")

result = False

if choice == 1:
    result = a + b
elif choice == 2:
    result = a * b
elif choice == 3:
    result = a ** b
elif choice == 4:
    result = a / b

if not result:
    print("Invalid choice")
else:
    print("Result: ", result)




# # ---------------------------
# # Using match case

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))

# print("Choices\n1. for addition\n2. for multiplication\n3. for power\n4. for dividing")
# choice = int(input("Enter choice: "))

# result = False

# match choice:
#     case 1:
#         result = a + b
#     case 2:
#         result = a * b
#     case 3:
#         result = a ** b
#     case 4:
#         result = a / b

# if not result:
#     print("Invalid choice")
# else:
#     print("Result: ", result)






# # -------------------------------------
# # Square of all numbers from 1 to 10

# for i in range (10):
#     print((i + 1) ** 2)
