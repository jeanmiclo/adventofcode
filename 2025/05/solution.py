from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):
        
        ranges = []
        n = len(data)
        i = 0
        while data[i].rstrip() != '':
            l,r = map(int,data[i].rstrip().split('-'))
            ranges.append((l,r))
            i += 1
        
        ranges.sort()

        i += 1
        res = 0

        while i < n:
            _id = int(data[i].rstrip())
            for l,r in ranges:
                if _id <= r and _id >= l:
                    res += 1
                    break
            i += 1

        return res

    def part2(self, data):
        
        ranges = []
        i = 0
        while data[i].rstrip() != '':
            l,r = map(int,data[i].rstrip().split('-'))
            ranges.append((l,r))
            i += 1
        
        ranges.sort()
        res = 0

        start,end = ranges[0]

        n = len(ranges)
        for i in range(1,n):
            if ranges[i][0] > end:
                res += end-start+1
                start,end = ranges[i]
            else:
                end = max(end,ranges[i][1])
        
        res += end-start+1

        return res