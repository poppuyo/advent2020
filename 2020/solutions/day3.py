from functools import reduce
import operator


class Day3:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day3.txt", "r")
        txt = f.read()
        self.input = txt.splitlines()

    def solve_part_1(self):
        print(self.count_impacts(0, 0, 3, 1))

    def count_impacts(self, start_x, start_y, step_x, step_y):
        x = start_x
        tree_count = 0

        for y in range(start_y, len(self.input), step_y):
            tree_count += 1 if self.input[y][x] == '#' else 0
            x = x + step_x if x + step_x < len(self.input[y]) else x + step_x - len(self.input[y])
        return tree_count

    def solve_part_2(self):
        results = []
        results.append(self.count_impacts(0, 0, 1, 1))
        results.append(self.count_impacts(0, 0, 3, 1))
        results.append(self.count_impacts(0, 0, 5, 1))
        results.append(self.count_impacts(0, 0, 7, 1))
        results.append(self.count_impacts(0, 0, 1, 2))
        print(f'{results}, {reduce(operator.mul, results)}')


Day3()
