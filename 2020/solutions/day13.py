import math


class Day13:
    def __init__(self):
        self.input = []
        self.simplified_input = []
        self.load_input()
        print(self.solve_part_1())
        print(self.solve_part_2())

    def load_input(self):
        f = open("../inputs/day13.txt", "r")
        txt = f.read()
        to_process = txt.splitlines()
        self.input.append(int(to_process[0]))
        self.input.append([])
        for bus in to_process[1].split(','):
            if bus is not 'x':
                self.input[1].append(int(bus))
            else:
                self.input[1].append(-1)

        for i, bus_id in zip(range(len(self.input[1])), self.input[1]):
            if bus_id > 0:
                self.simplified_input.append((i, bus_id))

    def solve_part_1(self):
        start_time = self.input[0]
        shortest_wait = 999999
        best_bus_id = -1

        for bus_id in self.input[1]:
            if bus_id > 0:
                first_time = math.floor(start_time/bus_id)
                # perfect bus, btw
                if start_time - (first_time * bus_id) == 0:
                    shortest_wait = 0
                    best_bus_id = bus_id
                else:
                    next_time = (first_time + 1)*bus_id
                    if next_time - start_time < shortest_wait:
                        shortest_wait = next_time - start_time
                        best_bus_id = bus_id

        return best_bus_id, shortest_wait

    def solve_part_2(self):
        found_seq = False
        largest_bus = -1
        largest_bus_offset = -1

        for i, bus_id in self.simplified_input:
            if bus_id > largest_bus:
                largest_bus = bus_id
                largest_bus_offset = i
        val = largest_bus - largest_bus_offset

        while not found_seq:
            for i, bus_id in self.simplified_input:
                if bus_id > 0:
                    if not Day13.check_offset(val, i, bus_id):
                        break
                if i + 1 == len(self.input[1]):
                    return val
            val += largest_bus

    @staticmethod
    def check_offset(candidate_time, minute_offset, bus_id):
        return (candidate_time + minute_offset) % bus_id == 0


Day13()
