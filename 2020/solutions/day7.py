import re


class Day7:
    def __init__(self):
        self.input = {}
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day7.txt", "r")
        txt = f.read()
        raw_input = txt.splitlines()
        left_regex = r'(\S+\s\S+)\sbags?'
        right_regex = r'(\d)\s(\S+\s\S+)\sbags?'
        bag_dict = {}
        for line in raw_input:
            left, right = line.split("contain")
            outer_bag = re.findall(left_regex, left)[0]
            if "no other bags" in right:
                bag_dict[outer_bag] = False
            else:
                inner_bags = re.findall(right_regex, right)
                bag_dict[outer_bag] = inner_bags
        self.input = bag_dict

    def bag_search(self, candidate_bag, wanted='shiny gold'):
        bag_list = [candidate_bag]
        while len(bag_list) > 0:
            if bag_list[0] == wanted:
                return True
            else:
                bag_to_open = bag_list.pop(0)
                # skip if False (end-bag)
                if self.input[bag_to_open]:
                    for bag in self.input[bag_to_open]:
                        # bag[0] = count
                        # bag[1] = condition+color
                        if bag[1] == wanted:
                            return True
                        bag_list.append(bag[1])
        return False

    def count_sub_bags(self, candidate_bag):
        bag_list = [(1, candidate_bag)]
        count = 0
        while len(bag_list) > 0:
            bag_tuple = bag_list.pop(0)
            print(bag_tuple)
            curr_bag_count = int(bag_tuple[0])
            count += curr_bag_count
            if self.input[bag_tuple[1]]:
                for inner_bag_count, inner_bag in self.input[bag_tuple[1]]:
                    bag_list.append((int(inner_bag_count) * curr_bag_count, inner_bag))
            else:
                continue
        return count

    def solve_part_1(self):
        bag_count = 0
        for outer_bag, inner_bags in self.input.items():
            if outer_bag == 'shiny gold':
                continue
            else:
                bag_count += 1 if self.bag_search(outer_bag, 'shiny gold') else 0
            print(f'{outer_bag}:{self.bag_search(outer_bag, "shiny gold")}')
        print(bag_count)

    def solve_part_2(self):
        # this is counting itself, so -1
        print(self.count_sub_bags('shiny gold') - 1)


Day7()
