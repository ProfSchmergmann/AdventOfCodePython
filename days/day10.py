from numpy import sign

from days.day import Day


class Day10(Day):

    def __init__(self):
        super().__init__(10)

    def part_a(self):
        X = 1
        cycle = 0
        cycles_to_check = [20 + (40 * i) for i in range(6)]
        signal_strength = 0
        for line in self.get_lines_as_list():
            if len(line.split()) == 2:
                instruction, V = line.split()
                V = int(V)
            else:
                cycle += 1
                if cycle in cycles_to_check:
                    signal_strength += (cycle * X)
                continue
            for i in range(2):
                cycle += 1
                if i == 1:
                    if cycle in cycles_to_check:
                        signal_strength += (cycle * X)
                    X += V
                else:
                    if cycle in cycles_to_check:
                        signal_strength += (cycle * X)
        return signal_strength

    def part_b(self):
        X = 1
        V_list = []
        for line in self.get_lines_as_list():
            if len(line.split()) == 1:
                V_list.append(X)
            else:
                V = int(line.split()[1])
                V_list.append(X)
                V_list.append(X)
                X += V
        for row in range(0, len(V_list), 40):
            for col in range(40):
                print(end='##' if abs(V_list[row + col] - col) <= 1 else '..')
            print()
        return ''
