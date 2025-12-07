from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data: list[str]) -> int:
        grid = []
        for line in data:
            grid.append(line.rstrip())
        start = (0, grid[0].index("S"))
        n = len(grid)
        dp = defaultdict(int)
        dp[start] += 1
        res = 0
        for _ in range(n - 1):
            ndp = defaultdict(int)
            for (i, j), cur in dp.items():
                if i == n - 1:
                    continue
                inc = 1
                if grid[i + 1][j] == "^":
                    res += 1
                    ndp[(i + 1, j - 1)] += inc
                    ndp[(i + 1, j + 1)] += inc
                else:
                    ndp[(i + 1, j)] += inc
            dp = ndp
        return res

    def part2(self, data):
        grid = []
        for line in data:
            grid.append(line.rstrip())
        start = (0, grid[0].index("S"))
        n = len(grid)
        dp = defaultdict(int)
        dp[start] += 1
        res = 1
        for _ in range(n - 1):
            ndp = defaultdict(int)
            for (i, j), cur in dp.items():
                if i == n - 1:
                    continue
                inc = cur
                if grid[i + 1][j] == "^":
                    res += cur
                    ndp[(i + 1, j - 1)] += inc
                    ndp[(i + 1, j + 1)] += inc
                else:
                    ndp[(i + 1, j)] += inc
            dp = ndp
        return res