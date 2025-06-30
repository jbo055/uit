import string

def read_words_from_file(filename):
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            text = text.translate(str.maketrans("", "", string.punctuation))
            words = set(text.split())
        return words
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def get_filenames():
    file1 = input("Enter the first filename: ").strip()
    file2 = input("Enter the second filename: ").strip()
    return file1, file2    

def main():
    
    file1, file2 = get_filenames()

    words1 = read_words_from_file(file1)
    words2 = read_words_from_file(file2)
    
    if not words1 or not words2:
        print("Could not compare files.")
    else:
        union_words = words1 | words2
        intersecting_words = words1 & words2
        unique_to_file1 = words1 - words2
        unique_to_file2 = words2 - words1
        symmetric_difference_words = words1 ^ words2

        # Viser antallet unike ord i begge filer (lengde av union() (operator |) de to mengdene)
        print(f"Antall unike ord i fil 1: {len(words1)}")
        print(f"Antall unike ord i fil 2: {len(words2)}")

        # Viser alle unike ord i begge filer (union()  (operator |) av de to mengdene)
        print(f"Unike ord i begge filer: {union_words}")

        # Viser alle unike ord som forekommer både i første og andre fil (intersection() (operator & av de to mengdene)
        print(f"Unike ord som forekommer i begge filer: {intersecting_words}")

        # Viser alle unike ord som forekommer i første fil, men ikke i andre (difference() (operator -))
        print(f"Unike ord i fil 1: {unique_to_file1}")

        # Viser alle unike ord som forekommer i andre fil, men ikke i første (difference() (operator -))
        print(f"Unike ord i fil 2: {unique_to_file2}")

        # Viser alle ord som forekommer enten i første eller andre, men ikke i begge (symmetrisk differanse (operator ^))
        print(f"Unike ord i fil 1 eller fil 2: {symmetric_difference_words}")


if __name__ == "__main__":
    main()