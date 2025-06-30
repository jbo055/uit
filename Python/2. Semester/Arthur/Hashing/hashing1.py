
def simple_hashing(text):
    #ASCII Table is important when it comes to hashing - To create encrypted data
    hash_value = 0
    # We want to transform the data into the new data - We encrypt the data based on the shift in the ASCII table.
    for char in text:
        hash_value = (hash_value * 31 + ord(char) % (10**8)) # We shift the data by 31 and take the modulo of 10^8 to keep it within a certain range.
    return hash_value

def hashing_function_2(text): # Shift and XOR
    hash_value = 5381
    # Hex hash - A combination of bitwise shifting and XOR
    for char in text:
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
        # Bitwise shift
    return hash_value & 0xFFFFFFFFFFFFFFFF # We want to keep the hash value within a certain range.

def main():
    teststring = "hhhhkjotyerk"
    print(teststring)
    print(simple_hashing(teststring))
    print(hashing_function_2(teststring))


if __name__ == "__main__":
    main()