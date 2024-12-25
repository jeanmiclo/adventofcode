from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):

    def grid_converter(self,grid):
        m,n = 7,5
        heights = []
        for i in range(n):
            cnt = 0
            for j in range(1,m-1):
                if grid[j][i] == '#':
                    cnt += 1
            heights.append(cnt)

        if '#' in grid[m-1]: return (False,heights)
        else: return (True,heights)

    def part1(self, data): 
        keys = []
        locks = []

        i = 0
        while i < len(data):
            lock,heights = self.grid_converter([line.rstrip('\n') for line in data[i:i+7]])
            if lock: locks.append(heights)
            else: keys.append(heights)
            i += 8

        res = 0

        for key in keys:
            for lock in locks:
                fit = True
                for i in range(5):
                    if key[i] + lock[i] > 5:
                        fit = False
                        break
                if fit: res += 1

        return res

    def part2(self, data):
        return None