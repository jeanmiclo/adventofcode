from utils.solution_base import SolutionBase

from collections import deque

class Solution(SolutionBase):

    DIR = [(0,1),(1,0),(0,-1),(-1,0)]

    def print_grid(self,grid):
        m,n = len(grid),len(grid[0])

        for x in range(m):
            for y in range(n):
                print(f"{grid[x][y]:<5}", end='')
            print('')
        print('')
    
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
        sx = sy = ex = ey = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S': 
                    sx,sy = i,j
                    grid[i][j] = 0
                elif grid[i][j] == 'E': 
                    ex,ey = i,j
                    grid[i][j] = float('inf')
                elif grid[i][j] == '.':
                    grid[i][j] = float('inf')
                else:
                    grid[i][j] = float('-inf')
                

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        visited = set()
        visited.add((sx,sy,0))

        queue = deque()
        queue.append((sx,sy,0))

        while queue:
            x,y,score = queue.popleft()
            grid[x][y] = min(score,grid[x][y])
            if (x,y) == (ex,ey): break

            for dx,dy in self.DIR:
                nx,ny = x+dx,y+dy
                if is_valid(nx,ny) and (nx,ny,score) not in visited:
                    if grid[nx][ny] >= 0 and grid[nx][ny] >= score:
                        queue.append((nx,ny,score+1))
                        visited.add((nx,ny,score+1))

        res = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] >= 0:
                    for dx,dy in [(2,0),(0,2),(-2,0),(0,-2),(1,-1),(-1,1),(1,1),(-1,-1)]:
                        nx,ny = x+dx,y+dy
                        if is_valid(nx,ny) and grid[nx][ny]-grid[x][y]-2 >= 100 :
                            res += 1

        return res

    def part2(self, data):

        grid,m,n = self.get_grid(data)
        sx = sy = ex = ey = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S': 
                    sx,sy = i,j
                    grid[i][j] = 0
                elif grid[i][j] == 'E': 
                    ex,ey = i,j
                    grid[i][j] = float('inf')
                elif grid[i][j] == '.':
                    grid[i][j] = float('inf')
                else:
                    grid[i][j] = float('-inf')
                

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        visited = set()
        visited.add((sx,sy,0))

        queue = deque()
        queue.append((sx,sy,0))

        while queue:
            x,y,score = queue.popleft()
            grid[x][y] = min(score,grid[x][y])
            if (x,y) == (ex,ey): break

            for dx,dy in self.DIR:
                nx,ny = x+dx,y+dy
                if is_valid(nx,ny) and (nx,ny,score) not in visited:
                    if grid[nx][ny] >= 0 and grid[nx][ny] >= score:
                        queue.append((nx,ny,score+1))
                        visited.add((nx,ny,score+1))

        res = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] >= 0:
                    for r in range(2,21):
                        for dx in range(r+1):
                            dy = r - dx
                            for nx, ny in {(x + dx, y + dy), (x + dx, y - dy), (x - dx, y + dy), (x - dx, y - dy)}:
                                if is_valid(nx, ny) and grid[nx][ny] - grid[x][y] - r >= 100:
                                    res += 1

        return res