from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):

    def part1(self, data): 

        value = defaultdict(lambda : None)

        for i,line in enumerate(data):
            if line == '\n': break
            x,v = line.rstrip('\n').split(':')
            value[x] = int(v)

        instructions = []

        for line in data[i+1:]:
            instructions.append(line.rstrip('\n').split(' '))

        while len(instructions) > 0:
            for i,instruction in enumerate(instructions):
                v1,operator,v2,_,v3 = instruction
                if value[v1] is not None and value[v2] is not None:
                    if operator == 'OR':
                        value[v3] = value[v1] | value[v2]
                    elif operator == 'XOR':
                        value[v3] = value[v1] ^ value[v2]
                    else :
                        value[v3] = value[v1] & value[v2]

                    instructions.remove(instruction)

        res = 0
        i = 0

        for k in sorted(value):
            if k[0] == 'z':
                res += value[k] << i
                i += 1

        return res

    def part2(self, data):

        operations = []
        op_per_var = defaultdict(set)

        for line in data[92:]:
            operations.append(line.rstrip('\n').split(' '))

        for var1, op, var2, _, _ in operations:
            op_per_var[var1].add(op)
            op_per_var[var2].add(op)

        wrong = set()
        for var1, op, var2, _, res in operations:
            if res.startswith("z") and op != "XOR":
                wrong.add(res)
            elif op == "XOR" and all(x[0] not in ("x", "y", "z") for x in (res[0], var1[0], var2[0])):
                wrong.add(res)
            elif op != "OR":
                if (op == "AND") == ("OR" not in op_per_var[res]):
                    wrong.add(res)

        print(",".join(sorted(wrong - {next(out for var1, op, var2, _,out in operations if "x00" in (var1, var2)), "z45"})))