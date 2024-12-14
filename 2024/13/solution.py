from utils.solution_base import SolutionBase

import re

class Solution(SolutionBase):

    def part1(self, data):
        n = len(data)
        i = 0
        res = 0

        while i < n:
            ax, ay = map(int, re.findall(r'(\d+)', data[i]))
            bx, by = map(int, re.findall(r'(\d+)', data[i+1]))
            x, y   = map(int, re.findall(r'(\d+)', data[i+2]))
            A = (bx*y - by*x) / (bx*ay - by*ax)
            B = (x-ax*A) / bx

            if abs(A - round(A)) < 0.00001 and abs(B - round(B)) < 0.00001:
                res += 3*A + B
        
            i += 4

        return int(res)

    def part2(self, data):
        n = len(data)
        i = 0
        res = 0

        while i < n:
            ax, ay = map(int, re.findall(r'(\d+)', data[i]))
            bx, by = map(int, re.findall(r'(\d+)', data[i+1]))
            x, y  = map(int, re.findall(r'(\d+)', data[i+2]))
            x += 10000000000000
            y += 10000000000000
            A = (bx*y - by*x) / (bx*ay - by*ax)
            B = (x-ax*A) / bx

            if abs(A - round(A)) < 0.00001 and abs(B - round(B)) < 0.00001:
                res += 3*A + B
        
            i += 4

        return int(res)