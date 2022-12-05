from collections import deque


def day5_1():
    with open('res/day5_input.txt') as file:
        lines = file.readlines()
        stacks = list([deque[str]])
        moves = False
        i = 0
        for i in range(len(lines)):
            stack_num = 1
            j = 0
            if not moves:
                for j in range(len(lines[i])):
                    if lines[i][j] == ' ' and lines[i][j + 1] != '1' and not moves:
                        j += 4
                        stack_num += 1
                        try:
                            stacks[stack_num - 1].append(char)
                        except IndexError:
                            stacks.append(deque())
                    elif lines[i][j+1] != '1' and not moves:
                        char = lines[i][j + 1]
                        try:
                            stacks[stack_num - 1].append(char)
                        except IndexError:
                            stacks.append(deque)
                            stacks[stack_num - 1].append(char)
                        j += 4
                    else:
                        moves = True
                        break
            else:
                for j in range(len(lines[i])):
                    move = lines[i].replace('move', '').replace('from', '').replace('to', '').split('  ')
                    amount = int(move[0])
                    start = int(move[1])
                    end = int(move[2])
                    for k in range(amount):
                        element = stacks[start - 1].popleft()
                        stacks[end - 1].appendleft(element)
        i += 1
        return ''.join(stacks[i].popleft() for i in range(len(stacks)))
