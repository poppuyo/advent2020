class Day18:
    def __init__(self):
        self.input = []
        self.load_input()
        print(f'pt1: {self.solve_part_1()}')
        print(f'pt2: {self.solve_part_2()}')

    def load_input(self):
        f = open("../inputs/day18.txt", "r")
        txt = f.read()
        self.input = txt.split('\n')

    @staticmethod
    def solve_line(line):
        open_parens = []
        close_parens = []

        for i in range(len(line)):
            if line[i] == '(':
                open_parens.append(i)
            elif line[i] == ')':
                close_parens.append(i)
            else:
                continue

        if len(open_parens) != len(close_parens):
            raise RuntimeError(f'mismatched paren count: (:{len(open_parens)},):{len(close_parens)}')
        print(open_parens)
        print(close_parens)

        for

    @staticmethod
    def solve_inner(expr):
        result = []
        stored_left_num = None

        cur = 0
        while not ''.join(result).isdecimal():
            if expr[cur].isdecimal():
                stored_left_num = int(expr[i])
            elif expr[cur] == '+':
                stored_left_num + expr[i+1]




    def solve_part_1(self):
        print(Day18.solve_line(self.input[0]))

    def solve_part_2(self):
        return



# Day18()
