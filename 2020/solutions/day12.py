import re


class Day12:
    def __init__(self):
        self.input = []
        self.load_input()

        self.rot_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.transpose_lookup = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        self.facing = (1, 0)
        self.pos = (0, 0)
        self.waypoint_pos = (10, 1)

        self.solve_part_1()
        self.solve_part_2()

    def reset(self):
        self.facing = (1, 0)
        self.pos = (0, 0)
        self.waypoint_pos = (10, 1)

    def load_input(self):
        f = open("../inputs/day12.txt", "r")
        txt = f.read()
        raw_input = txt.splitlines()
        regex = r'(\w)(\d+)'
        for line in raw_input:
            instructions = re.findall(regex, line)[0]
            self.input.append((instructions[0], int(instructions[1])))

    def rotate(self, direction, angle):
        cur_index = self.rot_list.index(self.facing)
        rot_amount = int(angle / 90)
        if direction == "L":
            self.facing = self.rot_list[(cur_index - rot_amount) % 4]
        elif direction == "R":
            self.facing = self.rot_list[(cur_index + rot_amount) % 4]
        else:
            raise ValueError

    def get_xy_dist_of_waypoint_from_ship(self):
        return (self.waypoint_pos[0] - self.pos[0],
                self.waypoint_pos[1] - self.pos[1])

    def rotate_waypoint(self, direction, angle):
        # rot L/R180 = sign flip
        # rot L90/R270 = (x,y) --> (-y,x)
        # rot R90/L270 = (x,y) --> (y,-x)?
        rel_pos = self.get_xy_dist_of_waypoint_from_ship()
        if angle == 180:
            rel_pos = (-rel_pos[0], -rel_pos[1])
        elif f'{direction}{angle}' in ["L90", "R270"]:
            rel_pos = (-rel_pos[1], rel_pos[0])
        elif f'{direction}{angle}' in ["R90", "L270"]:
            rel_pos = (rel_pos[1], -rel_pos[0])
        else:
            raise ValueError
        self.waypoint_pos = (self.pos[0] + rel_pos[0],
                             self.pos[1] + rel_pos[1])

    def transpose(self, direction, value, is_waypoint_mode=False):
        if is_waypoint_mode:
            current = self.waypoint_pos
            self.waypoint_pos = (current[0] + value * self.transpose_lookup[direction][0],
                                 current[1] + value * self.transpose_lookup[direction][1])
        current = self.pos
        self.pos = (current[0] + value * self.transpose_lookup[direction][0],
                    current[1] + value * self.transpose_lookup[direction][1])

    def forward(self, value):
        for cardinal, vector in self.transpose_lookup.items():
            if self.facing == vector:
                self.transpose(cardinal, value)

    def forward_to_waypoint(self, value):
        self.waypoint_pos = (self.pos[0] + self.waypoint_pos[0]*value,
                             self.pos[1] + self.waypoint_pos[1]*value)

    def process_step(self, action, value, is_waypoint_mode=False):
        if action in "LR":
            self.rotate_waypoint(action, value) if is_waypoint_mode else self.rotate(action, value)
        elif action in "NSEW":
            self.transpose(action, value, is_waypoint_mode)
        elif action in "F":
            self.forward_to_waypoint(value) if is_waypoint_mode else self.forward(value)

    def solve_part_1(self):
        for action, value in self.input:
            self.process_step(action, value)
            # print(f'{self.facing}: {self.pos}')
        print(f'{abs(self.pos[0]) + abs(self.pos[1])}')

    def solve_part_2(self):
        self.reset()
        for action, value in self.input:
            self.process_step(action, value, True)
            print(f'{self.waypoint_pos}, {self.pos}')
        print(f'{abs(self.pos[0]) + abs(self.pos[1])}')
        return True


Day12()
