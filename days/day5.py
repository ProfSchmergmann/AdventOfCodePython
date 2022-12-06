from queue import LifoQueue


def day5_1():
    with open('res/day5_input.txt', 'r') as file:
        lines = file.readlines()

        for i in range(len(lines)):
            if lines[i].replace('\n', '') == '':
                stack_line = lines[i - 1].replace('\n', '')
                stack_line_index = i - 1
                break
            i += 1

        stack_indexes = []
        for i in range(len(stack_line)):
            if stack_line[i] != ' ':
                stack_indexes.append(i)
            i += 1

        stacks = {}
        for i in range(len(stack_indexes)):
            stacks.update({i + 1: LifoQueue()})

        for i in range(stack_line_index - 1, -1, -1):
            line = lines[i].replace('\n', '')
            for j in range(len(line)):
                if str.isalpha(line[j]):
                    stacks.get(stack_indexes.index(j) + 1).put(line[j])

        moves = lines[stack_line_index + 2:]
        for move in moves:
            m = move.replace('move', '').replace('from', '').replace('to', '').replace('\n', '').split('  ')
            amount = int(m[0])
            start = int(m[1])
            end = int(m[2])
            for k in range(amount):
                element = stacks.get(start).get()
                stacks.get(end).put(element)

        return ''.join([stacks.get(i).get() for i in range(1, len(stack_indexes) + 1)])


def day5_2():
    with open('res/day5_input.txt', 'r') as file:
        lines = file.readlines()

        for i in range(len(lines)):
            if lines[i].replace('\n', '') == '':
                stack_line = lines[i - 1].replace('\n', '')
                stack_line_index = i - 1
                break
            i += 1

        stack_indexes = []
        for i in range(len(stack_line)):
            if stack_line[i] != ' ':
                stack_indexes.append(i)
            i += 1

        stacks = {}
        for i in range(len(stack_indexes)):
            stacks.update({i + 1: LifoQueue()})

        for i in range(stack_line_index - 1, -1, -1):
            line = lines[i].replace('\n', '')
            for j in range(len(line)):
                if str.isalpha(line[j]):
                    stacks.get(stack_indexes.index(j) + 1).put(line[j])

        moves = lines[stack_line_index + 2:]
        for move in moves:
            m = move.replace('move', '').replace('from', '').replace('to', '').replace('\n', '').split('  ')
            amount = int(m[0])
            start = int(m[1])
            end = int(m[2])
            if amount == 1:
                stacks.get(end).put(stacks.get(start).get())
            else:
                elements = [stacks.get(start).get() for _ in range(amount)]

                for k in range(len(elements)-1, -1, -1):
                    stacks.get(end).put(elements[k])

        return ''.join([stacks.get(i).get() for i in range(1, len(stack_indexes) + 1)])
