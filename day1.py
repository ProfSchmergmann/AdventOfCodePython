from itertools import groupby
import numpy as np
from aocd import data


def day1_1():
    list = []

    with open('day1_input.txt', 'r') as f_data:
        tmp = 0
        for line in f_data.readlines():
            if line.strip():
                tmp += int(line)
            else:
                list.append(tmp)
                tmp = 0

    print(np.max(list))


def day1_2():
    list = []

    with open('day1_input.txt', 'r') as f_data:
        tmp = 0
        for line in f_data.readlines():
            if line.strip():
                tmp += int(line)
            else:
                list.append(tmp)
                tmp = 0

    sorted = np.sort(list)
    print(sorted[-1])
    print(sorted[-1] + sorted[-2] + sorted[-3])


if __name__ == '__main__':
    print(data)
