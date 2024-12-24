from utils.solution_base import SolutionBase

class Solution(SolutionBase):

    def part1(self, data): 

        towels = data[0].rstrip('\n').replace(' ','').split(',')
        res = 0

        cache = {}

        def dfs(i,word):
            if i == len(word): return True

            if (i,word) not in cache:
                ans = False
                for towel in towels:
                    if towel == word[i:i+len(towel)]:
                        ans = ans or dfs(i+len(towel),word)
                cache[(i,word)] = ans

            return cache[(i,word)]

        for i,line in enumerate(data[2:]):
            if dfs(0,line.rstrip('\n')):
                res += 1

        return res

    def part2(self, data):

        towels = data[0].rstrip('\n').replace(' ','').split(',')
        res = 0

        cache = {}

        def dfs(i,word):
            if i == len(word): return 1
            if (i,word) not in cache:
                ans = 0
                for towel in towels:
                    if towel == word[i:i+len(towel)]:
                        ans += dfs(i+len(towel),word)
                cache[(i,word)] = ans

            return cache[(i,word)]

        for line in data[2:]:
            res += dfs(0,line.rstrip('\n'))
                
        return res