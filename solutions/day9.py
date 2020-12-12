class Day9:
    def __init__(self):
        self.input = {}
        self.load_input()
        offending_value = self.solve_part_1()
        self.solve_part_2(2, offending_value)

    def load_input(self):
        f = open("../inputs/day9.txt", "r")
        txt = f.read()
        self.input = list(map(int, txt.splitlines()))

    @staticmethod
    def run_program(input_list, preamble_length):
        search_space = input_list[:preamble_length]
        for i in range(preamble_length, len(input_list[preamble_length:])):
            found, values = Day9.find_summing_values(search_space, input_list[i])
            if not found:
                return False, input_list[i]
            search_space[i % preamble_length] = input_list[i]
        return True, None

    @staticmethod
    def find_summing_values(search_space, value):
        for i in range(0, len(search_space)):
            for j in range(i, len(search_space)):
                if search_space[i] + search_space[j] == value:
                    return True, (search_space[i], search_space[j])
        return False, (None, None)

    @staticmethod
    def find_contiguous_summing_to_value(search_space, min_search_width, value):
        for i in range(0, len(search_space)):
            search_relative_cursor = 0
            decrementor = value
            while decrementor > 0:
                decrementor -= search_space[i + search_relative_cursor]
                search_relative_cursor += 1
                if decrementor == 0 and search_relative_cursor >= min_search_width:
                    return search_space[i:i + search_relative_cursor]
        return None

    def solve_part_1(self):
        succeeded, offending_value = self.run_program(self.input, 25)
        print(f'success:{succeeded}, offending:{offending_value}')
        return offending_value

    def solve_part_2(self, min_search_width, offending_value):
        result_list = self.find_contiguous_summing_to_value(self.input, min_search_width, offending_value)
        print(result_list)
        print(min(result_list) + max(result_list))


Day9()
