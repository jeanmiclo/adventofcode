from utils.solution_base import SolutionBase

class Solution(SolutionBase):

    DIR = [(-1,0),(0,1),(1,0),(0,-1)]

    def get_grid(self,data):

        grid = []

        for line in data:
            grid.append(line.rstrip('\n'))

        m,n = len(grid),len(grid[0])
        
        x,y= 0,0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '^':
                    x,y = i,j

        return grid,x,y

    def simulate_guard(self,grid,x,y):

        m,n = len(grid),len(grid[0])

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n 

        direction = 0
        visited = set([(x,y)])
        visited_direction = set([(x,y,direction)])

        while is_valid(x,y):
            while grid[x][y] != '#':
                dx,dy = self.DIR[direction]
                nx,ny = x+dx,y+dy

                if is_valid(nx,ny) and grid[nx][ny] == "#":
                    break
                else:
                    x,y = nx,ny
                    if not is_valid(x,y): 
                        return len(visited),visited,False
                    if (x,y,direction) in visited_direction: 
                        return None,None,True
                    visited.add((x,y))
                    visited_direction.add((x,y,direction))
            direction = (direction+1)%4
        return len(visited),visited,False

    def part1(self, data):
        return self.simulate_guard(*self.get_grid(data))[0]


    def part2(self, data):
        grid,x,y = self.get_grid(data)
        m,n = len(grid),len(grid[0])

        _,visited,_ = self.simulate_guard(grid,x,y)
        loop_positions = set()

        for i in range(m):
            for j in range(n):
                if (i,j) in visited and (i,j) != (x,y):
                    grid[i] = grid[i][:j] + '#' + grid[i][j+1:]
                    if self.simulate_guard(grid, x, y)[2]:
                        loop_positions.add((i, j))
                    grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
        
        return len(loop_positions)