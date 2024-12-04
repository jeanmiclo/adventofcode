from utils.solution_base import SolutionBase

class Solution(SolutionBase):

    DIR = [(1,0),(0,1),(1,1),(1,-1),(-1,0),(0,-1),(-1,-1),(-1,1)]

    def find_coordonates_appearance(self,x,y,grid,word):

        m,n = len(grid),len(grid[0])

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n
        
        cnt = 0

        for dx,dy in self.DIR:
            nx,ny = x+dx,y+dy
            i = 1
            while is_valid(nx,ny) and grid[nx][ny] == word[i]:
                nx,ny = nx+dx,ny+dy
                i += 1
                if i == len(word):
                    cnt += 1
                    break
        
        return cnt

    def part1(self, data):

        grid = []

        for line in data:
            grid.append(line.rstrip('\n'))

        m,n = len(grid),len(grid[0])
        res = 0

        WORD = 'XMAS'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == WORD[0]:
                    res += self.find_coordonates_appearance(i,j,grid,WORD)

        return res
    
    def find_cross_word(self,x,y,grid,left_letter,right_letter):

        m,n = len(grid),len(grid[0])
        if x == 0 or y == 0 or x == m-1 or y == n-1: return 0

        if (grid[x-1][y-1] != grid[x+1][y+1] and grid[x-1][y-1] in (left_letter,right_letter) and grid[x+1][y+1] in (left_letter,right_letter)
            and grid[x+1][y-1] != grid[x-1][y+1] and grid[x+1][y-1] in (left_letter,right_letter) and grid[x-1][y+1] in (left_letter,right_letter)):
            return 1
        
        return 0


    def part2(self, data):

        grid = []

        for line in data:
            grid.append(line.rstrip('\n'))

        m,n = len(grid),len(grid[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'A':
                    res += self.find_cross_word(i,j,grid,'M','S')

        return res