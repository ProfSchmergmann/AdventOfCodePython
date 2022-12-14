from days.day import Day


def create_rocks(lines: list[str]):
    rocks = set()
    for line in lines:
        prev_point = None
        for point in line.strip().split(' -> '):
            point = (int(point.split(',')[0]), int(point.split(',')[1]))
            if prev_point is None:
                prev_point = point
            else:
                x1, y1 = prev_point
                x2, y2 = point
                if x1 < x2:
                    for x in range(x1, x2):
                        rocks.add((x, y1))
                elif x1 > x2:
                    for x in range(x2, x1, -1):
                        rocks.add((x, y1))
                else:
                    if y1 < y2:
                        for y in range(y1, y2):
                            rocks.add((x1, y))
                    elif y1 > y2:
                        for y in range(y2, y1, -1):
                            rocks.add((x1, y))
                prev_point = point
            rocks.add(point)
    return rocks


class Day14(Day):

    def __init__(self):
        super().__init__(14)

    def part_a(self):
        matrix = create_rocks(self.get_lines_as_list())
        print(matrix)
        return ''

    def part_b(self):
        return ''
