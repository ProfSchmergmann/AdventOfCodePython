from days.day import Day


def read_heightmap(lines: list[str]) -> list[list[str]]:
    return [[letter for letter in line] for line in lines]


def create_graph(heightmap: list[list[str]]):
    graph = {}

    def check_neighbour(current_height, neighbour_height, row, col):
        if current_height + 1 == neighbour_height or current_height >= neighbour_height:
            neighbours.append((row, col))

    for row in range(len(heightmap)):
        for col in range(len(heightmap[row])):
            neighbours = []
            current_height = ord(heightmap[row][col])
            # top
            if row - 1 >= 0:
                neighbour_height = ord(heightmap[row - 1][col])
                check_neighbour(current_height, neighbour_height, row - 1, col)
            # bottom
            if row + 1 < len(heightmap):
                neighbour_height = ord(heightmap[row + 1][col])
                check_neighbour(current_height, neighbour_height, row + 1, col)
            # left
            if col - 1 >= 0:
                neighbour_height = ord(heightmap[row][col - 1])
                check_neighbour(current_height, neighbour_height, row, col - 1)
            # right
            if col + 1 < len(heightmap[row]):
                neighbour_height = ord(heightmap[row][col + 1])
                check_neighbour(current_height, neighbour_height, row, col + 1)
            graph.update({(row, col): neighbours})
    return graph


def bfs(graph, start, end):
    queue = [(start, [start])]
    visited = set()
    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)
        for node in graph[vertex]:
            if node == end:
                return path + [end]
            else:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + [node]))


def shortest_path(graph, start, end):
    path_list = [[start]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start}
    if start == end:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if end in next_nodes:
            current_path.append(end)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if next_node not in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


def print_path(path, heightmap):
    diagram = [['.' for _ in range(len(heightmap[0]))] for _ in range(len(heightmap))]
    i = 0
    while i < len(path) - 1:
        current_point = path[i]
        if heightmap[current_point[0]][current_point[1]] == 'E':
            diagram[current_point[0]][current_point[1]] = 'E'
            i += 1
            continue
        next_point = path[i + 1]
        if current_point[0] < next_point[0]:
            diagram[current_point[0]][current_point[1]] = 'v'
        elif current_point[0] > next_point[0]:
            diagram[current_point[0]][current_point[1]] = '^'
        elif current_point[1] < next_point[1]:
            diagram[current_point[0]][current_point[1]] = '>'
        elif current_point[1] > next_point[1]:
            diagram[current_point[0]][current_point[1]] = '<'
        i += 1
    for row in range(len(diagram)):
        for col in range(len(diagram[row])):
            print(end=diagram[row][col])
        print()


class Day12(Day):

    def __init__(self):
        super().__init__(12)

    def part_a(self):
        heightmap: list[list[str]] = read_heightmap(self.get_lines_as_list())
        start = (0, 0)
        stop = (0, 0)
        for row in range(len(heightmap)):
            for col in range(len(heightmap[row])):
                if heightmap[row][col] == 'S':
                    heightmap[row][col] = '`'
                    start = (row, col)
                    continue
                if heightmap[row][col] == 'E':
                    heightmap[row][col] = '{'
                    stop = (row, col)
                    continue
        graph = create_graph(heightmap)
        # path = bfs(graph, start, stop)
        path = shortest_path(graph, start, stop)
        # print_path(path, heightmap)
        return len(path) - 1

    def part_b(self):
        return ''
