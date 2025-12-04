from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):
        
        res = 0
        for line in data:
            line = line.rstrip("\n") 
            n = len(line)
            greatest = int(line[-1])
            mx = 0
            for i in range(n-2,-1,-1):
                mx = max(mx,int(line[i])*10 + greatest)
                if int(line[i]) > greatest:
                    greatest = int(line[i])
            
            res += mx
        return res

    def part2(self, data):
        
        res = 0
        for line in data:
            line = line.rstrip("\n") 
            n = len(line)
            stack = []
            for i in range(n):
                num = int(line[i])

                while stack and stack[-1] < num and len(stack)+n-i > 12:
                    stack.pop()
                
                stack.append(num)
            
            while len(stack) > 12:
                stack.pop()
            
            multiple = 0
            while stack:
                num = stack.pop()
                res += num * (10  ** multiple)
                multiple += 1
        return res
    