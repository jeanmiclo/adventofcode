from utils.solution_base import SolutionBase

from collections import defaultdict

class Solution(SolutionBase):

    def is_safe(self,arr):
        increasing = None
        
        for i in range(1,len(arr)):
            if increasing is None:
                if arr[i] > arr[i-1]: increasing = True
                if arr[i] < arr[i-1]: increasing = False

            diff = arr[i] - arr[i-1]
            if increasing and (diff < 1 or diff > 3): return False
            if not increasing and (diff > -1 or diff < -3): return False
        
        return True

    def is_safe_bis(self,arr):
        increasing = None
        count = 0
        
        for i in range(1,len(arr)):
            if increasing is None:
                if arr[i] > arr[i-1]: increasing = True
                if arr[i] < arr[i-1]: increasing = False

            diff = arr[i] - arr[i-1]
            if increasing and (diff < 1 or diff > 3): 
                if count: return False
                else: count += 1
            if not increasing and (diff > -1 or diff < -3): 
                if count: return False
                else: count += 1
        
        return True

    def part1(self, data):

        safe_number = 0

        for line in data:
            if self.is_safe(list(map(int, line.rstrip("\n").split()))):
                safe_number += 1

        return safe_number

    def part2(self, data):

        safe_number = 0

        for line in data:
            if self.is_safe_bis(list(map(int, line.rstrip("\n").split()))):
                safe_number += 1

        return safe_number