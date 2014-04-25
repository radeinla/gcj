#!/usr/bin/python

import sys

def get_file(argv):
    if len(argv) == 1:
        return "b.in"
    else:
        return "b_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "b.out"
    else:
        return "b_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def loop_optimized(C, F, X):
    c, r, t = float(0), float(2), float(0)
    while c < X:
        no_farm_cost = (X-c)/r
        next_farm_cost = (C-c)/r
        if no_farm_cost < next_farm_cost + X/(r+F):
            c = X
            t += no_farm_cost
        else:
            c = 0
            r += F
            t += next_farm_cost
    return t

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        arr = f.readline().split(" ")
        C = float(arr[0])
        F = float(arr[1])
        X = float(arr[2])
        print_answer(t, "%.7f" % loop_optimized(C, F, X), f_out)

if __name__ == "__main__":
    main(sys.argv)