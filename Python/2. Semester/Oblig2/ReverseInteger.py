
def reverse_display(value):
    if value < 10: # If value is lower than 10, it only has one digit, so we can print it
        print(value, end="")
    else:
        print(value % 10, end="")
        reverse_display(value // 10)

def main():
    value = int(input("Enter an integer: "))
    reverse_display(value)

if __name__ == "__main__":
    main()