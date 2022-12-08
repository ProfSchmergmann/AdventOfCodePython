import numpy as np

from days.day import Day


def read_trees(lines: list[str]):
    return np.matrix([[int(i) for i in lines[j].replace('\n', '').strip()] for j in range(len(lines))])


def print_seen_trees(trees, seen):
    for row in range(trees.shape[0]):
        line = ''
        for col in range(trees.shape[1]):
            if seen[row, col]:
                line += f'|{trees[row, col]}|'
            else:
                line += f' {trees[row, col]} '
        print(line)
    print(seen.sum())


class Day8(Day):
    def __init__(self, ):
        super().__init__(8)

    def part_a(self):
        trees = read_trees(self.get_lines_as_list())
        num_cols = trees.shape[0]
        num_rows = trees.shape[1]
        seen = np.matrix([[True for _ in range(num_rows)] for _ in range(num_cols)])

        for row in range(num_rows):
            for col in range(num_cols):
                if row == num_rows - 1 or row == 0 or col == num_cols - 1 or col == 0:
                    seen[row, col] = True
                    continue
                tree_height = trees[row, col]

                # Watch to top
                top = True
                for row2 in range(row - 1, -1, -1):
                    if tree_height <= trees[row2, col]:
                        top = False
                        break
                # Watch to bottom
                bottom = True
                for row2 in range(row + 1, num_rows):
                    if tree_height <= trees[row2, col]:
                        bottom = False
                        break
                # Watch to right
                right = True
                for col2 in range(col + 1, num_cols):
                    if tree_height <= trees[row, col2]:
                        right = False
                        break
                # Watch to left
                left = True
                for col2 in range(col - 1, -1, -1):
                    if tree_height <= trees[row, col2]:
                        left = False
                        break
                seen[row, col] = top or bottom or left or right
        return seen.sum()

    def part_b(self):
        trees = read_trees(self.get_lines_as_list())
        num_cols = trees.shape[0]
        num_rows = trees.shape[1]
        scenic_score = 0
        for row in range(num_rows):
            for col in range(num_cols):
                current = trees[row, col]
                top = bottom = left = right = 0
                for x in range(col - 1, -1, -1):
                    left += 1
                    if trees[row, x] >= current:
                        break
                for x in range(col + 1, num_cols):
                    right += 1
                    if trees[row, x] >= current:
                        break
                for x in range(row - 1, -1, -1):
                    bottom += 1
                    if trees[x, col] >= current:
                        break
                for x in range(row + 1, num_rows):
                    top += 1
                    if trees[x, col] >= current:
                        break
                scenic_score = max(scenic_score, top * bottom * left * right)
        return scenic_score
