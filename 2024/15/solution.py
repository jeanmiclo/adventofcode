from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):

    def print_grid(self,grid):
        m,n = len(grid),len(grid[0])

        for x in range(m):
            for y in range(n):
                print(grid[x][y],end='')
            print('')
        print('')

    def is_valid(self,x,y,m,n):
        return 0 <= x < m and 0 <= y < n
    
    def get_movements(self,data):
        res = []

        for line in data:
            for c in line.rstrip('\n'):
                if c == '^':
                    res.append((-1,0))
                elif c == '<':
                    res.append((0,-1))
                elif c == '>':
                    res.append((0,1))
                elif c == 'v':
                    res.append((1,0))

        return res
    
    def find_space_part1(self,x,y,dx,dy,grid):
        m,n = len(grid),len(grid[0])

        while self.is_valid(x,y,m,n) and grid[x][y] == 'O':
            x,y = x+dx,y+dy

            if self.is_valid(x,y,m,n) and grid[x][y] == '.':
                return x,y

        return None,None
    
    def get_data_part1(self,data):

        initial_x,initial_y = None,None
        n = data[0].count('#')-2
        grid = [[] for _ in range(n)]
        i = 1

        while data[i].count('#') < n+2:
            for j,c in enumerate(data[i].rstrip('\n')[1:-1]):
                if c == '@': initial_x,initial_y = i-1,j
                grid[i-1].append(c)
            i += 1

        movements = self.get_movements(data[i+1:])

        return initial_x,initial_y,grid,movements

    def part1(self, data):
        x,y,grid,movements = self.get_data_part1(data)
        m,n = len(grid),len(grid[0])

        for dx,dy in movements:
            nx,ny = x+dx,y+dy
            if self.is_valid(nx,ny,m,n):
                if grid[nx][ny] == '.':
                    grid[nx][ny],grid[x][y] = grid[x][y],grid[nx][ny]
                    x,y = nx,ny
                elif grid[nx][ny] == '#':
                    pass
                else:
                    xs,ys = self.find_space_part1(nx,ny,dx,dy,grid)
                    if xs is not None and ys is not None:
                        grid[x][y] = '.'
                        grid[nx][ny] = '@'
                        grid[xs][ys] = 'O'
                        x,y = nx,ny
                    else:
                        pass
        res = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 'O':
                    res += (x+1)*100+y+1

        return res
    
    def find_space_part2(self,x,y,dx,dy,grid):
        m,n = len(grid),len(grid[0])

        while self.is_valid(x,y,m,n) and grid[x][y] in '[]':
            x,y = x+dx,y+dy

            if self.is_valid(x,y,m,n) and grid[x][y] == '.':
                return x,y

        return None,None
    
    def get_data_part2(self,data):

        initial_x,initial_y = None,None
        n = data[0].count('#')-2
        grid = [[] for _ in range(n)]
        i = 1

        while data[i].count('#') < n+2:
            j = 0
            for c in data[i].rstrip('\n')[1:-1]:
                if c == '@': 
                    initial_x,initial_y = i-1,j
                    grid[i-1].append('@')
                    grid[i-1].append('.')
                elif c == 'O':
                    grid[i-1].append('[')
                    grid[i-1].append(']')
                elif c == '#':
                    grid[i-1].append('#')
                    grid[i-1].append('#')
                else: 
                    grid[i-1].append('.')
                    grid[i-1].append('.')
                j += 2
            i += 1

        movements = self.get_movements(data[i+1:])

        return initial_x,initial_y,grid,movements

    def part2(self, data):
        
        x,y,grid,movements = self.get_data_part2(data)
        m,n = len(grid),len(grid[0])

        for dx,dy in movements:

            nx,ny = x+dx,y+dy
            if self.is_valid(nx,ny,m,n):
                if grid[nx][ny] == '.':
                    grid[nx][ny],grid[x][y] = grid[x][y],grid[nx][ny]
                    x,y = nx,ny
                elif grid[nx][ny] == '#':
                    pass
                else:
                    # move on y axis is same as part 1
                    if dy != 0:
                        xs,ys = self.find_space_part2(nx,ny,dx,dy,grid)
                        if xs is not None and ys is not None:
                            if ys > y:
                                for i in range(ys-1,y-1,-1):
                                    grid[x][i+1] = grid[x][i]
                            else:
                                for i in range(ys+1,y+1):
                                    grid[x][i-1] = grid[x][i]

                            grid[x][y] = '.'    
                            x,y = nx,ny
                    else:
                        space_find = False
                        wall_find = False
                        level_hmap = defaultdict(set)
                        level = 0
                        level_hmap[0] = {y}

                        while not wall_find and not space_find:
                            space_count = 0
                            if dx == 1: x_value = x+level+1
                            else: x_value = x-level-1

                            for y_value in level_hmap[level]:

                                if not self.is_valid(x_value,y_value,m,n):
                                    wall_find = True
                                    break
                                if grid[x_value][y_value] == '[':
                                    level_hmap[level+1].add(y_value)
                                    level_hmap[level+1].add(y_value+1)
                                elif grid[x_value][y_value] == ']':
                                    level_hmap[level+1].add(y_value)
                                    level_hmap[level+1].add(y_value-1)
                                elif grid[x_value][y_value] == '#':
                                    wall_find = True
                                    break
                                else: 
                                    space_count += 1

                            if space_count == len(level_hmap[level]):
                                space_find = True
                            
                            level += 1

                        if space_find:
                            max_level = max(level_hmap)

                            for level in range(max_level,-1,-1):

                                for y_value in level_hmap[level]:
                                    if dx == 1:
                                        grid[x+level+1][y_value] = grid[x+level][y_value]
                                        grid[x+level][y_value] = '.'
                                    else:
                                        grid[x-level-1][y_value] = grid[x-level][y_value]
                                        grid[x-level][y_value] = '.'
                            
                            x,y = nx,ny

        res = 0
        self.print_grid(grid)
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '[':
                    res += (x+1)*100+y+2

        return res