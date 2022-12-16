from days.day import Day


def manhattan(point_1: tuple[int, int], point_2: tuple[int, int]):
    return abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1])


def read_map(lines: list[str]):
    sensors_beacons = {}
    for line in lines:
        splitted_line = line.strip().split(':')
        sensor_x = int(splitted_line[0].split(',')[0].split('x=')[1])
        sensor_y = int(splitted_line[0].split(',')[1].split('y=')[1])
        beacon_x = int(splitted_line[1].split(',')[0].split('x=')[1])
        beacon_y = int(splitted_line[1].split(',')[1].split('y=')[1])
        sensors_beacons.update({(sensor_x, sensor_y): (beacon_x, beacon_y)})

    return sensors_beacons


class Day15(Day):

    def __init__(self):
        super().__init__(15)

    def part_a(self):
        sensors_beacons = read_map(self.get_lines_as_list())

        impossible_positions = set()
        row_to_search = 10
        for sensor, beacon in sensors_beacons.items():
            dist = manhattan(sensor, beacon)
            if row_to_search < sensor[1]:
                # row to search is above sensor
                if row_to_search >= sensor[1] - dist:
                    # row is in distance
                    dist_to_row = abs(sensor[1] - row_to_search)
                    for x in range(sensor[0] - abs(dist_to_row - dist), sensor[0] + abs(dist_to_row - dist) + 1):
                        if not (x == beacon[0] and row_to_search == beacon[1]):
                            impossible_positions.update({x})
            elif row_to_search > sensor[1]:
                # row to search is below sensor
                if row_to_search <= sensor[1] + dist:
                    # row is in distance
                    dist_to_row = abs(sensor[1] - row_to_search)
                    for x in range(sensor[0] - abs(dist_to_row - dist), sensor[0] + abs(dist_to_row - dist) + 1):
                        if not (x == beacon[0] and row_to_search == beacon[1]):
                            impossible_positions.update({x})
            else:
                for x in range(sensor[0] - dist, sensor[0] + dist):
                    if x != beacon[0]:
                        impossible_positions.update({x})
        return len(impossible_positions)

    def part_b(self):
        return ''
