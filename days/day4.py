from days.day import Day


class Day4(Day):
    def __init__(self):
        super().__init__(4)

    def part_a(self):
        res = 0
        for line in self.get_lines_as_list():
            a, b, x, y = map(int, line.replace(",", "-").split("-"))
            if (x <= a <= b <= y) or (a <= x <= y <= b):
                res += 1
        return res

    def part_b(self):
        res = 0
        for line in self.get_lines_as_list():
            a, b, x, y = map(int, line.replace(",", "-").split("-"))
            if (x <= b <= y) or (a <= y <= b) or (x <= a <= y) or (a <= x <= b):
                res += 1
        return res
