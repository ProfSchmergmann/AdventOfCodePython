from days.day import Day


class Day9(Day):
    def __init__(self):
        super().__init__(9)

    def part_a(self):
        visited: set[tuple[int, int]] = {(0, 0)}
        H = T = [0, 0]
        for line in self.get_lines_as_list():
            x, y = line.split()
            y = int(y)

            for _ in range(y):
                dx = 1 if x == 'R' else -1 if x == 'L' else 0
                dy = 1 if x == 'U' else -1 if x == 'D' else 0

                H[0] += dx
                H[1] += dy

                _x = H[0] - T[0]
                _y = H[1] - T[1]

                if abs(_x) > 1 or abs(_y) > 1:
                    if _x == 0:
                        T[1] += _y // 2
                    elif _y == 0:
                        T[0] += _x // 2
                    else:
                        T[0] += 1 if _x > 0 else -1
                        T[1] += 1 if _y > 0 else -1

                visited.add(tuple(T))
        return len(visited)

    def part_b(self):
        visited: set[tuple[int, int]] = {(0, 0)}
        positions = [[0, 0] for _ in range(10)]

        for line in self.get_lines_as_list():
            x, y = line.split()
            y = int(y)

            for _ in range(y):
                dx = 1 if x == 'R' else -1 if x == 'L' else 0
                dy = 1 if x == 'U' else -1 if x == 'D' else 0

                positions[0][0] += dx
                positions[0][1] += dy

                for i in range(9):
                    H = positions[i]
                    T = positions[i + 1]
                    _x = H[0] - T[0]
                    _y = H[1] - T[1]

                    if abs(_x) > 1 or abs(_y) > 1:
                        if _x == 0:
                            T[1] += _y // 2
                        elif _y == 0:
                            T[0] += _x // 2
                        else:
                            T[0] += 1 if _x > 0 else -1
                            T[1] += 1 if _y > 0 else -1

                visited.add(tuple(positions[-1]))
        return len(visited)
