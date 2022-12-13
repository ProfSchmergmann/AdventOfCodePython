from days.day import Day


def compare(left, right):
    if type(left) is int:
        if type(right) is int:
            return left - right
        else:
            return compare([left], right)
    else:
        if type(right) is int:
            return compare(left, [right])

    for i, j in zip(left, right):
        c = compare(i, j)
        if c:
            return c

    return len(left) - len(right)


class Day13(Day):

    def __init__(self):
        super().__init__(13)

    def part_a(self):
        right_order_indices = []
        splitted_lines = list(map(str.splitlines, open(self.filename, 'r').read().strip().split('\n\n')))
        for i, (left, right) in enumerate(splitted_lines):
            if (compare(eval(left), eval(right))) < 0:
                right_order_indices.append(i + 1)
        return sum(right_order_indices)

    def part_b(self):
        splitted_lines = list(map(eval, open(self.filename, 'r').read().split()))
        divider_2 = 1
        divider_6 = 2
        for packet in splitted_lines:
            if compare(packet, [[2]]) < 0:
                divider_2 += 1
                divider_6 += 1
            elif compare(packet, [[6]]) < 0:
                divider_6 += 1
        return divider_2 * divider_6
