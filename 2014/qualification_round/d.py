#!/usr/bin/python

import sys

def get_file(argv):
    if len(argv) == 1:
        return "d.in"
    else:
        return "d_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "d.out"
    else:
        return "d_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def deceit(N, naomi, ken):
    return None

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        N = int(f.readline())
        naomi = [float(x) for x in f.readline().split(" ")]
        ken = [float(x) for x in f.readline().split(" ")]
        print_answer(t, deceit(N, naomi, ken), f_out)

if __name__ == "__main__":
    main(sys.argv)