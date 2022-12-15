from days.day import Day


def manhattan(point_1: tuple[int, int], point_2: tuple[int, int]):
    return abs(point_2[0] - point_1[0]) + abs(point_2[1] - point_1[1])


def process_input(lines: list[str]):
    sensors_beacons = {}
    for line in lines:
        splitted_line = line.strip().split(':')
        sensor_x = int(splitted_line[0].split(',')[0].split('x=')[1])
        sensor_y = int(splitted_line[0].split(',')[1].split('y=')[1])
        beacon_x = int(splitted_line[1].split(',')[0].split('x=')[1])
        beacon_y = int(splitted_line[1].split(',')[1].split('y=')[1])
        sensors_beacons.update({(sensor_x, sensor_y): (beacon_x, beacon_y)})

    impossible_positions = set()
    for sensor, beacon in sensors_beacons.items():
        dist = manhattan(sensor, beacon)
        for x in range(dist + 1):
            for y in range(dist + 1):
                if abs(x + y) <= dist:
                    impossible_positions.update({(sensor[0] + x, sensor[1] + y)})
                    impossible_positions.update({(sensor[0] - x, sensor[1] - y)})
                    impossible_positions.update({(sensor[0] - x, sensor[1] + y)})
                    impossible_positions.update({(sensor[0] + x, sensor[1] - y)})
    for sensor, beacon in sensors_beacons.items():
        if impossible_positions.__contains__(beacon):
            impossible_positions.remove(beacon)
    return sensors_beacons, impossible_positions


class Day15(Day):

    def __init__(self):
        super().__init__(15)

    def part_a(self):
        impossible_positions = process_input(self.get_lines_as_list())[1]
        res = 0
        for pos in impossible_positions:
            if pos[1] == 2_000_000:
                res += 1
        return res

    def part_b(self):
        return ''
