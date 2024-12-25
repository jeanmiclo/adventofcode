from utils.solution_base import SolutionBase
from collections import defaultdict

class Solution(SolutionBase):
    
    MODULO = 16777216
    LENGTH = 2000

    def part1(self, data): 
        
        res = 0

        def mix(nb,secret_number):
            return nb^secret_number

        def prune(secret_number):
            return secret_number%self.MODULO

        def find_secret_number(num,r):

            for _ in range(r):
                num = prune(mix(num,(num*64)))
                num = prune(mix(num//32,num))
                num = prune(mix(num,(num*2048)))
            
            return num

        for line in data:
            secret_number = int(line.rstrip('\n'))
            res += find_secret_number(secret_number,self.LENGTH)
        
        return res

    def part2(self, data):
        
        scores = defaultdict(int)

        def mix(nb,secret_number):
            return nb^secret_number

        def prune(secret_number):
            return secret_number%self.MODULO

        def find_changes(num,r):
            changes = [0]
            seq = [num%10]

            for _ in range(r):
                num = prune(mix(num,(num*64)))
                num = prune(mix(num//32,num))
                num = prune(mix(num,(num*2048)))
                seq.append(num%10)
                changes.append(seq[-1]-seq[-2])
            
            return seq,changes

        def find_scores(sequences,changes):

            seen = set()
            for i in range(1,self.LENGTH-3):
                key = tuple([changes[i+j] for j in range(4)])
                if key not in seen:
                    scores[key] += sequences[i+3]
                    seen.add(key)

        for line in data:
            secret_number = int(line.rstrip('\n'))
            find_scores(*find_changes(secret_number,self.LENGTH))

        return max(scores.values())