from string import ascii_lowercase as asc_l
from string import ascii_uppercase as asc_u

priorities = {letter: value for letter, value in zip(asc_l + asc_u, range(1, 53))}


def first_elem_intersection(str1: str, str2: str):
    return list(set(c for c in str1).intersection(c for c in str2))[0]


def first_elem_intersection_2(str1: str, str2: str, str3: str):
    l = set.intersection(set(c for c in str1),
                         set(c for c in str2),
                         set(c for c in str3))
    return '' if len(l) == 0 else list(l)[0]


def day3_1():
    res = 0
    with open('day3_input.txt', 'r') as file:
        for line in file.readlines():
            res += priorities[first_elem_intersection(line[0:len(line) // 2],
                                                      line[len(line) // 2:].replace('\n', ''))]

    return res


def day3_2():
    res = 0
    with open('day3_input.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if (i + 1) % 3 == 0:
                c = first_elem_intersection_2(
                    lines[i - 2].replace('\n', ''),
                    lines[i - 1].replace('\n', ''),
                    lines[i].replace('\n', '')
                )
                if priorities.__contains__(c):
                    res += priorities[c]

    return res


if __name__ == '__main__':
    print(day3_2())
