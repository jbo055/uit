import random
import time

class Path:
    def __init__(self, num_rows, num_cols):
        self._num_rows = num_rows # Number of rows
        self._num_cols = num_cols # Number of columns
        self._square = [['*' for _ in range(num_cols)] for _ in range(num_rows)]
        self._create_path()
        self._player_pos = [0,0] # Always start at the top left corner
        self._visited = [self._player_pos]

    def _create_path(self):
        random.seed(time.time())  # Seed the random number generator with the current time
        row, col = 0, 0
        self._square[row][col] = ' '
        while row < self._num_rows - 1 or col < self._num_cols - 1:
            if row < self._num_rows - 1 and (col == self._num_cols - 1 or random.choice([True, False])):
                row += 1
            else:
                col += 1
            self._square[row][col] = ' '
        self._exit = [row, col]

    def display(self):
        for row in self._square:
            print(''.join(row))
        print(f"Player position: {self._player_pos}")

    def move(self, direction):
        # første linjer som et forslag, bruk hvis du vil :-)
        row, col = self._player_pos
        if direction == 'n':
            self._player_pos[row] -= 1
            if self._player_pos == '*':
                self._player_pos[row] += 1
                print("WALL")
            elif self._player_pos ==' ':
                
                print("OK")
        elif direction == 's':
            self._player_pos[row] += 1
            if self._player_pos == '*':
                self._player_pos[row] -= 1
                print("WALL")
            elif self._player_pos ==' ':
                
                print("OK")
        elif direction == 'e':
            self._player_pos[col] += 1
            if self._player_pos == '*':
                self._player_pos[col] -= 1
                print("WALL")
            elif self._player_pos ==' ':
                
                print("OK")
        elif direction == 'w':
            self._player_pos[col] -= 1
            if self._player_pos == '*':
                self._player_pos[col] += 1
                print("WALL")
            elif self._player_pos ==' ':
                
                print("OK")
        else:
            print("Invalid direction (legal = n, s, e, w)")
            return
    
    
        # din kode for de andre tilfellene...

# Example usage
path = Path(5, 5)
path.display()

while path._player_pos != path._exit:
    direction = input("Enter direction (n, e, w, s): ").strip().lower()
    path.move(direction)
    path.display()