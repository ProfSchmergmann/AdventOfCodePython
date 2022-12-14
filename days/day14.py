from days.day import Day

import numpy as np


def create_matrix(lines: list[str], floor: bool = False):
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
                    for x in range(x1, x2, -1):
                        rocks.add((x, y1))
                else:
                    if y1 < y2:
                        for y in range(y1, y2):
                            rocks.add((x1, y))
                    elif y1 > y2:
                        for y in range(y1, y2, -1):
                            rocks.add((x1, y))
                prev_point = point
            rocks.add(point)

    x_min = min(rocks, key=lambda tup: tup[0])[0]
    x_max = max(rocks, key=lambda tup: tup[0])[0]
    length_x = x_max - x_min
    length_x = length_x if not floor else 9 * length_x
    y_min = 0
    y_max = max(rocks, key=lambda tup: tup[1])[1]
    y_max = y_max if not floor else y_max + 2
    length_y = y_max - y_min

    matrix: np.ndarray = np.array([[0 for _ in range(length_x + 1)] for _ in range(length_y + 1)])

    for point in rocks:
        if floor:
            matrix[point[1] - y_min, (point[0] - x_min) + length_x // 3] = 1
        else:
            matrix[point[1] - y_min, point[0] - x_min] = 1

    if floor:
        start = (0, (500 - x_min) + length_x // 3)
        # Add floor
        for x in range(0, matrix.shape[1]):
            matrix[y_max, x] = 1
    else:
        # Starting point for sand (500,0) is equal to 5
        start = (0, 500 - x_min)

    matrix[start[0], start[1]] = 5

    return matrix, start


def print_matrix(matrix: np.ndarray):
    for x in matrix:
        for y in x:
            s = ''
            if y == 5:
                s = '+'
            elif y == 1:
                s = '#'
            elif y == 0:
                s = '.'
            elif y == 6:
                s = 'o'
            print(end=s)
        print()


def add_sand(matrix: np.ndarray, start: tuple[int, int], part2: bool = False):
    current_sand = start
    x = current_sand[1]
    sand_rock_start = {1, 5, 6}

    if not part2:
        for y in range(start[0] + 1, matrix.shape[0]):
            next_possible = matrix[y, x]
            # Rock or sand underneath
            if next_possible in sand_rock_start:
                # Look diagonally down left
                if x - 1 < 0:
                    # Falls over on the left side
                    return True
                if matrix[y, x - 1] in sand_rock_start:
                    # Look diagonally down right
                    if x + 1 >= matrix.shape[1]:
                        # Falls over on the right side
                        return True
                    if matrix[y, x + 1] in sand_rock_start:
                        # Sand settles
                        matrix[y - 1, x] = 6
                        return False
                    else:
                        x += 1
                else:
                    x -= 1
        return True

    else:
        for y in range(start[0] + 1, matrix.shape[0]):
            next_possible = matrix[y, x]
            # Rock or sand underneath
            if next_possible in sand_rock_start:
                # Look diagonally down left
                if matrix[y, x - 1] in sand_rock_start:
                    # Look diagonally down right
                    if matrix[y, x + 1] in sand_rock_start:
                        # Sand settles
                        if matrix[y - 1, x] == 5:
                            matrix[y - 1, x] = 6
                            return True
                        matrix[y - 1, x] = 6
                        return False
                    else:
                        x += 1
                else:
                    x -= 1
        return True


class Day14(Day):

    def __init__(self):
        super().__init__(14)

    def part_a(self):
        matrix = create_matrix(self.get_lines_as_list())
        i = 0
        while not add_sand(matrix[0], matrix[1]):
            i += 1
        return i

    def part_b(self):
        matrix = create_matrix(self.get_lines_as_list(), True)
        i = 1
        while not add_sand(matrix[0], matrix[1], True):
            i += 1
        return i
