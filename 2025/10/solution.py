from utils.solution_base import SolutionBase

from collections import defaultdict,deque
from bisect import bisect_left,bisect_right
from z3 import *

class Solution(SolutionBase):
    

    def part1(self, data):

        def helper(mask,buttons):
            time = 0
            visited = set([mask])
            q = deque([mask])

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    if cur == 0: return time
                    for button in buttons:
                        nxt = cur
                        for v in button:
                            nxt  ^= (1<<v)
                        
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
                time += 1

            return -1

        res = 0

        for line in data:
            line = line.rstrip()
            lights,*buttons,joltage = line.split(' ')
            mask = 0
            for i,c in enumerate(lights[1:-1]):
                if c == '#':
                    mask |= (1<<i)
            button_list = []
            for button in buttons:
                button_list.append(list(map(int,button[1:-1].split(','))))
            
            res += helper(mask,button_list)

        return res

    def part2(self, data):

        def helper(target,buttons):
            opt = Optimize()
    
            button_vars = [Int(f'b_{i}') for i in range(len(buttons))]
            print(button_vars)
            for b in button_vars:
                opt.add(b >= 0)
            
            num_counters = len(target)
            for counter_idx in range(num_counters):
                contributors = []
                for b_idx, affected_indices in enumerate(buttons):
                    if counter_idx in affected_indices:
                        contributors.append(button_vars[b_idx])
                
                opt.add(Sum(contributors) == target[counter_idx])
                
            total_presses = Sum(button_vars)
            opt.minimize(total_presses)
            
            if opt.check() == sat:
                model = opt.model()
                result = model.eval(total_presses).as_long()
                return result

        res = 0

        for i,line in enumerate(data):
            line = line.rstrip()
            lights,*buttons,joltage = line.split(' ')

            button_list = []
            for button in buttons:
                button_list.append(list(map(int,button[1:-1].split(','))))
            
            joltage = list(map(int,joltage[1:-1].split(',')))
            
            res += helper(joltage,button_list)

        return res