from queue import LifoQueue
from days.day import Day


def get_move_from_line(line):
    m = line.replace('move', '').replace('from', '').replace('to', '').replace('\n', '').split('  ')
    return int(m[0]), int(m[1]), int(m[2])


def get_stacks(lines):
    for i in range(len(lines)):
        if lines[i].replace('\n', '') == '':
            stack_line = lines[i - 1].replace('\n', '')
            stack_line_index = i - 1
            break
        i += 1

    stack_indexes = []
    for i in range(len(stack_line)):
        if stack_line[i] != ' ':
            stack_indexes.append(i)
        i += 1

    stacks = {}
    for i in range(len(stack_indexes)):
        stacks.update({i + 1: LifoQueue()})

    for i in range(stack_line_index - 1, -1, -1):
        line = lines[i].replace('\n', '')
        for j in range(len(line)):
            if str.isalpha(line[j]):
                stacks.get(stack_indexes.index(j) + 1).put(line[j])

    return stack_line_index, stacks, stack_indexes


class Day5(Day):

    def __init__(self):
        super().__init__(5)

    def part_a(self):
        lines = self.get_lines_as_list()
        stack_line_index, stacks, stack_indexes = get_stacks(lines)
        moves = lines[stack_line_index + 2:]
        for move in moves:
            amount, start, end = get_move_from_line(move)
            for k in range(amount):
                element = stacks.get(start).get()
                stacks.get(end).put(element)

        return ''.join([stacks.get(i).get() for i in range(1, len(stack_indexes) + 1)])

    def part_b(self):

        lines = self.get_lines_as_list()
        stack_line_index, stacks, stack_indexes = get_stacks(lines)
        moves = lines[stack_line_index + 2:]
        for move in moves:
            amount, start, end = get_move_from_line(move)
            if amount == 1:
                stacks.get(end).put(stacks.get(start).get())
            else:
                elements = [stacks.get(start).get() for _ in range(amount)]

                for k in range(len(elements) - 1, -1, -1):
                    stacks.get(end).put(elements[k])

        return ''.join([stacks.get(i).get() for i in range(1, len(stack_indexes) + 1)])
