import re

class Read:
    def __init__(self, root):
        self._root = root
        self._file = open(root, 'r')
        lines = self._file.readlines()
        self._file.close()
        self._lines = self.clean_lines(lines)
        for line in self._lines:
            print(line)

    @staticmethod
    def clean_lines(lines):
        valid_list = []
        for line in lines:
            # Start with !
            r = re.match("^[!\n\#]", line)
            if not r:
                valid_list.append(line.rstrip("\n"))
        return valid_list