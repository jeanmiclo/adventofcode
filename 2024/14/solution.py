from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data):

        M,N = 103,101
        MIDDLE_M,MIDDLE_N = M//2,N//2
        SECONDS = 100

        cnt = defaultdict(int)

        for line in data:
            p1,p2 = line.rstrip('\n').split(' ')
            y,x = map(int,p1[2:].split(','))
            dy,dx = map(int,p2[2:].split(','))
            x = (x +dx*SECONDS)%M 
            y = (y +dy*SECONDS)%N

            if x < MIDDLE_M and y < MIDDLE_N:
                cnt[0] += 1
            elif x < MIDDLE_M and y > MIDDLE_N:
                cnt[1] += 1
            elif x > MIDDLE_M and y < MIDDLE_N:
                cnt[2] += 1
            elif x > MIDDLE_M and y > MIDDLE_N:
                cnt[3] += 1
        
        res = 1
        for v in cnt.values():
            res *= v
        return res

    def part2(self, data):

        M,N = 103,101
        SECONDS = 7916

        """
        for s in range(10000):
            hmap = defaultdict(int)
            for line in data:
                p1,p2 = line.rstrip('\n').split(' ')
                y,x = map(int,p1[2:].split(','))
                dy,dx = map(int,p2[2:].split(','))
                x = (x +dx*s)%M 
                y = (y +dy*s)%N
                hmap[(x,y)] += 1
                if hmap[(x,y)] > 1: break
            
            if len(hmap) == 500: print(s)
        """
        
        hmap = defaultdict(int)
        for line in data:
            p1,p2 = line.rstrip('\n').split(' ')
            y,x = map(int,p1[2:].split(','))
            dy,dx = map(int,p2[2:].split(','))
            x = (x +dx*SECONDS)%M 
            y = (y +dy*SECONDS)%N

            hmap[(x,y)]

        for x in range(M):
            for y in range(N):
                if (x,y) in hmap:
                    print('X',end='')
                else:
                    print('.',end='')
            print('')
        
        return None