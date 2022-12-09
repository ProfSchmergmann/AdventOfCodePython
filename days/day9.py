from days.day import Day
import numpy as np


def read_steps(filename: str):
    with open(filename, 'r') as file:
        res = []
        for line in file.readlines():
            move = line.split(' ')[0]
            amount = int(line.split(' ')[1].replace('\n', ''))
            res.append((move, amount))
    return res


class Day9(Day):
    def __init__(self):
        super().__init__(9)

    def part_a(self):
        steps: list[tuple[str, int]] = read_steps(self.filename)
        position_T = (0, 0)
        current_position_H = (0, 0)
        visited: set[tuple[int, int]] = {(0, 0)}
        for step in steps:
            for s in range(step[1]):
                x_H = current_position_H[0]
                y_H = current_position_H[1]
                position_H_plus_1 = current_position_H
                # Move H
                if step[0] == 'L':
                    position_H_plus_1 = (x_H - 1, y_H)
                elif step[0] == 'U':
                    position_H_plus_1 = (x_H, y_H + 1)
                elif step[0] == 'R':
                    position_H_plus_1 = (x_H + 1, y_H)
                elif step[0] == 'D':
                    position_H_plus_1 = (x_H, y_H - 1)
                x_H = position_H_plus_1[0]
                y_H = position_H_plus_1[1]
                x_T = position_T[0]
                y_T = position_T[1]
                # If x positions differ by more than 1:
                if bool(abs(x_H - x_T) > 1) ^ bool(abs(y_H - y_T) > 1):
                    # Move T to H:
                    position_T = current_position_H
                # If positions differ diagonally:
                elif (abs(x_H - x_T) + abs(y_H - y_T)) > 1:
                    if (abs(x_H - x_T) + abs(y_H - y_T)) > 2:
                        # Move T diagonally to H:
                        position_T = current_position_H
                current_position_H = position_H_plus_1
                visited.update({position_T})
        return len(visited)

    def part_b(self):
        return ''
