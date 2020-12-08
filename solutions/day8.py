import copy


class Day8:
    def __init__(self):
        self.input = {}
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day8.txt", "r")
        txt = f.read()
        raw_input = txt.splitlines()

        instructions = []
        for line in raw_input:
            parsed = line.split(" ")
            instruction = {}
            instruction['cmd'] = parsed[0]
            instruction['val'] = int(parsed[1].replace("+", ""))
            instruction['run'] = False
            instructions.append(instruction)
        self.input = instructions

    @staticmethod
    def run_program(instructions):
        cur = 0
        acc = 0
        try:
            while True:
                if cur == len(instructions):
                    return cur, acc, ''
                if instructions[cur]['run']:
                    return cur, acc, 'inf_loop'
                instructions[cur]['run'] = True
                cmd = instructions[cur]['cmd']
                if cmd == 'nop':
                    cur += 1
                    pass
                elif cmd == 'acc':
                    acc += instructions[cur]['val']
                    cur += 1
                    pass
                elif cmd == 'jmp':
                    cur += instructions[cur]['val']
                    pass
        except IndexError:
            return cur, acc, 'list_oob'

    def solve_part_1(self):
        instructions = copy.deepcopy(self.input)
        cur, acc, inf_loop = self.run_program(instructions)
        print(acc)

    def solve_part_2(self):
        for i in range(0, len(self.input)):
            instructions = copy.deepcopy(self.input)
            if self.input[i]['cmd'] == "nop":
                instructions[i]['cmd'] = "jmp"
            elif self.input[i]['cmd'] == "jmp":
                instructions[i]['cmd'] = "nop"
            cur, acc, err = self.run_program(instructions)
            if err == '':
                print(acc)
                return


Day8()
