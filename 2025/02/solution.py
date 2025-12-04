from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):
        res = 0
        for intervals in str(data[0]).split(','):
            l,r = map(int,intervals.split('-'))
            for _id in range(l,r+1):
                s = str(_id)
                n = len(s)
                if s[:n//2] == s[n//2:]:
                    res += _id
        return res

    def part2(self, data):
        res = 0
        for intervals in str(data[0]).split(','):
            l,r = map(int,intervals.split('-'))
            for _id in range(l,r+1):
                s = str(_id)
                n = len(s)
                for i in range(2,n+1):
                    if s[:n//i] * i == s:
                        res += _id
                        break
        return res