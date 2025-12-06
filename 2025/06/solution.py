from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def to_map1(self,data):

        map = []
        for line in data:
            new_s = ''
            s = line.rstrip('\n')
            for i,c in enumerate(s):
                if c == ' ' and s[i-1] == ' ':
                    continue
                else:
                    new_s += c
            map.append(list(new_s.lstrip(' ').rstrip(' ').split(' ')))

        return map

    def to_map2(self,data):

        n = len(data[0])-1
        new_col_idx = []

        s = data[-1].rstrip()
        map = [[s[0]]]
        for i,c in enumerate(s):
            if c != ' ' and i != 0:
                new_col_idx.append(i)
                map.append([c])

        m = len(data)

        k = 0
        for i in range(n):
            val = 0
            if k < len(new_col_idx) and i == new_col_idx[k]:
                k += 1
            for j in range(m-1):
                if data[j][i] != ' ':
                    val = val*10 + int(data[j][i])
            
            if val != 0:
                map[k].append(val)
            
        return map

    def part1(self, data):
        map = self.to_map1(data)
        m,n = len(map),len(map[0])

        res = 0
        for j in range(n):
            if map[-1][j] == '*':
                mult = True
                ans = 1
            else:
                mult = False
                ans = 0

            for i in range(m-1):
                if mult:
                    ans *= int(map[i][j])
                else:
                    ans += int(map[i][j])
            
            res += ans

        return res

    def part2(self, data):

        map = self.to_map2(data)
        m = len(map)

        res = 0
        for i in range(m):
            if map[i][0] == '*':
                mult = True
                ans = 1
            else:
                mult = False
                ans = 0

            for j in range(1,len(map[i])):
                if mult:
                    ans *= map[i][j]
                else:
                    ans += map[i][j]
            
            res += ans

        return res