from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data): 

        graph = defaultdict(list)

        for line in data:
            x,y = line.rstrip('\n').split('-')
            graph[x].append(y)
            graph[y].append(x)

        triplet = set()

        for k in graph.keys():
            if k[0] == 't':
                for k2 in graph[k]:
                    for k3 in graph[k2]:
                        if k != k2 != k3 and k in graph[k3]:
                            triplet.add(tuple(sorted([k,k2,k3])))

        return len(triplet)

    def part2(self, data):

        graph = defaultdict(set)

        for line in data:
            x,y = line.rstrip('\n').split('-')
            graph[x].add(y)
            graph[y].add(x)
        

        def find_largest(_set,k):
            
            if len(_set) == len(_set&graph[k]):
                _set.add(k)
                largest = set()

                for neighbor in graph[k]:
                    if neighbor not in _set:
                        largest = max(largest,find_largest(_set,neighbor),key=len)
                return largest

            return _set

        max_v = float('-inf')
        res = None

        for k in graph.keys():
            _set = find_largest(set(),k)
            if len(_set) > max_v:
                max_v = len(_set)
                res = _set

        return ','.join(sorted(list(res)))