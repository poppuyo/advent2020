import math


class Day14:
    def __init__(self):
        self.input = []
        self.memory = {}
        self.load_input()
        print(self.solve_part_1())
        print(self.memory)

    def load_input(self):
        f = open("../inputs/day14.txt", "r")
        txt = f.read()
        for line in txt.splitlines():
            to_process = list(map(str.strip, line.split('=')))
            if to_process[0] == 'mask':
                self.input.append(('m', to_process[1]))
            elif 'mem[' in to_process[0]:
                self.input.append((int(to_process[0].replace('mem[', '').replace(']', '')),
                                   format(int(to_process[1]), '036b')))

    def solve_part_1(self):
        active_mask = ''
        for cmd, val in self.input:
            if cmd == 'm':
                active_mask = val
            else:
                if cmd not in self.memory:
                    self.memory[cmd] = format(0, '036b')
                if active_mask == '':
                    raise RuntimeError('tried to change memory without an active mask!')
                if cmd >= 0:
                    self.memory[cmd] = Day14.apply_mask(active_mask, val)
        sum = 0
        for mem_loc, value in self.memory.items():
            sum += int(value, 2)
        return sum

    @staticmethod
    def apply_mask(mask, value):
        result = ''
        for m_value, v_value in zip(mask, value):
            if m_value == 'X':
                result += v_value
            else:
                result += m_value
        return result


Day14()
