# write a program that prompts the user to enter a point (x, 7) and checks whether the point is withing the circle centered at (0, 0) with radius 10. 
# for example, (4, 5) is inside the circle and (9, 9) is outside the circle.

# Check if the point is inside the circle using pytagoras (a**2 + b**2 = c**2)
def check_point(x, y):
    if (x**2 + y**2) <= 10**2: # x**2 + y**2 is the distance from the center of the circle to the point
        return f"The point ({x}, {y}) is inside the circle."
    else:
        return f"The point ({x}, {y}) is outside the circle."

# Display the result
choice = 0
while choice != 2:
    choice = int(input("1. Check a circle. \n2. Exit. \nChoose an option: "))
    if choice == 1:
        x, y = eval(input("Enter the coordinates of a point (x, y): "))
        print(check_point(x, y))
    elif choice == 2:
        print("Exiting.")
    else:
        print("Invalid input.")