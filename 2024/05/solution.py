from utils.solution_base import SolutionBase

from collections import defaultdict,deque

class Solution(SolutionBase):
    
    def topological_order(self,graph,updates):
        
        updates_set = set(updates)
        sub_graph = defaultdict(list)
        sub_in_degree = defaultdict(int)

        for update in updates:
            if update in graph:
                sub_graph[update] = [neighbor for neighbor in graph[update] if neighbor in updates_set]
                for neighbor in sub_graph[update]:
                    sub_in_degree[neighbor] += 1
        
        queue = deque(update for update in updates if sub_in_degree[update] == 0)
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for neighbor in sub_graph[node]:
                sub_in_degree[neighbor] -= 1
                if not sub_in_degree[neighbor]: queue.append(neighbor)
        
        return topo_order

    def part1(self, data):
        
        graph = defaultdict(list)
        res = 0

        for i,line in enumerate(data):
            if line.rstrip('\n') == '': 
                data = data[i+1:]
                break
            x,y = map(int,line.rstrip('\n').split('|'))
            graph[x].append(y)

        for line in data:
            updates = list(map(int,line.rstrip('\n').split(',')))
            if updates == self.topological_order(graph,updates):
                n = len(updates)
                res += updates[n//2]

        return res


    def part2(self, data):
        
        graph = defaultdict(list)
        res = 0

        for i,line in enumerate(data):
            if line.rstrip('\n') == '': 
                data = data[i+1:]
                break
            x,y = map(int,line.rstrip('\n').split('|'))
            graph[x].append(y)

        for line in data:
            updates = list(map(int,line.rstrip('\n').split(',')))
            sorted_updates = self.topological_order(graph,updates)
            if updates != sorted_updates:
                n = len(updates)
                res += sorted_updates[n//2]

        return res