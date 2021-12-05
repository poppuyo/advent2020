import copy

class Day3:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day3.txt", "r")
        txt = f.read()
        self.input = txt.splitlines()

    def solve_part_1(self):
        print("p1 ====================")
        length = len(self.input[0])
        counts = [0]*length
        gamma = [""]*length

        for line in self.input:
            # print(line)
            for cur in range(length):
                if line[cur] == "1":
                    counts[cur] += 1
                else:
                    counts[cur] -= 1
        # print(counts)
        for i in range(length):
            if counts[i] > 0:
                gamma[i] = "1"
            else:
                gamma[i] = "0"
        gamma = int("".join(gamma), 2)
        epsilon = Day3.bit_not(gamma, length)
        print(f'{gamma}x{epsilon}={gamma*epsilon}')

    def solve_part_2(self):
        print("p2 ====================")
        length = len(self.input[0])
        oxygen_list = copy.deepcopy(self.input)
        co2_list = copy.deepcopy(self.input)

        oxygen_val = Day3.value_finder(oxygen_list, True, 1)
        co2_val = Day3.value_finder(co2_list, False, 0)
        print(f'oxygen_val {oxygen_val} ({int(oxygen_val, 2)})')
        print(f'co2_val    {co2_val} ({int(co2_val, 2)})')
        print(f'mult: {int(oxygen_val, 2) * int(co2_val, 2)}')
        return

    @staticmethod
    def value_finder(search_list: list, search_high, tiebreaker):
        length = len(search_list[0])

        for i in range(length):
            zeros, ones = Day3.list_pos_counter(search_list, i)
            # print(f'{i}: {zeros} vs {ones}')
            keep = tiebreaker
            if zeros > ones:
                keep = '0' if search_high else '1'
            else:
                keep = '1' if search_high else '0'

            keeplist = []
            # print(f'step: {i}: listlen: {len(search_list)}')
            for item in search_list:
                if item[i] == keep:
                    keeplist.append(item)

            search_list = keeplist
            # print(search_list)
            if len(search_list) == 1:
                return search_list[0]
        return

    @staticmethod
    def list_pos_counter(search_list, pos):
        counts = {'0': 0, '1': 0}

        for item in search_list:
            counts[item[pos]] += 1
        return counts['0'], counts['1']

    # https://stackoverflow.com/a/31151236
    @staticmethod
    def bit_not(n, bits=8):
        return (1 << bits) - 1 - n

Day3()
