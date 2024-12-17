from utils.solution_base import SolutionBase
from collections import defaultdict
import heapq

class Solution(SolutionBase):

    def part1(self, data):

        A = int(data[0].rstrip("\n").split(':')[1])
        B = int(data[1].rstrip("\n").split(':')[1])
        C = int(data[2].rstrip("\n").split(':')[1])

        out = []

        def combo_operand(operand):
            if operand < 4: return operand
            if operand == 4: return A
            if operand == 5: return B
            if operand == 6: return C 

        instructions = list(map(int,data[4].rstrip("\n").split(':')[1].split(',')))

        i = 0
        while i < len(instructions):
            opcode,operand = instructions[i:i+2]

            if opcode == 0:
                A = int(A/2**combo_operand(operand))
            elif opcode == 1:
                B ^= operand
            elif opcode == 2:
                B = combo_operand(operand) % 8
            elif opcode == 3:
                if A != 0:
                    i = operand
                else:
                    i += 2
            elif opcode == 4:
                B ^= C
            elif opcode == 5:
                out.append(combo_operand(operand) % 8)
            elif opcode == 6:
                B = int(A/2**combo_operand(operand))
            elif opcode == 7:
                C = int(A/2**combo_operand(operand))
            
            if opcode != 3: i += 2

        return ','.join(map(str,out))
    
    def run_program(self, registers, program):
        def combo_operand(value):
            match value:
                case 0 | 1 | 2 | 3:
                    return value
                case 4:
                    return A
                case 5:
                    return B
                case 6:
                    return C

        A, B, C = registers
        pointer = 0
        outputs = []

        while pointer < len(program):
            opcode = program[pointer]
            operand = program[pointer + 1]

            if opcode == 0:  # adv
                A //= 2 ** combo_operand(operand)
            elif opcode == 1:  # bxl
                B ^= operand
            elif opcode == 2:  # bst
                B = combo_operand(operand) % 8
            elif opcode == 3:  # jnz
                if A != 0:
                    pointer = operand
                    continue  # skip the pointer increment
            elif opcode == 4:  # bxc
                B ^= C
            elif opcode == 5:  # out
                outputs.append(combo_operand(operand) % 8)
            elif opcode == 6:  # bdv
                B = A // (2 ** combo_operand(operand))
            elif opcode == 7:  # cdv
                C = A // (2 ** combo_operand(operand))

            pointer += 2

        return outputs

    def part2(self, data):
        program = list(map(int, data[4].split(": ")[1].split(",")))

        A = sum(7 * 8**i for i in range(len(program) - 1)) + 1

        while True:
            result = self.run_program([A, 0, 0], program)
            if result == program:
                return A
            add = 0
            for i in range(len(result) - 1, -1, -1):
                if result[i] != program[i]:
                    add = 8**i
                    A += add
                    break