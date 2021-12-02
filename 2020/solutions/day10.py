import copy


class Day10:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        # self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day10.txt", "r")
        txt = f.read()
        self.input = list(map(int, txt.splitlines()))

    def count_joltage_buckets(self, buckets_to_count):
        buckets = {}
        sorted_input = copy.deepcopy(self.input)
        list.sort(sorted_input)
        for bucket_val in buckets_to_count:
            buckets[bucket_val] = 0
        sorted_input.insert(0, 0)  # initial joltage hop
        for i in range(0, len(sorted_input) - 1):
            spread = sorted_input[i + 1] - sorted_input[i]
            if spread in buckets.keys():
                buckets[spread] += 1
        buckets[max(buckets.keys())] += 1  # last joltage hop is max size
        return buckets

    def count_possibilities(self, max_spread=3):
        sorted_input = copy.deepcopy(self.input)
        list.sort(sorted_input)
        sorted_input.insert(0, 0)
        sorted_input.append(sorted_input[-1] + 3)
        ways = 1
        while len(sorted_input) > 0:
            start = sorted_input[0]

    def solve_part_1(self):
        buckets = self.count_joltage_buckets([1, 3])
        print(f'buckets:{buckets}, mult:{buckets[1] * buckets[3]}')

    def solve_part_2(self, min_search_width, offending_value):
        result_list = self.find_contiguous_summing_to_value(self.input, min_search_width, offending_value)
        print(result_list)
        print(min(result_list) + max(result_list))


Day10()
