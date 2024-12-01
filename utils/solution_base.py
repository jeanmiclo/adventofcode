
class SolutionBase:

    def __init__(self,data):
        self.data = data

    def solve(self, part_num: int):
        func = getattr(self, f"part{part_num}")
        return func(self.data)