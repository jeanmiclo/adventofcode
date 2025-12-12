from functools import cache
from utils.solution_base import SolutionBase

from collections import defaultdict
from bisect import bisect_left,bisect_right

class Solution(SolutionBase):

    def part1(self, data):

        graph = defaultdict(list)
        start = "you"
        end = "out"

        @cache
        def dfs(node):
            res = 0
            if node == end:
                res = 1
            
            for next in graph[node]:
                res += dfs(next)
            
            return res

        for line in data:
            u,*child = line.rstrip().split(' ')
            u = u[:-1]
            for v in child:
                graph[u].append(v)

        return dfs(start)

    def part2(self, data):

        graph = defaultdict(list)
        start = "svr"
        end = "out"

        node1 = "dac"
        node2 = "fft"

        @cache
        def dfs(node,n1,n2):
            res = 0
            if node == end and n1 and n2:
                res = 1
            
            if node == node1: n1 = True
            if node == node2: n2 = True
            
            for next in graph[node]:
                res += dfs(next,n1,n2)
            
            return res

        for line in data:
            u,*child = line.rstrip().split(' ')
            u = u[:-1]
            for v in child:
                graph[u].append(v)

        return dfs(start,False,False)