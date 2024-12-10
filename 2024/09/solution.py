from utils.solution_base import SolutionBase

from sortedcontainers import SortedList
from collections import deque

class Solution(SolutionBase):

    def part1(self, data):
        
        queue = deque(map(int,data[0].rstrip('\n')))

        res = 0
        min_id = 0
        max_id = len(queue)//2
        i = 0
        block_nb = 0
        right_blocks = queue.pop()

        while queue:
            digit = queue.popleft()
            i += 1

            if i & 1:
                for j in range(digit):
                    res += min_id * (block_nb+j)

                min_id += 1
            else:
                for j in range(digit):
                    res += max_id * (block_nb+j)
                    right_blocks -= 1
                    if right_blocks == 0:
                        max_id -= 1
                        if len(queue) > 1:
                            queue.pop()
                            right_blocks = queue.pop()
                        else:
                            return res
            
            block_nb += digit
        
        for i in range(right_blocks):
            res += max_id * (block_nb+i)

        return res
    

    def search(self,arr,val):

        for start,size in arr:
            if size >= val: 
                return start,size
        
        return None,None

    def part2(self, data):

        block_list = map(int,data[0].rstrip('\n'))
        start = 0
        files_list = []
        space_list = SortedList()

        for i,block in enumerate(block_list):
            if not block: continue
            if i&1:
                space_list.add((start,block))
            else:
                files_list.append([start,block])
            start += block

        new_file = []

        for idx in range(len(files_list)-1,-1,-1):
            start,length = files_list[idx]
            _start,_size = self.search(space_list,length)
            if _size is not None and _start < start:
                space_list.remove((_start,_size))
                if _size-length > 0:
                    space_list.add((_start+length,_size-length))
                new_file.append((_start,length,idx))
            else:
                new_file.append((start,length,idx))

        new_file.sort(key=lambda x: x[2])
        res = 0
        for start,length,_id in new_file:
            for i in range(length):
                res += (start+i)*_id

        return res