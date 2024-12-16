from utils.solution_base import SolutionBase
from collections import defaultdict
import heapq

class Solution(SolutionBase):

    DIR = [(0,1),(1,0),(0,-1),(-1,0)]

    def print_grid(self,grid):
        m,n = len(grid),len(grid[0])

        for x in range(m):
            for y in range(n):
                print(grid[x][y],end='')
            print('')
        print('')

    def is_valid(self,x,y,m,n):
        return 0 <= x < m and 0 <= y < n
    
    def get_grid(self,data):

        xs = ys = xe = ye = 0
        
        grid = []

        for i,line in enumerate(data):
            row = []
            for j,c in enumerate(line.rstrip('\n')):
                if c == 'S': 
                    xs,ys = i,j
                elif c == 'E': 
                    xe,ye = i,j
                row.append(c)
            grid.append(row)

        return xs,ys,xe,ye,grid

    def part1(self, data):
        xs,ys,xe,ye,grid = self.get_grid(data)
        hq = [(0,0,xs,ys)]

        hmap = {}

        while hq:
            score,direction,x,y = heapq.heappop(hq)
            if x == xe and y == ye: return score

            for i,(dx,dy) in enumerate(self.DIR):
                nx,ny = x+dx,y+dy
                if grid[nx][ny] != '#':
                    rotate = abs(direction-i)
                    if rotate == 3: rotate = 1
                    new_score = score + rotate*1000 + 1

                    if (nx,ny) not in hmap:
                        hmap[(nx,ny)] = new_score
                        heapq.heappush(hq,(new_score,i,nx,ny))
                    else:
                        if new_score < hmap[(nx,ny)]+1000:
                            hmap[(nx,ny)] = new_score
                            heapq.heappush(hq,(new_score,i,nx,ny))


        self.print_grid(grid)

        return None

    def part2(self, data):
        sx,sy,ex,ey,grid = self.get_grid(data)
        
        ed = 0
        best_dist = float('inf')

        start = (sx,sy,0)
        pq = []
        heapq.heappush(pq,(0,start))

        dists = defaultdict(lambda : float('inf'))
        from_ = defaultdict(lambda : set())


        def adjs(cur):
            cx,cy,cd = cur
            yield 1000, (cx,cy,(cd-1)%4)
            yield 1000, (cx,cy,(cd+1)%4)
            dx,dy = self.DIR[cd]
            nx,ny = cx+dx,cy+dy
            if grid[nx][ny] != '#':
                yield 1,(nx,ny,cd)

        while len(pq) > 0:

            dist,cur = heapq.heappop(pq)
            (cx,cy,cd) = cur
            if (cx,cy) == (ex,ey): 
                if dist < best_dist:
                    best_dist = dist
                    ed = cd
                continue

            for d,adj in adjs(cur):
                if dist + d < dists[adj]:
                    dists[adj] = dist+d
                    heapq.heappush(pq,(dists[adj],adj))
                    from_[adj] = {(cur)}
                elif dist+d == dists[adj]:
                    from_[adj].add(cur)
        
        stack = [(ex,ey,ed)]
        states = set(stack)

        while len(stack) > 0:
            state = stack.pop()
            for _state in from_[state]:
                if _state not in states:
                    states.add(_state)
                    stack.append(_state)

        return len(set(x[:2] for x in states))