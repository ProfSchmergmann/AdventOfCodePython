def day4_1():
    with open('res/day4_input.txt', 'r') as file:
        res = 0
        for line in file.readlines():
            first_pair = line.split(',')[0]
            second_pair = line.split(',')[1].replace('\n', '')
            first_pair_start = first_pair.split('-')[0]
            first_pair_end = first_pair.split('-')[1]
            second_pair_start = second_pair.split('-')[0]
            second_pair_end = second_pair.split('-')[1]
            if ((second_pair_start <= first_pair_start <= first_pair_end <= second_pair_end) or
                    (first_pair_start <= second_pair_start <= second_pair_end <= first_pair_end)):
                res += 1
        return res
