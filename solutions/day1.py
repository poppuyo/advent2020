class Day1:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day1.txt", "r")
        txt = f.read()
        self.input = list(map(lambda x: int(x), txt.splitlines()))

    def solve_part_1(self):
        loop = 0
        for a in self.input:
            loop += 1
            for b in self.input[loop:]:
                if a + b == 2020:
                    print(a * b)
                    break

    def solve_part_2(self):
        data = self.input
        size = len(data)

        for i in range(0, size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if data[i] + data[j] + data[k] == 2020:
                        print(data[i] * data[j] * data[k])


Day1()
