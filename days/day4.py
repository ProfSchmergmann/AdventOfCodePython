from days.day import Day


def split_pair_from_line(line):
    first_pair = line.split(',')[0]
    second_pair = line.split(',')[1].replace('\n', '')
    first_pair_start = int(first_pair.split('-')[0])
    first_pair_end = int(first_pair.split('-')[1])
    second_pair_start = int(second_pair.split('-')[0])
    second_pair_end = int(second_pair.split('-')[1])
    return first_pair_start, first_pair_end, second_pair_start, second_pair_end


class Day4(Day):
    def __init__(self):
        super().__init__(4)

    def part_a(self):
        res = 0
        for line in self.get_lines_as_list():
            first_pair_start, first_pair_end, second_pair_start, second_pair_end = split_pair_from_line(line)
            if ((second_pair_start <= first_pair_start <= first_pair_end <= second_pair_end) or
                    (first_pair_start <= second_pair_start <= second_pair_end <= first_pair_end)):
                res += 1
        return res

    def part_b(self):
        res = 0
        for line in self.get_lines_as_list():
            first_pair_start, first_pair_end, second_pair_start, second_pair_end = split_pair_from_line(line)
            if ((second_pair_start <= first_pair_end <= second_pair_end) or
                    (first_pair_start <= second_pair_end <= first_pair_end) or
                    (second_pair_start <= first_pair_start <= second_pair_end) or
                    (first_pair_start <= second_pair_start <= first_pair_end)):
                res += 1
        return res
