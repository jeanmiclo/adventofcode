from functools import cache
from utils.solution_base import SolutionBase

from collections import defaultdict
from bisect import bisect_left,bisect_right

class Solution(SolutionBase):

    def part1(self, data):
        groups = []
        group = []
        for line in data:
            line = line.rstrip()
            if line == '':
                groups.append(group)
                group = []
            else:
                group.append(line)
        groups.append(group)

        res = 0
        for regions in groups[-1]:
            line = regions.split(' ')
            x = int(line[0][:2])
            y = int(line[0][-3:-1])
            sm = sum(map(int,line[1:]))
            if x*y - (sm*9) >= 0:
                res += 1
            
        return res

    def part2(self, data):

        return None