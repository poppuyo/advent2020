import re


class Day4:
    def __init__(self):
        self.input = []
        self.load_input()
        self.solve_part_1()
        self.solve_part_2()

    def load_input(self):
        f = open("../inputs/day4.txt", "r")
        txt = f.read()
        self.input = txt.splitlines()

    def group_passports(self):
        regex = r'(\S+:\S+)'
        passports = []
        current = {}
        for i in range(0, len(self.input)):
            if self.input[i] == '':
                passports.append(current)
                current = {}
            else:
                results = re.findall(regex, self.input[i])
                for item in results:
                    key, val = str.split(item, ":")
                    current[key] = val
        passports.append(current)
        return passports

    def passport_has_fields(self, passport, fields, optional_fields):
        for field in fields:
            if field not in passport.keys():
                return False
        return True

    def passport_has_valid_fields(self, passport, fields, optional_fields):
        re_hcl = r'^#[0-9a-f]{6}$'
        re_ecl = r'^(amb|blu|brn|gry|grn|hzl|oth)$'
        re_pid = r'^[0-9]{9}$'
        try:
            for field in fields:
                if field not in passport.keys():
                    return False
                if field == 'byr' and (int(passport['byr']) < 1920 or int(passport['byr']) > 2002):
                    return False
                if field == 'iyr' and (int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020):
                    return False
                if field == 'eyr' and (int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030):
                    return False
                if field == 'hgt':
                    res = False
                    if bool("in" in passport['hgt']) and bool("cm" in passport['hgt']):
                        return False
                    if "in" in passport['hgt']:
                        inches = int(passport['hgt'].replace("in", ""))
                        res = False if inches < 59 or inches > 76 else True
                    if "cm" in passport['hgt']:
                        centis = int(passport['hgt'].replace("cm", ""))
                        res = False if centis < 150 or centis > 193 else True
                    if not res:
                        return False
                if field == 'hcl' and re.search(re_hcl, passport['hcl']) is None:
                    return False
                if field == 'ecl' and re.search(re_ecl, passport['ecl']) is None:
                    return False
                if field == 'pid' and re.search(re_pid, passport['pid']) is None:
                    return False
            return True
        except ValueError:
            return False

    def solve_part_1(self):
        passports = self.group_passports()
        valid = 0
        for ps in passports:
            valid += 1 if self.passport_has_fields(ps, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], ["cid"]) else 0
        print(valid)

    def solve_part_2(self):
        passports = self.group_passports()
        valid = 0
        for ps in passports:
            valid += 1 if self.passport_has_valid_fields(ps, ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], ["cid"]) else 0
        print(valid)


Day4()
