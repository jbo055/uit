students = [] # list of students
# we want to make a system where we can add, delete and edit students to a list
# we will use a dictionary to store the students
# the dictionary will have the keys name and id
# the name will be a string and the id will be an integer
def add_student_name():
    name = input("Enter the name of the student: ")
    return name
def add_student(students):
    print("Adding student.")
    name = str(input("Enter the name of the student: "))
    id = input("Enter the student ID: ")
    try:
        id = int(id)
    except ValueError:
        print("Invalid ID.")
        return
    # make a check for no id and input new id
    if id == 0 or id == "":
        print("Invalid ID.")
        return
    print("Student added.")
    
    # make a check 

    # if id is already used
    for student in students:
        if student["id"] == id:
            print("ID already used.")
            return
    student = {"name": name, "id": id} # Adding the student to the dictionary
    students.append(student) # Adding the student to the list of students
    #append is a method that adds an item to the end of the list
def print_students(students):
    for student in students:
        print("Name:", student["name"], "\nID: ", student["id"])
def search_student_id(students, search_id):
    for student in students:
        if student["id"] == search_id:
            print("Student found.")
            print("Name:", student["name"], "\nID: ", student["id"])
            break
    else:
        print("Student not found.")
def search_student_name(students, search_name):
    for student in students:
        if student["name"] == search_name:
            print("Student found.")
            print("Name:", student["name"], "\nID: ", student["id"])
            break
    else:
        print("Student not found.")



choice = 0
while choice != 4:
    choice = int(input("Welcome to student administration. \n1. Add student. \n2. Print students. \n3. Search for student. \n4. Leave menu. \nChoose an option: "))

    if choice == 1:
        print("Adding students.")
        students_amount = int(input("Enter the amount of students you want to add: "))
        if students_amount == 0:
            print("No students added.")
            continue
        for i in range(students_amount):
            add_student(students)

    elif choice == 2:
        print("Printing students.")
        print_students(students)

    elif choice == 3:
        print("Searching for student.")
        search_choice = int(input("1. Search by name. \n2. Search by ID. \nChoose an option: "))
        if search_choice == 1:
            search_name = input("Enter the name of the student you want to search for: ")
            search_student_name(students, search_name)
        elif search_choice == 2:
            search_id = int(input("Enter the ID of the student you want to search for: "))
            search_student_id(students, search_id)
        else:
            print("Invalid choice.")

    
    elif choice == 4:
        print("Leaving menu.")
        break
    
    else:
        print("Invalid choice.")
        continue





# students = [student]
# print(students)
# print_students(students)



