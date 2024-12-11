from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def stones_number(self,data,limit):
        
        memo = {}

        def dfs(i,stone):
            if i == limit: return 1
            if (i,stone) not in memo:
                if stone == '0':
                    memo[(i,stone)] = dfs(i+1,'1')
                elif len(stone) % 2 == 0:
                    middle = len(stone)//2
                    memo[(i,stone)] = dfs(i+1,stone[:middle]) + dfs(i+1,str(int(stone[middle:])))
                else:
                    memo[(i,stone)] = dfs(i+1,str(int(stone)*2024))
            
            return memo[(i,stone)]
        
        res = 0
        for elt in data:
            res += dfs(0,elt)

        return res
    

    def part1(self, data):

        return self.stones_number(data[0].rstrip("\n").split(' '),25)

    def part2(self, data):

        return self.stones_number(data[0].rstrip("\n").split(' '),75)