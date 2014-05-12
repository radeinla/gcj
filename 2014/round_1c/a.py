#!/usr/bin/python

import sys
import inspect
from fractions import gcd

problem = inspect.getmodulename(__file__)

def get_file(argv):
    if len(argv) == 1:
        return "%s.in" % problem
    else:
        return "%s_%s.in" % (problem, argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "%s.out" % problem
    else:
        return "%s_%s.out" % (problem, argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

cache = {}

def min_gens(P, Q, d, mx):
    g = gcd(P, Q)
    P = P/g
    Q = Q/g
    if d > mx:
        ans = None
    elif 2 * P == Q:
        ans = d
    elif 2 * P > Q:
        if 2 * P > 2 * Q:
            ans = None
        else:
            if min_gens(2*P-Q, Q, d+1, 40):
                ans = d
            else:
                ans = None
    else:
        ans = min_gens(P * 2, Q, d+1, 40)
    return ans

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        P, Q = [int(x) for x in f.readline().strip().split('/')]
        ans = min_gens(P, Q, 1, 40)
        if ans:
            print_answer(case, ans, f_out)
        else:
            print_answer(case, 'impossible', f_out)

if __name__ == "__main__":
    main(sys.argv)