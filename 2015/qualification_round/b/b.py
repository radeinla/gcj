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
    if current_min is not None and steps >= current_min:
        return current_min
    current_diners = [diner for diner in diners if diner > 0]
    if not current_diners:
        return steps
    current_diners.append(0)
    # print ''.join([' ']*steps), steps, current_diners, current_min
    for transfer_from in xrange(0, len(current_diners)):
        for transfer_to in xrange(transfer_from+1, len(current_diners)):
            if transfer_from != transfer_to:
                for to_transfer in xrange(1, current_diners[transfer_from]+1):
                    special_diners = current_diners[:]
                    special_diners[transfer_from] = special_diners[transfer_from] - to_transfer
                    special_diners[transfer_to] = special_diners[transfer_to] + to_transfer
                    special_transfer = min_steps(special_diners, steps+1, current_min)
                    if current_min is None:
                        current_min = special_transfer
                    else:
                        current_min = min(current_min, special_transfer)
    let_them_eat = min_steps([diner-1 for diner in current_diners if diner>0], steps+1, current_min)
    if current_min is None:
        current_min = let_them_eat
    else:
        current_min = min(current_min, let_them_eat)
    return current_min


def main(argv):
    with open(get_file(argv), 'r') as f, open(get_file_out(argv), 'w') as f_out:
        T = int(f.readline())
        for t in xrange(1, T+1):
            N = int(f.readline())
            initial = [int(x) for x in f.readline().split(' ')]
            current_pancakes = sum(initial)
            print_answer(t, "%d" % min_steps(initial, 0, current_pancakes), f_out)

if __name__ == "__main__":
    main(sys.argv)
