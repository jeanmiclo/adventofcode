import os

class FileReader:
    def __init__(self, year, day, part):
        self.file_path = os.path.join(str(year), str(day), f'input.txt')
        self.file_path_part = os.path.join(str(year), str(day), f'input{part}.txt')
    
    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            return lines
        except Exception:
            try:
                with open(self.file_path_part, 'r') as file:
                    lines = file.readlines()
                return lines
            except Exception:
                return []