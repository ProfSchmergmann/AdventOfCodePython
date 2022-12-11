from days.day import Day
import operator

ops = {'+': operator.add, '*': operator.mul}


class Monkey:
    def __init__(self,
                 num: str,
                 starting_items_str: str,
                 operation: str,
                 test: str,
                 if_true: str,
                 if_false: str):
        self.num = int(num.strip().split(' ')[1].replace(':', ''))

        starting_items = []
        for item in starting_items_str.split(':')[1].strip().split(','):
            starting_items.append(int(item))
        self.items = starting_items

        right_operation_side = operation.split('=')[1].split('old')[1].strip()
        op = right_operation_side.split(' ')[0]
        self.operation = lambda x: ops[op](x, x if len(right_operation_side.split(' ')) == 1 else int(
            right_operation_side.split(' ')[1]))

        self.divisor = int(test.split('by')[1].strip())
        self.test = lambda x: x % self.divisor == 0

        self.monkey_if_true = int(if_true.split('monkey')[1].strip())
        self.monkey_if_false = int(if_false.split('monkey')[1].strip())
        self.items_inspected = 0

    def add_item(self, item: int):
        self.items.append(item)

    def inspect_items(self, part: str, divisor: int = 0) -> list[tuple[int, int]]:
        items = self.items.copy()
        inspection_list: list[tuple[int, int]] = []
        for item in self.items:
            if part == 'a':
                worry_level = self.operation(item) // 3
            else:
                worry_level = self.operation(item) % divisor
            test = self.test(worry_level)
            if test:
                inspection_list.append((self.monkey_if_true, worry_level))
            else:
                inspection_list.append((self.monkey_if_false, worry_level))
            items.remove(item)
            self.items_inspected += 1
        self.items = items
        return inspection_list


def read_monkeys_as_list(lines: list[str]):
    monkeys = []
    i = 0
    while i < len(lines):
        num = lines[i].strip()
        starting_items = lines[i + 1].strip()
        op = lines[i + 2].strip()
        test = lines[i + 3].strip()
        if_true = lines[i + 4].strip()
        if_false = lines[i + 5].strip()
        monkeys.append(Monkey(num, starting_items, op, test, if_true, if_false))
        i += 7
    return monkeys


class Day11(Day):
    def __init__(self):
        super().__init__(11)

    def part_a(self):
        monkeys = read_monkeys_as_list(self.get_lines_as_list())
        for i in range(20):
            for monkey in monkeys:
                for inspection in monkey.inspect_items('a'):
                    for monkey_to_throw_to in monkeys:
                        if monkey_to_throw_to.num == inspection[0]:
                            monkey_to_throw_to.add_item(inspection[1])
        #     print(f'Items after round {i}:')
        #     for monkey in monkeys:
        #         print(f'Monkey {monkey.num}: {monkey.items}')
        #     print()
        # for monkey in monkeys:
        #     print(f'Monkey {monkey.num} inspected items : {monkey.items_inspected} times.')
        inspected_items_list = [monkey.items_inspected for monkey in monkeys]
        inspected_items_list.sort()
        return inspected_items_list[-1] * inspected_items_list[-2]

    def part_b(self):
        monkeys = read_monkeys_as_list(self.get_lines_as_list())
        mod = 1
        for monkey in monkeys:
            mod *= monkey.divisor

        for i in range(1, 10_001):
            for monkey in monkeys:
                for inspection in monkey.inspect_items('b', mod):
                    for monkey_to_throw_to in monkeys:
                        if monkey_to_throw_to.num == inspection[0]:
                            monkey_to_throw_to.add_item(inspection[1])
            # if i % 1000 == 0 or i == 20:
            #     print(f'== After round {i} ==')
            #     for monkey in monkeys:
            #         print(f'Monkey {monkey.num} inspected items : {monkey.items_inspected} times.')
        inspected_items_list = [monkey.items_inspected for monkey in monkeys]
        inspected_items_list.sort()
        return inspected_items_list[-1] * inspected_items_list[-2]
