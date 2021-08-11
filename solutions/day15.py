class Day15:
    def __init__(self):
        self.input = []
        self.memory = {}
        self.load_input()
        # print(self.input)
        print(f'pt1: {self.solve_part_1(2020)}')
        # print(self.memory)
        print(f'pt2: {self.solve_part_2()}')

    def load_input(self):
        f = open("../inputs/day15.txt", "r")
        txt = f.read()
        self.input = list(map(int, txt.split(',')))

    def solve_part_1(self, turn_count):
        turn = 1
        r = self.input
        prev = {}
        for i in range(0, len(self.input)):
            prev[self.input[i]] = [i + 1]
        turn += len(self.input)

        for i in range(len(self.input), turn_count):
            val = self.ply(r[i - 1], turn, prev)
            r.append(val)
            turn += 1
        return r[-1]

    def ply(self, num, turn, prev_dict):
        ret = -1
        # print(f't{turn},n:{num}')
        if num not in prev_dict.keys():
            ret = 0
        elif len(prev_dict[num]) > 1:
            ret = prev_dict[num][-1] - prev_dict[num][-2]
        else:
            ret = 0

        if ret not in prev_dict.keys():
            prev_dict[ret] = [turn]
        else:
            prev_dict[ret].append(turn)
        # print(f't{turn},n:{num},ret:{ret}')
        return ret

    def solve_part_2(self):
        return self.solve_part_1(30000000)


Day15()
