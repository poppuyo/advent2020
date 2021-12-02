class Day2:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day2.txt", "r")
        txt = f.read()
        temp_input = txt.splitlines()
        for line in temp_input:
            a, b = line.split(" ")
            self.input.append((a, int(b)))

    def solve_part_1(self):
        h_pos = 0
        d_pos = 0
        for command, value in self.input:
            if command == "forward":
                h_pos += value
            elif command == "up":
                d_pos -= value
            else:
                d_pos += value
        print(f'h_pos:{h_pos}, d_pos: {d_pos}, product: {h_pos*d_pos}')

    def solve_part_2(self):
        h_pos = 0
        d_pos = 0
        a_pos = 0
        for command, value in self.input:
            if command == "forward":
                h_pos += value
                d_pos += a_pos * value
            elif command == "up":
                a_pos -= value
            else:
                a_pos += value
        print(f'h_pos:{h_pos}, d_pos: {d_pos}, product: {h_pos*d_pos}')
        return


Day2()
