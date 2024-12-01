from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):
        left, right = [], []

        for line in data:
            l,r  = map(int, line.rstrip("\n").split())
            left.append(l)
            right.append(r)

        distance = sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))
        return distance

    def part2(self, data):
        hmap_left,hmap_right = defaultdict(int),defaultdict(int)

        for line in data:
            l,r  = map(int, line.rstrip("\n").split())
            hmap_left[l] += 1
            hmap_right[r] += 1

        score = sum(x*hmap_left[x]*hmap_right[x] for x in hmap_left.keys())
        return score