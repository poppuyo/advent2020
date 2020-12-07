class Day6:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day6.txt", "r")
        txt = f.read()
        self.input = txt.splitlines()

    def group_responses(self, include_responder_count):
        responses = []
        current = {}
        for i in range(0, len(self.input)):
            if self.input[i] == '':
                responses.append(current)
                current = {}
            else:
                if include_responder_count:
                    current['people'] = current.get('people', 0) + 1
                for letter in self.input[i]:
                    current[letter] = current.get(letter, 0) + 1
        responses.append(current)
        return responses

    def solve_part_1(self):
        responses = self.group_responses(False)
        total_count = 0
        for response in responses:
            total_count += len(response.keys())
        print(total_count)

    def solve_part_2(self):
        responses = self.group_responses(True)
        total_count = 0
        for response in responses:
            for letter, count in response.items():
                if letter == 'people':
                    continue
                else:
                    if response['people'] == count:
                        total_count += 1
        print(total_count)


Day6()
