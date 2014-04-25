#!/usr/bin/python

import sys

def get_file(argv):
    if len(argv) == 1:
        return "a.in"
    else:
        return "a_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "a.out"
    else:
        return "a_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def arithmetic_sum(a, d, n):
    return (n*(2*a + (n-1)*d))/2

def all_rings(r, N):
    if N == 0:
        return 0
    return 2*N*r + arithmetic_sum(1, 4, N)

def search(r, target):
    low, high, increase = 0, 1, True
    while low < high:
        test = all_rings(r, high)
        if test < target:
            high = high * 2
        elif test == target:
            return high
        else:
            test = all_rings(r, low)
            if test < target:
                low = low + ((high-low+1)/2)
            elif test == target:
                return low
            else:
                high = low
                low = low / 2
    return low - 1


def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        r, t = [int(d) for d in (f.readline().split(' '))]
        print_answer(case, search(r, t), f_out)


if __name__ == "__main__":
    main(sys.argv)