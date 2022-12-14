from days.day import Day

import numpy as np


def create_matrix(lines: list[str]):
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
    y_min = 0
    y_max = max(rocks, key=lambda tup: tup[1])[1]

    matrix: np.ndarray = np.array([[0 for _ in range((x_max - x_min) + 1)] for _ in range((y_max - y_min) + 1)])
    for point in rocks:
        matrix[point[1] - y_min, point[0] - x_min] = 1
    # Starting point for sand (500,0) is equal to 5
    start = (0, 500 - x_min)
    matrix[0, 500 - x_min] = 5

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


def add_sand(matrix: np.ndarray, start: tuple[int, int]):
    current_sand = start
    x = current_sand[1]
    settled_before = False
    sand_rock = {1, 6}
    for y in range(start[0] + 1, matrix.shape[0]):
        next_possible = matrix[y, x]
        # Rock or sand underneath
        if next_possible in sand_rock:
            # Look diagonally down left
            diag_left = matrix[y, x - 1]
            if x - 1 < 0 or diag_left in sand_rock:
                if diag_left < 0:
                    # Falls over on the left side
                    settled_before = True
                    break
                # Look diagonally down right
                diag_right = matrix[y, x + 1]
                if x + 1 >= matrix.shape[1] or diag_right in sand_rock:
                    if x + 1 >= matrix.shape[1]:
                        # Falls over on the right side
                        settled_before = True
                        break
                    # if settled before
                    if matrix[y - 1, x] in {5, 6}:
                        settled_before = True
                        break
                    else:
                        # Sand settles
                        matrix[y - 1, x] = 6
                        break
                else:
                    x += 1
            else:
                x -= 1

    return settled_before


class Day14(Day):

    def __init__(self):
        super().__init__(14)

    def part_a(self):
        matrix = create_matrix(self.get_lines_as_list())
        # print_matrix(matrix[0])
        i = 1
        while not add_sand(matrix[0], matrix[1]):
            if i % 100_000 == 0:
                print(f'i = {i}')
                print_matrix(matrix[0])
                print()
            i += 1
        return np.count_nonzero(matrix[0] == 6)

    def part_b(self):
        return ''
