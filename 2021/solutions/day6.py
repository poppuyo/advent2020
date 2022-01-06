class Day6:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day6.txt", "r")
        txt = f.read()
        self.input = txt.split(',')
        print(self.input)

    def solve_part_1(self):
        print("p1 ====================")
        population = [0]*9  # init
        for i in self.input:
            population[int(i)] += 1
        grown_population = Day6.grow_population(population, 80)
        print(sum(grown_population))

    def solve_part_2(self):
        print("p2 ====================")
        population = [0]*9  # init
        for i in self.input:
            population[int(i)] += 1
        grown_population = Day6.grow_population(population, 256)
        print(sum(grown_population))

    @staticmethod
    def grow_population(population, days):
        for d in range(days ):
            # print(population)
            new_fish = population[0]
            population = population[1:]
            population[6] += new_fish
            population.append(new_fish)
        return population


Day6()
