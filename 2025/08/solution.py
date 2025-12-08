from utils.solution_base import SolutionBase

from collections import defaultdict,Counter

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y: return False
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    
def distance(p1,p2):
    return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2 + (p1[2]-p2[2]) ** 2) ** 0.5

import heapq

class Solution(SolutionBase):

    def part1(self, data):

        points = []
        for line in data:
            elt = list(map(int,line.rstrip().split(',')))
            points.append(elt)
        
        hq = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                d = distance(points[i],points[j])
                heapq.heappush(hq,(d,i,j))
        
        dsu = UnionFind(n)
        
        for i in range(1000):
            _,x,y = heapq.heappop(hq)
            dsu.union(x,y)
        
        for i in range(n):
            dsu.find(i)
        
        hmap = Counter(dsu.parent)
        values = sorted(hmap.values(),reverse=True)[:3]

        return values[0] * values[1] * values[2]

    def part2(self, data):

        points = []
        for line in data:
            elt = list(map(int,line.rstrip().split(',')))
            points.append(elt)
        
        hq = []
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                d = distance(points[i],points[j])
                heapq.heappush(hq,(d,i,j))
        
        dsu = UnionFind(n)
        
        cnt = 0
        while True:
            _,x,y = heapq.heappop(hq)
            if dsu.union(x,y):
                cnt += 1
                if cnt == 999:
                    return points[x][0] * points[y][0] 
        
        return None