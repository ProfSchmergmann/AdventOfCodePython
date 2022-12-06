from days.day import Day


def calculate_score(chosen_values):
    res = 0
    for i in range(len(chosen_values)):
        played_value = chosen_values[i]
        # Rock
        if played_value[1] == "X":
            res += 1
            # Scissors
            if played_value[0] == "C":
                res += 6
            # Rock
            elif played_value[0] == "A":
                res += 3
        # Paper
        elif played_value[1] == "Y":
            res += 2
            # Rock
            if played_value[0] == "A":
                res += 6
            # Paper
            elif played_value[0] == "B":
                res += 3
        # Scissors
        elif played_value[1] == "Z":
            res += 3
            # Paper
            if played_value[0] == "B":
                res += 6
            # Scissors
            elif played_value[0] == "C":
                res += 3

    return res


class Day2(Day):
    def __init__(self):
        super().__init__(2)

    def part_a(self):
        chosen_values = []
        for line in self.get_lines_as_list():
            chosen_values.append(line.strip().split(" "))

        return calculate_score(chosen_values)

    def part_b(self):
        chosen_values = []
        for line in self.get_lines_as_list():
            value = line.strip().split(" ")
            # Loose
            if value[1] == "X":
                # Rock
                if value[0] == "A":
                    chosen_values.append(["A", "Z"])
                # Paper
                elif value[0] == "B":
                    chosen_values.append(["B", "X"])
                # Scissors
                elif value[0] == "C":
                    chosen_values.append(["C", "Y"])
            # Draw
            elif value[1] == "Y":
                # Rock
                if value[0] == "A":
                    chosen_values.append(["A", "X"])
                # Paper
                elif value[0] == "B":
                    chosen_values.append(["B", "Y"])
                # Scissors
                elif value[0] == "C":
                    chosen_values.append(["C", "Z"])

            # Win
            elif value[1] == "Z":
                # Rock
                if value[0] == "A":
                    chosen_values.append(["A", "Y"])
                # Paper
                elif value[0] == "B":
                    chosen_values.append(["B", "Z"])
                # Scissors
                elif value[0] == "C":
                    chosen_values.append(["C", "X"])

        return calculate_score(chosen_values)
