from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def adjacentCount(self,x,y,m,n):
        ans = 0
        for dx in range(-1,2):
            for dy in range(-1,2):
                if dx == dy == 0: continue
                nx,ny = x+dx,y+dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n: continue
                if self.grid[nx][ny] == '@':
                    ans += 1
        return ans

    def part1(self, data):
        m,n = len(data),len(data[0])-1
        self.grid = []
        for line in data:
            line = line.rstrip('\n')
            self.grid.append(line)

        res = 0
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == '@' and self.adjacentCount(i,j,m,n) < 4:
                    res += 1

        return res

    def part2(self, data):
        m,n = len(data),len(data[0])-1
        self.grid = []
        for line in data:
            line = line.rstrip('\n')
            self.grid.append(line)

        res = 0

        while True:
            cnt = 0
            new_grid = [['.' for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if self.grid[i][j] == '@' and self.adjacentCount(i,j,m,n) < 4:
                        new_grid[i][j] = '.'
                        cnt += 1
                    else:
                        new_grid[i][j] = self.grid[i][j]
            if cnt == 0: break
            self.grid = new_grid
            res += cnt

        return res