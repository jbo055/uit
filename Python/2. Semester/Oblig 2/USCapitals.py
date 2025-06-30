
def create_dictionary(filename):
    try:
        with open(filename, "r") as file:
            capitals = {}
            for line in file:
                state, capital = line.strip().split(",")
                capitals[state] = capital
        return capitals
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def get_state(capitals):
    while True:
        state = input("Enter the name of a state: ").strip().title()
        if state in capitals:
            return state
        else:
            print("Could not find state.")

def main():
    capitals = create_dictionary("USCapitals.txt")
    if not capitals:
        print("Could not read file.")
        return
    
    state = get_state(capitals)
    capital = capitals[state]
    print(f"The capital of {state} is {capital}.")

if __name__ == "__main__":
    main()