from utils.solution_base import SolutionBase

class Solution(SolutionBase):

    def dfs(self,i,cmpt,target,equations,operands=['+','*']):
        if cmpt > target: return False
        if i >= len(equations):
            if cmpt == target: return True
            else: return False
        res = False
        for operand in operands:
            if operand == '||':
                val = self.dfs(i+1,int(str(cmpt)+str(equations[i])),target,equations,operands)
            elif operand == '+':
                val = self.dfs(i+1,cmpt+equations[i],target,equations,operands)
            elif operand == '*':
                val = self.dfs(i+1,cmpt*equations[i],target,equations,operands)
            res = res or val

        return res

    def part1(self, data):
        res = 0

        for line in data:
            ans,equations = line.rstrip("\n").split(': ')
            ans = int(ans)
            equations = list(map(int,equations.split(' ')))
            if self.dfs(1,equations[0],ans,equations):
                res += ans

        return res

    def part2(self, data):
        res = 0

        for line in data:
            ans,equations = line.rstrip("\n").split(': ')
            ans = int(ans)
            equations = list(map(int,equations.split(' ')))
            if self.dfs(1,equations[0],ans,equations,['+','*','||']):
                res += ans

        return res