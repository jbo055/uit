
def first_exception():
    try:
        students = []
        for i in range(students):
            print(students[i])

        number = int(input("Enter a number: "))
        calculated = 100 / number # Dette kan bli en ZeroDivisionError
        print(calculated)
    except Exception as e: # Dette kan være mange forskjellige exceptions
        print("An error occurred.", e)
    except ValueError as e:
        print("There is something wrong with a value", e)
    except ZeroDivisionError as e:
        print("Division by zero har occured", e)
    finally:
        print("This will always run")

first_exception()