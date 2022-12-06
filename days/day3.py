from string import ascii_lowercase as asc_l
from string import ascii_uppercase as asc_u

from days.day import Day


def first_element_intersection(strings):
    intersect = set.intersection(*[set(c for c in string) for string in strings])
    return '' if len(intersect) == 0 else list(intersect)[0]


class Day3(Day):
    priorities = {letter: value for letter, value in zip(asc_l + asc_u, range(1, 53))}

    def __init__(self):
        super().__init__(3)

    def part_a(self):
        res = 0
        for line in self.get_lines_as_list():
            res += self.priorities[first_element_intersection([line[0:len(line) // 2],
                                                               line[len(line) // 2:].replace('\n', '')])]
        return res

    def part_b(self):
        res = 0
        lines = self.get_lines_as_list()
        for i in range(len(lines)):
            if (i + 1) % 3 == 0:
                c = first_element_intersection([
                    lines[i - 2].replace('\n', ''),
                    lines[i - 1].replace('\n', ''),
                    lines[i].replace('\n', '')]
                )
                if self.priorities.__contains__(c):
                    res += self.priorities[c]

        return res
