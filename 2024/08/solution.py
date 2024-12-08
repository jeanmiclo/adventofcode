from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):

        hmap = defaultdict(list)
        visited = set()
        m = len(data)

        for i,line in enumerate(data):
            n = len(line.rstrip('\n'))
            for j,element in enumerate(line.rstrip('\n')):
                if element != '.': 
                    hmap[element].append((i,j))

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        for v in hmap.values():
            for i,(x1,y1) in enumerate(v):
                for x2,y2 in v[i+1:]:
                    dx,dy = x2-x1,y2-y1
                    nx1,ny1 = x1-dx,y1-dy
                    if is_valid(nx1,ny1): visited.add((nx1,ny1))
                    nx2,ny2 = x2+dx,y2+dy
                    if is_valid(nx2,ny2): visited.add((nx2,ny2))

        return len(visited)

    def part2(self, data):

        hmap = defaultdict(list)
        visited = set()
        m = len(data)

        for i,line in enumerate(data):
            n = len(line.rstrip('\n'))
            for j,element in enumerate(line.rstrip('\n')):
                if element != '.': 
                    hmap[element].append((i,j))

        def is_valid(x,y):
            return 0 <= x < m and 0 <= y < n

        for v in hmap.values():
            for i,(x1,y1) in enumerate(v):
                for x2,y2 in v[i+1:]:
                    dx,dy = x2-x1,y2-y1
                    visited.add((x1,y1))
                    visited.add((x2,y2))
                    nx1,ny1 = x1-dx,y1-dy
                    while (is_valid(nx1,ny1)):
                        visited.add((nx1,ny1))
                        nx1,ny1 = nx1-dx,ny1-dy
                    nx2,ny2 = x2+dx,y2+dy
                    while (is_valid(nx2,ny2)):
                        visited.add((nx2,ny2))
                        nx2,ny2 = nx2+dx,ny2+dy

        return len(visited)