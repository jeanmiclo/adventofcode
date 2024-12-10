from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    DIR = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def get_grid(self,data):

        grid = []

        for line in data:
            row = []
            for c in line.rstrip("\n"):
                row.append(int(c))
            grid.append(row)
        
        return grid,len(grid),len(grid[0])

    def part1(self, data):

        grid,m,n = self.get_grid(data)
        visited = set()

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x,y,val):
            if val == 9: return 1
            res = 0
            for dx,dy in self.DIR:
                nx,ny = x+dx,y+dy
                if is_valid(nx,ny) and (nx,ny) not in visited and grid[nx][ny] == val+1:
                    visited.add((nx,ny))
                    res += dfs(nx,ny,val+1)
                    
            return res

        res = 0

        for i in range(m):
            for j in range(n):
                 if grid[i][j] == 0:
                     visited = set()
                     res += dfs(i,j,0)


        return res

    def part2(self, data):

        grid,m,n = self.get_grid(data)

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x,y,val):
            if val == 9: return 1
            res = 0
            for dx,dy in self.DIR:
                nx,ny = x+dx,y+dy
                if is_valid(nx,ny) and (nx,ny) and grid[nx][ny] == val+1:
                    res += dfs(nx,ny,val+1)
                    
            return res

        res = 0

        for i in range(m):
            for j in range(n):
                 if grid[i][j] == 0:
                     res += dfs(i,j,0)


        return res