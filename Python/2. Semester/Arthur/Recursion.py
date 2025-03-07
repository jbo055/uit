def first_recursive_function(counter):
    if counter <= 0: # Basis condition
        print("Done!")
        return
    else:
        first_recursive_function(counter - 1) # Recursive call
        print("Tada!", counter)

first_recursive_function(10)