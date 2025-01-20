import random
students = []
chosen_students = []

def add_students():
    amount_of_students = int(input("How many students do you want to add? "))
    for i in range(amount_of_students):
        student = input("Enter the name of the student: ")
        students.append(student)

def generate_random_students():
    nr_students = int(input("Enter the number of students to choose: "))
    chosen_students = random.choices(students, k = nr_students)
    for student in chosen_students:
        return student


if __name__ == "__main__":
    choice = 0
    while choice != 5:
        choice = int(input("1. Add students. \n2. Generate random students. \n3. Print chosen students. \n4. Print all students. \n5. Exit. \nChoose an option: "))
        if choice == 1:
            add_students()
        elif choice == 2:
            generate_random_students()
        elif choice == 3:
            print(chosen_students)

    
    #press 1 for adding students

    #press 2 for generating random students
    #press 3 for printing students
    # chosen_students = []
    # chosen_students = choose_students(students, nr_students)


    # play_game()