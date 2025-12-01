from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):

        cur = 50
        res = 0

        for line in data:
            current_line = line.rstrip("\n")
            direction = current_line[0]
            steps = int(current_line[1:])

            cur = (cur + steps if direction == 'R' else cur - steps) % 100

            if cur == 0:
                res += 1

        return res

    def part2(self, data):

        cur = 50
        res = 0

        for line in data:
            current_line = line.rstrip("\n")
            direction = current_line[0]
            steps = int(current_line[1:])

            if direction == 'R':
                res += (cur+steps) // 100
            else:
                if cur == 0:
                    res -= 1
                res += (cur-steps-100) // (-100)

            cur = (cur + steps if direction == 'R' else cur - steps) % 100
            
            print(cur,res)

        return res