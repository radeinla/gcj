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
    if steps >= current_min:
        return current_min
    if left == 0:
        return steps

    current_diners = [diner for diner in diners if diner > 0]
    max_index = 0
    max_pancakes = 0
    for i in xrange(0, len(current_diners)):
        if max_pancakes < current_diners[i]:
            max_pancakes = current_diners[i]
            max_index = i
    if max_pancakes == 1:
        return steps + 1
    for to_transfer in xrange(1, ((max_pancakes+1)/2)+1):
        diners_with_special = current_diners[:]
        diners_with_special[max_index] = current_diners[max_index] - to_transfer
        diners_with_special.append(to_transfer)
        steps_with_special = min_steps(diners_with_special, steps+1, current_min)
        current_min = min(steps_with_special, current_min)

    diners_without_special = [diner-1 for diner in diners if diner > 0]
    return min_steps(diners_without_special, steps+1, current_min)

def main(argv):
    with open(get_file(argv), 'r') as f, open(get_file_out(argv), 'w') as f_out:
        T = int(f.readline())
        for t in xrange(1, T+1):
            N = int(f.readline())
            initial = [int(x) for x in f.readline().split(' ')]
            current_pancakes = max(initial)
            print_answer(t, "%d" % min_steps(initial, 0, current_pancakes), f_out)

if __name__ == "__main__":
    main(sys.argv)
