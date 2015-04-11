#!/usr/bin/python

import sys

PREFIX = __file__
if PREFIX.endswith('.py'):
    PREFIX = PREFIX[0:-3]

def get_file(argv):
    if len(argv) == 1:
        return "%s_sample.in" % PREFIX
    else:
        return "%s_%s.in" % (PREFIX, argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "%s_sample.out" % PREFIX
    else:
        return "%s_%s.out" % (PREFIX, argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n") 

def min_steps(diners, steps, current_min):
    # print ''.join([' ']*steps), steps, diners, current_min
    left = sum(diners)
    if current_min is not None and steps >= current_min:
        return current_min
    if left == 0:
        return steps

    diners_with_special = [diner for diner in diners if diner > 0]
    max_index = 0
    max_pancakes = 0
    for i in xrange(0, len(diners_with_special)):
        if max_pancakes < diners_with_special[i]:
            max_pancakes = diners_with_special[i]
            max_index = i
    if max_pancakes == 1:
        return steps + 1
    diners_with_special[max_index] = diners_with_special[max_index]/2
    diners_with_special.append(max_pancakes - diners_with_special[max_index])
    steps_with_special = min_steps(diners_with_special, steps+1, current_min)
    if current_min is None:
        current_min = steps_with_special
    else:
        current_min = min(steps_with_special, current_min)

    diners_without_special = [diner-1 for diner in diners if diner > 0]
    steps_without_special = min_steps(diners_without_special, steps+1, current_min)
    return min(steps_with_special, steps_without_special)

def main(argv):
    with open(get_file(argv), 'r') as f, open(get_file_out(argv), 'w') as f_out:
        T = int(f.readline())
        for t in xrange(1, T+1):
            N = int(f.readline())
            initial = [int(x) for x in f.readline().split(' ')]
            current_pancakes = sum(initial)
            print_answer(t, "%d" % min_steps(initial, 0, None), f_out)

if __name__ == "__main__":
    main(sys.argv)
