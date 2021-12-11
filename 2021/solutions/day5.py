import copy

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

    def solve_part_1(self):
        print("p1 ====================")

    def solve_part_2(self):
        print("p2 ====================")


Day5()
