import re

class Day5:
    def __init__(self):
        self.input = []
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day5.txt", "r")
        txt = f.read()
        temp_input = txt.splitlines()
        for line in temp_input:
            points = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
            if len(points.groups()) != 4:
                raise RuntimeError
            a_line = [[int(points.group(1)), int(points.group(2))], [int(points.group(3)), int(points.group(4))]]
            if max(a_line[0][0], a_line[1][0]) > self.max_x:
                self.max_x = max(a_line[0][0], a_line[1][0])
            if max(a_line[0][1], a_line[1][1]) > self.max_y:
                self.max_y = max(a_line[0][1], a_line[1][1])
            is_hor_or_vert = a_line[0][0] == a_line[1][0] or a_line[0][1] == a_line[1][1]
            self.input.append([a_line, is_hor_or_vert])
        # print(self.input)
        # print(self.max_x, self.max_y)

    @staticmethod
    def build_map(x_size, y_size, line_data, ignore_diags=True):
        hit_map = [[0]*(x_size+1) for y in range(y_size + 1)]
        # print(hit_map)
        for vent_line in line_data:
            # print(vent_line)
            if ignore_diags and not vent_line[1]:
                continue
            else:
                hits_to_process = [*Day5.get_path(vent_line[0][0], vent_line[0][1])]
                for x, y in hits_to_process:
                    hit_map[y][x] += 1

        # Day5.show_map(hit_map)
        return hit_map

    @staticmethod
    def show_map(hit_map):
        for y in hit_map:
            print(f'{y}')

    @staticmethod
    def get_path(start, end):
        line_path = []

        x_seq_end = end[0]
        if start[0] > end[0]:
            x_seq_end -= 1
        elif start[0] < end[0]:
            x_seq_end += 1

        y_seq_end = end[1]
        if start[1] > end[1]:
            y_seq_end -= 1
        elif start[1] < end[1]:
            y_seq_end += 1

        x_list = [*range(start[0], x_seq_end, -1 if start[0] > end[0] else 1)]
        y_list = [*range(start[1], y_seq_end, -1 if start[1] > end[1] else 1)]

        if len(x_list) == len(y_list):
            # diagonal case
            line_path = zip(x_list, y_list)
        elif len(x_list) == 0:
            # vertical case
            line_path = zip([start[0]]*len(y_list), y_list)
        elif len(y_list) == 0:
            # horizontal case
            line_path = zip(x_list, [start[1]]*len(x_list))
        return line_path

    def solve_part_1(self):
        print("p1 ====================")
        hit_map = Day5.build_map(self.max_x, self.max_y, self.input, True)
        count = 0
        for y in hit_map:
            for x_val in y:
                if x_val > 1:
                    count += 1
        print(f'count: {count}')

    def solve_part_2(self):
        print("p2 ====================")
        hit_map = Day5.build_map(self.max_x, self.max_y, self.input, False)
        count = 0
        for y in hit_map:
            for x_val in y:
                if x_val > 1:
                    count += 1
        print(f'count: {count}')

Day5()
