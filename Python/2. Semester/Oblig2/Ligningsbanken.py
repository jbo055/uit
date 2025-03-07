import random

def generate_equation():
    while True:
        a = random.randint(-9, 9)
        b = random.randint(-9, 9)
        c = random.randint(-9, 9)
        
        if a == c:
            continue  # Skip invalid equations where a == c
        
        # Ensure (d - b) is divisible by (a - c) to get a whole number solution
        d = b + (a - c) * random.randint(-9, 9)
        
        equation = f"{format_coefficient(a)}x {format_constant(b)} = {format_coefficient(c)}x {format_constant(d)}"
        solution = (d - b) // (a - c)
        return equation, solution
    


def format_coefficient(coef):
    if coef == 1:
        return ""
    elif coef == -1:
        return "-"
    else:
        return str(coef)

def format_constant(const):
    if const > 0:
        return f"+ {const}"
    elif const < 0:
        return f"- {-const}"
    else:
        return ""

def generate_equations_for_students(students): # students = ['John', 'Maria', 'Fredrick',"Sara","Julia"]
    student_equations = {}
    for student in students:
        equations = []
        solutions = []
        student_answers = []
        for _ in range(4):
            eq, sol = generate_equation()
            equations.append(eq)
            solutions.append(sol)
        student_equations[student] = {"equations": equations, "solutions": solutions, "answers": student_answers}
            # lag ligninger og legg til i listene equations og solutions
        # lag dictionary for studenten og indekser med
        # 'equations', 'solutions' og 'answers' for listene 
    return student_equations
    
def student_session(student_equations):
    student_name = input("Enter student name: ")
    if student_name not in student_equations:
        print(f"Student {student_name} not found")
        return
    
    student_data = student_equations[student_name]

    for i, equation in enumerate(student_data["equations"]):
        print(f"Solve the equation: {equation}")
        answer = int(input("Enter your answer: "))
        student_data["answers"].append(answer)

    correct_answers = 0

    print(f"Results for {student_name}")
    for i in range(len(student_data["equations"])):
        print(f"Equation: {student_data['equations'][i]}")
        print(f"Correct answer: {student_data['solutions'][i]}")
        print(f"Your answer: {student_data['answers'][i]}")
        if student_data["solutions"][i] == student_data["answers"][i]:
            correct_answers += 1
            print("Correct!")
        else:
            print("Incorrect!")

    print(f"\nTotal correct answers: {correct_answers}/{len(student_data['equations'])}")

students = ['John', 'Maria', 'Fredrick', "Sara", "Julia"]
student_equations = generate_equations_for_students(students)

student_session(student_equations)


# Hint:
# slik legger vi til et svar for en student
# student_equations[student_name]['answers'].append(student_answer)