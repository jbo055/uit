class EightQueens:
    def __init__(self, queen_list: list = 8 * [-1]):
        self.queens = queen_list

    # Returns the column the queen is at.
    def get(self, queen_id: int) -> int:
        if queen_id > 7 or queen_id < 0:
            print("Queen id out of range of list. Select between 0-7")
            return -1
        return self.queens[queen_id]

    # Sets the queen at a row to a column
    def set(self, queen_id: int, queen_placement: int):
        if queen_id > 7 or queen_id < 0:
            print("Queen id out of range of list. Select between 0-7")
        else:
            self.queens[queen_id] = queen_placement

    # Checks if a queen can reach another queen in 1 move.
    # A Queen moves diagonally, horizontaly and vertically.
    # If it could hit another queen in while moving it returns false
    # If no queen can move to another queen, it returns true
    def isSolved(self) -> bool:
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                if self.queens[i] == self.queens[j]:
                    # Same column
                    return False
                if abs(self.queens[i] - self.queens[j]) == abs(i - j):
                    # Same diagonal
                    return False
        return True

    # Prints the board, with a Q representing the queen
    def print_board(self):
        for i in range(len(self.queens)):
            line = ''
            for j in range(0,8,1):
                if j == self.get(i):
                    line += ' Q'
                else:
                    line += ' -'
            print(line)            




    



def main():
    board1 = EightQueens([0,1,2,3,4,5,6,7])

    print(str(board1.get(0)))
    board1.set(0,7)
    board1.set(7,0)
    print(str(board1.get(0)))

    print("###")
    board2 = EightQueens([0,4,7,5,2,6,1,3])

    board1.print_board()
    print("###")
    board2.print_board()
    print("Board 1 is Solved: " + str(board1.isSolved()))
    print("Board 2 is Solved: " + str(board2.isSolved()))

if __name__ == "__main__":
    main()