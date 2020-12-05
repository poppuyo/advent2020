class Day5:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day5.txt", "r")
        txt = f.read()
        self.input = txt.splitlines()

    def parse_seat(self, seat_string):
        row = 0
        col = 0
        row_range = list(range(0, 128))
        col_range = list(range(0, 8))
        for letter in seat_string:
            if letter == 'F':
                row_range = row_range[0:int(len(row_range)/2)]
            elif letter == 'B':
                row_range = row_range[int(len(row_range)/2):]
            elif letter == 'L':
                col_range = col_range[0:int(len(col_range)/2)]
            elif letter == 'R':
                col_range = col_range[int(len(col_range)/2):]

        return row_range[0], col_range[0]

    def solve_part_1(self):
        highest_id = 0
        for seat in self.input:
            r, c = self.parse_seat(seat)
            sid = r*8 + c
            highest_id = sid if sid > highest_id else highest_id
        print(highest_id)

    def solve_part_2(self):
        seat_range = list(range(0, 8*127))
        for seat in self.input:
            r, c = self.parse_seat(seat)
            sid = r*8 + c
            seat_range.remove(sid)

        # cut front-half of contiguous seats (invalid seats)
        trim_id = 0
        while True:
            if seat_range[trim_id] + 1 == seat_range[trim_id + 1]:
                trim_id += 1
            else:
                seat_range = seat_range[trim_id + 1:]
                break
        print(seat_range[0])


Day5()
