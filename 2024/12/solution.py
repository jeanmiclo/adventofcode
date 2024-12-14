from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    DIR = [(0,1),(1,0),(0,-1),(-1,0)]
    
    def get_grid(self,data):

        grid = []

        for line in data:
            row = []
            for c in line.rstrip("\n"):
                row.append(c)
            grid.append(row)
        
        return grid,len(grid),len(grid[0])

    def part1(self, data):

        grid,m,n = self.get_grid(data)
        visited = set()

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        def dfs(x,y,current_value):
            
            region = 1
            sides = 0
            for dx,dy in self.DIR:
                nx,ny = x+dx,y+dy
                if not is_valid(nx,ny) or grid[nx][ny] != current_value:
                    sides += 1
                elif (nx,ny) not in visited:
                    visited.add((nx,ny))
                    _region,_sides = dfs(nx,ny,current_value)
                    region += _region
                    sides += _sides
                    
            return region,sides

        res = 0

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    visited.add((i,j))
                    fence,region = dfs(i,j,grid[i][j])
                    res += fence*region


        return res

    def part2(self, data):

        grid,m,n = self.get_grid(data)
        visited = set()
    
        def is_same(i, j, plant):
            return (
                i in range(m) and 
                j in range(n) and 
                grid[i][j] == plant
            )
        
        def find_region(i, j):
            plant = grid[i][j]
            region = set()
            queue = set([(i, j)])
            while queue:
                i, j = queue.pop()
                region.add((i, j))
                for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                    if (x in range(m) and 
                        y in range(n) and 
                        grid[x][y] == plant and
                        (x, y) not in region and
                        (x, y) not in queue
                    ):
                        queue.add((x, y))
                        
            corners = sum(get_corners(x, y) for x, y in region)
            return region, corners * len(region)
        
        def get_corners(i, j):
            NW, W, SW, N, S, NE, E, SE = [
                is_same(i+x, j+y, grid[i][j])
                for x in range(-1, 2) 
                for y in range(-1, 2) 
                if x or y
            ]
            return sum([
                N and W and not NW, 
                N and E and not NE, 
                S and W and not SW, 
                S and E and not SE, 
                not (N or W),
                not (N or E),
                not (S or W),
                not (S or E)
            ])

        res = 0

        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    region, cost = find_region(i, j)
                    res += cost
                    visited |= region


        return res