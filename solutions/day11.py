import copy
from collections import Counter


class Day11:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day11.txt", "r")
        txt = f.read()
        to_process = txt.splitlines()
        for line in to_process:
            self.input.append(list(line))

    @staticmethod
    def run_generation(seat_map_state, adjacent_mode):
        next_state = copy.deepcopy(seat_map_state)
        for y in range(0, len(seat_map_state)):
            for x in range(0, len(seat_map_state[0])):
                if seat_map_state[y][x] == '.':
                    continue
                if adjacent_mode:
                    count = Day11.count_immediate_neighbors(seat_map_state, x, y)
                    if count >= 4 and seat_map_state[y][x] == '#':
                        next_state[y][x] = 'L'
                    elif count == 0 and seat_map_state[y][x] == 'L':
                        next_state[y][x] = '#'
                else:
                    count = Day11.count_visible_neighbors(seat_map_state, x, y)
                    if count >= 5 and seat_map_state[y][x] == '#':
                        next_state[y][x] = 'L'
                    elif count == 0 and seat_map_state[y][x] == 'L':
                        next_state[y][x] = '#'
        return next_state

    @staticmethod
    def count_immediate_neighbors(seat_map_state, x, y):
        x_limit = len(seat_map_state[0]) - 1
        y_limit = len(seat_map_state) - 1
        count = 0  # center seat is not counted
        if y - 1 >= 0:
            if x - 1 >= 0:
                count += 1 if seat_map_state[y - 1][x - 1] == '#' else 0  # NW
            count += 1 if seat_map_state[y - 1][x] == '#' else 0  # N
            if x + 1 <= x_limit:
                count += 1 if seat_map_state[y - 1][x + 1] == '#' else 0  # NE
        if y + 1 <= y_limit:
            if x - 1 >= 0:
                count += 1 if seat_map_state[y + 1][x - 1] == '#' else 0  # SW
            count += 1 if seat_map_state[y + 1][x] == '#' else 0  # S
            if x + 1 <= x_limit:
                count += 1 if seat_map_state[y + 1][x + 1] == '#' else 0  # SE
        if x - 1 >= 0:
            count += 1 if seat_map_state[y][x - 1] == '#' else 0  # W
        if x + 1 <= x_limit:
            count += 1 if seat_map_state[y][x + 1] == '#' else 0  # E
        return count

    @staticmethod
    def count_visible_neighbors(seat_map_state, x, y):
        count = 0
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (-1, -1)) else 0  # NW
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (+0, -1)) else 0  # N
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (+1, -1)) else 0  # NE
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (-1, +0)) else 0  # W
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (+1, +0)) else 0  # E
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (-1, +1)) else 0  # SW
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (+0, +1)) else 0  # S
        count += 1 if Day11.scan_direction(seat_map_state, x, y, (+1, +1)) else 0  # SE
        return count

    @staticmethod
    def scan_direction(seat_map_state, x, y, direction_tuple):
        x_lim = len(seat_map_state[0]) - 1
        y_lim = len(seat_map_state) - 1
        cx = x + direction_tuple[0]
        cy = y + direction_tuple[1]
        while 0 <= cx <= x_lim and 0 <= cy <= y_lim:
            if seat_map_state[cy][cx] == '#':
                return True
            elif seat_map_state[cy][cx] == 'L':
                return False
            cx = cx + direction_tuple[0]
            cy = cy + direction_tuple[1]
        return False

    def solve_part_1(self):
        current_state = self.input
        gen_count = 0
        while True:
            prev_state = current_state
            current_state = self.run_generation(current_state, True)
            if current_state == prev_state:
                break
            gen_count += 1
        counts = Counter(i for sublist in current_state for i in sublist)
        print(f'{gen_count} generations: {counts["."]} floor, {counts["L"]} empty, {counts["#"]} filled')

    def solve_part_2(self):
        current_state = self.input
        gen_count = 0
        while True:
            prev_state = current_state
            current_state = self.run_generation(current_state, False)
            if current_state == prev_state:
                break
            gen_count += 1
        counts = Counter(i for sublist in current_state for i in sublist)
        print(f'{gen_count} generations: {counts["."]} floor, {counts["L"]} empty, {counts["#"]} filled')


Day11()
