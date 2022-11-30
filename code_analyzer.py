"""if __name__ == '__main__'"""
import re
from os import listdir
from sys import argv

# write your code here

blank_count = 0

args = argv
og_tasks = args[1]
k = og_tasks
tasks = []

if re.search(r"[^(.py)]\Z", og_tasks):
    og_tasks = listdir(og_tasks)
    og_tasks.sort()
    for i in og_tasks:
        if re.search(r"test_", i):
            tasks.append(k+'/'+i)
else:
    tasks = og_tasks

if type(tasks) != list:
    tasks = [tasks]


def first_test(line):
    # checks if a line is too long
    if len(line) > 79:
        print(f'{task}: Line {count}: S001 Too long')


def second_test(line):
    # checks if indentation has less than four spaces
    four_space_regex = r"\A(( {4})*[^ ])"

    if re.match(four_space_regex, line):
        pass
    else:
        print(f'{task}: Line {count}: S002 Indentation is not a multiple of four')


def third_test(line):
    # checks if there is a ; and that it is not in # or ''
    # \A(?:(?!#).)* this line of code is responsible for making sure that # is not before (;( ? ?# .*)?\n?)\Z at any instance
    reg = r"\A(?:(?!#).)*(;( ? ?# .*)?\n?)\Z"

    if re.match(reg, line):
        print(f'{task}: Line {count}: S003 Unnecessary semicolon after a statement')


def fourth_test(line):
    # checks if an inline comment has less than two spaces
    reg = r"\A(?:(?!  #).)*(\S ?#)"

    if re.search(reg, line):
        print(f'{task}: Line {count}: S004 Less than two spaces before inline comments')


def fifth_test(line):
    # checks if there is a T_odo at any point in the code
    reg = r"# [Tt][Oo][Dd][Oo]"

    if re.search(reg, line):
        print(f'{task}: Line {count}: S005 TODO found')


def sixth_test(line, cnt):
    # checks if there are more than two blank lines before this line of code
    if not line.split():
        cnt += 1
    elif cnt > 2:
        print(f'{task}: Line {count}: S006 More than two blank lines used before this line')
        cnt = 0
    else:
        cnt = 0
    return cnt


def seventh_test(line):
    # checks if there are more than one spaces when declaring a func or creating class
    reg = r"(def {2,})|(class {2,})"
    if re.search(reg, line):
        print(f"{task}: Line {count}: S007 Too many spaces after 'class'")


def eighth_test(line):
    # checks that class name is in camelcase
    reg = r"class [^A-Z]+\Z"
    if re.search(reg, line):
        print(f"{task}: Line {count}: S008 Class name '{line.split('class ')[-1].split(':')[0]}' should use CamelCase")


def ninth_test(line):
    # check that func name is in snake_case
    reg = r"def [^a-z_][A-Za-z1-9]+\(\S*\):\n\Z"
    if re.search(reg, line):
        printed_value = line.split('def ')[-1].split('():\n')[0]
        print(f"{task}: Line {count}: S009 Function name '{printed_value}' should use snake_case")


def tenth_test(line):
    reg_main = r"\([a-z,\d =]*\):"
    reg_func = r"def "
    if re.search(reg_func, line) and not re.search(reg_main, line):
        line = line.split("(")[-1]
        line = line.strip('):').split(', ')
        for p in line:
            arg = p.split("=")[0]
            if not re.search(r"\A[a-z_]+\Z", arg):
                print(f"{task}: Line {count}: S010 Argument {arg} should be written in snake_case")


def eleventh_test(line):
    reg_m = r"\A *[a-z1-9_.]+ = "
    reg_h = r" = "
    if not re.search(reg_m, line) and re.search(reg_h, line):
        variable = line.split(" = ")[0]
        print(f"{task}: Line {count}: S011 Variable {variable} should be written in snake_case")


def twelfth_test(line):
    # checks if a name of a default variable in a func is mutable
    reg = r"def \S+\(.*\S+=\[\]\):"
    if re.search(reg, line):
        print(f"{task}: Line {count}: S012 The default argument value is mutable.")


for task in tasks:
    with open(task, 'r') as file:
        count = 0
        for i in file:
            count += 1
            first_test(i)
            second_test(i)
            third_test(i)
            fourth_test(i)
            fifth_test(i)
            blank_count = sixth_test(i, blank_count)
            seventh_test(i)
            eighth_test(i)
            ninth_test(i)
            tenth_test(i)
            eleventh_test(i)
            twelfth_test(i)

# log.close()
