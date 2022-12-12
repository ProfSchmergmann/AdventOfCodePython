import time
from abc import ABC, abstractmethod


class Day(ABC):
    @abstractmethod
    def part_a(self):
        pass

    @abstractmethod
    def part_b(self):
        pass

    def __init__(self, number: int):
        self.filename = f'res/day{number}.txt'
        self.number = number

    def get_lines_as_list(self):
        with open(self.filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def print_with_time(self, part):
        res, time_ns, time_s = self.get_res_with_time(part)
        print(f'Result for Day {self.number} part {part}: {res}, took {time_ns:.2e} ns,'
              f' which is {time_s:.2f}s.')

    def get_res_with_time(self, part):
        t0 = time.time_ns()
        res = self.part_a() if part == 'a' else self.part_b()
        t1 = time.time_ns()
        return res, (t1 - t0), ((t1 - t0) * 10e-9)

    def print_part_a_and_b_with_time(self):
        self.print_with_time('a')
        self.print_with_time('b')
