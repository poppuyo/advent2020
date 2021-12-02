import math
import copy


class Day14:
    def __init__(self):
        self.input = []
        self.memory = {}
        self.load_input()
        self.memory2 = copy.deepcopy(self.memory)
        # print(self.inputs)
        print(f'pt1: {self.solve_part_1()}')
        # print(self.memory)
        print(f'pt2: {self.solve_part_2()}')


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

    def solve_part_2(self):
        active_mask = ''
        for cmd, val in self.input:
            if cmd == 'm':
                active_mask = val
            else:
                if active_mask == '':
                    raise RuntimeError('tried to change memory without an active mask!')
                addresses_to_write = Day14.get_values_from_wildcard_mask(active_mask, format(cmd, '036b'))
                #print(f'cmd:{cmd},val:{val}')
                for address in addresses_to_write:
                    #print(f'ret:{int(address,2)}:{address}')
                    self.memory2[int(address, 2)] = format(int(val,2), '036b')
        running_total = 0
        for key, vals in self.memory2.items():
            running_total += int(vals,2)
        #print(self.memory2)
        return running_total

    @staticmethod
    def apply_mask(mask, value):
        result = ''
        for m_value, v_value in zip(mask, value):
            if m_value == 'X':
                result += v_value
            else:
                result += m_value
        return result

    @staticmethod
    def get_values_from_wildcard_mask(mask, value):
        mid_result = ''
        for m_value, v_value in zip(mask, value):
            if m_value == 'X':
                mid_result += 'X'
            elif m_value == '1':
                mid_result += '1'
            elif m_value == '0':
                mid_result += v_value
            else:
                raise RuntimeError(f'unknown m_value: {m_value} from mask {mask}')

        results = [list(mid_result)]

        for i in range(0, 36):
            if mid_result[i] == 'X':
                to_append = []
                for result in results:
                    dupe = copy.deepcopy(result)
                    result[i] = '0'
                    dupe[i] = '1'
                    to_append.append(dupe)
                results += to_append

        ret_list = []
        for list_strings in results:
            ret_list.append(''.join(list_strings))
        return ret_list

Day14()
