import numpy as np

from days.day import Day


class Day1(Day):

    def __init__(self):
        super().__init__(1)

    def preprocess_input(self):
        list = []
        tmp = 0
        for line in self.get_lines_as_list():
            if line.strip():
                tmp += int(line)
            else:
                list.append(tmp)
                tmp = 0
        return list

    def part_a(self):
        return np.max(self.preprocess_input())

    def part_b(self):
        sorted_list = np.sort(self.preprocess_input())
        return sorted_list[-1] + sorted_list[-2] + sorted_list[-3]
