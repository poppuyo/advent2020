import re


class Day2:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day2.txt", "r")
        txt = f.read()
        raw_input = txt.splitlines()
        regex = r'(\d+)-(\d+) (\w): (\w+)'
        for line in raw_input:
            vals = re.findall(regex, line)[0]
            self.input.append([int(vals[0]), int(vals[1]), vals[2], vals[3]])

    def solve_part_1(self):
        valid = 0
        # [0] - lower bound count
        # [1] - upper bound count
        # [2] - letter must be found between [0] and [1] times
        # [3] - password
        for item in self.input:
            valid += 1 if item[0] <= item[3].count(item[2]) <= item[1] else 0
        print(valid)

    def solve_part_2(self):
        valid = 0
        # [0] - position 1 (1-indexed!)
        # [1] - position 2 (1-indexed!)
        # [2] - letter to be found at [0] xor [1]
        # [3] - password
        for item in self.input:
            valid += 1 if bool(item[3][item[0] - 1] == item[2]) ^ bool(item[3][item[1] - 1] == item[2]) else 0
        print(valid)


Day2()
