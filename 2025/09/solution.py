from utils.solution_base import SolutionBase

from collections import defaultdict
from bisect import bisect_left,bisect_right

class Solution(SolutionBase):

    def part1(self, data):

        points = []

        for line in data:
            x,y = map(int,line.rstrip().split(','))
            points.append((x,y))

        n = len(points)
        res = 0
        for i in range(n):
            p1 = points[i]
            for j in range(i+1,n):
                p2 = points[j]
                dx = abs(p1[0]-p2[0]) + 1
                dy = abs(p1[1]-p2[1]) + 1
                res = max(res,dx*dy)

        return res

    def part2(self, data):

        points = []

        for line in data:
            x, y = map(int, line.rstrip().split(','))
            points.append((x, y))

        n = len(points)
        hmap_x = defaultdict(set)
        hmap_y = defaultdict(set)

        for i in range(n):
            p1 = points[i]
            p2 = points[i-1] 

            mxx = max(p1[0], p2[0])
            mnx = min(p1[0], p2[0])
            mxy = max(p1[1], p2[1])
            mny = min(p1[1], p2[1])

            if mxx == mnx: 
                for y in range(mny, mxy + 1):
                    hmap_x[mxx].add(y)
                    hmap_y[y].add(mxx)
            else: 
                for x in range(mnx, mxx + 1):
                    hmap_x[x].add(mxy)
                    hmap_y[mxy].add(x)
        
        for k,v in hmap_x.items():
            hmap_x[k] = sorted(v)

        for k,v in hmap_y.items():
            hmap_y[k] = sorted(v)

        res = 0
        for i in range(n):
            p1 = points[i]
            for j in range(i + 1, n): 
                p2 = points[j]
                
                rect_mnx = min(p1[0], p2[0])
                rect_mxx = max(p1[0], p2[0])
                rect_mny = min(p1[1], p2[1])
                rect_mxy = max(p1[1], p2[1])

                dx = rect_mxx - rect_mnx + 1
                dy = rect_mxy - rect_mny + 1
                
                good = True

                y_inner_bottom = rect_mny + 1
                y_inner_top = rect_mxy - 1
                x_inner_left = rect_mnx + 1
                x_inner_right = rect_mxx - 1
                
                list_y_left = hmap_x.get(x_inner_left, [])
                if bisect_right(list_y_left, y_inner_top) - bisect_left(list_y_left, y_inner_bottom) > 0:
                    good = False
                
                    list_y_right = hmap_x.get(rect_mxx - 1, [])
                    if bisect_right(list_y_right, y_inner_top) - bisect_left(list_y_right, y_inner_bottom) > 0:
                        good = False

                if good:
                    list_x_bottom = hmap_y.get(y_inner_bottom, [])
                    if bisect_right(list_x_bottom, x_inner_right) - bisect_left(list_x_bottom, x_inner_left) > 0:
                        good = False

                if good:
                    list_x_top = hmap_y.get(rect_mxy - 1, [])
                    if bisect_right(list_x_top, x_inner_right) - bisect_left(list_x_top, x_inner_left) > 0:
                        good = False
                
                if good:
                    res = max(res, dx * dy)

        return res