from days.day1 import Day1
from days.day10 import Day10
from days.day11 import Day11
from days.day12 import Day12
from days.day13 import Day13
from days.day14 import Day14
from days.day15 import Day15
from days.day2 import Day2
from days.day3 import Day3
from days.day4 import Day4
from days.day5 import Day5
from days.day6 import Day6
from days.day7 import Day7
from days.day8 import Day8
from days.day9 import Day9

if __name__ == '__main__':
    day = Day15()
    day.print_part_a_and_b_with_time()
    day_list = [Day1(),
                Day2(),
                Day3(),
                Day4(),
                Day5(),
                Day6(),
                Day7(),
                Day8(),
                Day9(),
                Day10(),
                Day11(),
                Day12(),
                Day13(),
                Day14(),
                Day15()]
    # for day in day_list:
    #   day.print_part_a_and_b_with_time()
