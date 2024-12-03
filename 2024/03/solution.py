from utils.solution_base import SolutionBase

import re

class Solution(SolutionBase):

    def part1(self, data):

        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

        res = 0

        for line in data:
            for x,y in re.findall(pattern,line):
                res += int(x)*int(y)

        return res

    def part2(self, data):

        pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
        pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

        res = 0
        enabled = True

        for line in data:
            for match in re.findall(pattern,line):
                if match == "do()":
                    enabled = True
                elif match == "don't()":
                    enabled = False
                elif enabled:
                    x,y = map(int,re.search(pattern_mul,match).groups())
                    res += x*y

        return res