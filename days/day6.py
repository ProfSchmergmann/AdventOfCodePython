from days.day import Day


def process(line: str, window_length: int):
    i = 0
    window = []
    for c in line:
        if len(window) == window_length:
            return i
        if window.__contains__(c):
            idx = window.index(c)
            window = window[idx + 1:]
            window.append(c)
            i += 1
            continue
        window.append(c)
        i += 1
    return i


class Day6(Day):

    def __init__(self):
        super().__init__(6)

    def part_a(self):
        return process(self.get_lines_as_list()[0], 4)

    def part_b(self):
        return process(self.get_lines_as_list()[0], 14)
