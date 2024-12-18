from utils.solution_base import SolutionBase
from collections import defaultdict
import heapq

class Solution(SolutionBase):

    DIR = [(0,1),(1,0),(0,-1),(-1,0)]
    N = 71

    def print_grid(self,hmap,time):

        m = n = self.N

        for x in range(m):
            for y in range(n):
                if 0 < hmap[(x,y)] <= time:
                    print('#',end='')
                else:
                    print('.',end='')
            print('')
        print('')

    def dijkstra(self, hmap, value):

        start = (0,0)
        pq = []
        heapq.heappush(pq,(0,start))

        dists = defaultdict(lambda : float('inf'))

        def adjs(x,y):
            for dx,dy in self.DIR:
                nx,ny = x+dx,y+dy
                if 0 <= nx < self.N and 0 <= ny < self.N and hmap[(nx,ny)] > value-1:
                    yield 1,(nx,ny)

        while len(pq) > 0:
            dist,(x,y) = heapq.heappop(pq)
            if (x,y) == (self.N-1,self.N-1): 
                return dist

            for d,adj in adjs(x,y):
                if dist + d < dists[adj]:
                    dists[adj] = dist+d
                    heapq.heappush(pq,(dists[adj],adj))
        
        return None

    def part1(self, data): 

        hmap = defaultdict(lambda : float('inf'))

        for i,line in enumerate(data):
            x,y = map(int,line.rstrip('\n').split(','))
            hmap[(y,x)] = i
        
        return self.dijkstra(hmap,1024)

    def part2(self, data):

        hmap = defaultdict(lambda : float('inf'))

        for i,line in enumerate(data):
            x,y = map(int,line.rstrip('\n').split(','))
            hmap[(y,x)] = i

        l,r = 0,len(hmap)

        while l < r:
            m = l + (r-l)//2
            if self.dijkstra(hmap,m):
                l = m+1
            else: r = m
        
        for k,v in hmap.items():
            if v == l-1: print(list(reversed(k)))