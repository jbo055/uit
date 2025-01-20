class EQ:
    def __init__(self, queen_list: list = 8 * [-1]):
        self.queens = queen_list

    def place_queen(self, queen_id: int) -> int:
        if queen_id > 7 or queen_id < 0:
            print("Queen id out of range of list. Select between 0-7")
            return -1
        return self.queens[queen_id]

    def set(self, queen_id: int, queen_placement: int):
        if queen_id > 7 or queen_id < 0:
            print("Queen id out of range of list. Select between 0-7")
        else:
            self.queens[queen_id] = queen_placement

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

    def printBoard(self):
        for i in range(len(self.queens)):
            line = ''
            for j in range(0,8,1):
                if j == self.place_queen(i):
                    line += ' Q'
                else:
                    line += ' -'
            print(line)            

def main():

    board1 = EQ()

    board1.set(0, 2)

    board1.set(1, 4)

    board1.set(2, 7)

    board1.set(3, 1)

    board1.set(4, 0)

    board1.set(5, 3)

    board1.set(6, 6)

    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?",

        board1.isSolved())

 

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.isSolved():

        print("Eight queens are placed correctly in board 2")

        board2.printBoard()

    else:

        print("Eight queens are placed incorrectly in board 2")

if __name__ == "__main__":

    main()