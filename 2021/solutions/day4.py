from typing import List, Tuple

class Day4:
    def __init__(self):
        self.input = []
        self.bingo_numbers = []
        self.bingo_boards = []
        self.bingo_status = []
        self.load_input()
        print(self.bingo_boards)
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day4.txt", "r")
        txt = f.read()
        lines = txt.splitlines()
        self.bingo_numbers = list(map(int, lines[0].split(',')))
        self.bingo_boards, self.bingo_status = Day4.parse_bingo_boards(lines)

    def solve_part_1(self):
        print("p1 ====================")
        winning_board: List[Tuple[int, int]]
        winning_num: int
        winning_board, winning_num = Day4.find_winning_board(self.bingo_numbers, self.bingo_boards)
        unused_nums = sum(map(lambda n: n[0] if n[1] == 0 else 0, winning_board))
        print(f'unused({unused_nums}) * winning({winning_num}) = {unused_nums*winning_num}')
        return

    def solve_part_2(self):
        print("p2 ====================")
        return

    @staticmethod
    def find_winning_board(numbers, boards):
        for num in numbers:
            for board in boards:
                if Day4.play_board_turn(board, num):
                    return board, num

    @staticmethod
    def parse_bingo_boards(raw_input: List[str], start_line=2):
        boards = []
        status_boards = []
        board = []
        status = [0]*25
        for line in raw_input[start_line:]:
            if line.strip() == '':
                boards.append(board)
                board = []
            else:
                board.extend(list(map(int, line.split())))
        # capture the last board
        boards.append(board)

        for x in range(len(boards)):
            status_boards.append(status)
        return boards, status_boards

    @staticmethod
    def play_board_turn(board: List[List[int, int]], number):
        if number not in board:
            return False
        else:
            for board_pos in board:
                if board_pos[0] == number:
                    board_pos[1] = 1
                    # check victory
                    Day4.check_win(board, number)

    @staticmethod
    def check_win(board: List[List[int, int]], winning_num):
        # win conditions: horizontal match
        if board[0][1] and board[1][1] and board[2][1] and board[3][1] and board[4][1]:
            return True
        elif board[5][1] and board[6][1] and board[7][1] and board[8][1] and board[9][1]:
            return True
        elif board[10][1] and board[11][1] and board[12][1] and board[13][1] and board[14][1]:
            return True
        elif board[15][1] and board[16][1] and board[17][1] and board[18][1] and board[19][1]:
            return True
        elif board[20][1] and board[21][1] and board[22][1] and board[23][1] and board[24][1]:
            return True

        # win conditions: vertical match
        for i in range(5):
            if sum(map(lambda x: x,board[0:5][1])) == 5:
                # do stuff
                break

        return False


Day4()
