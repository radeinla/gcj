#!/usr/bin/python

import sys

def get_file(argv):
    if len(argv) == 1:
        return "c.in"
    else:
        return "c_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "c.out"
    else:
        return "c_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        print_answer(case, None, f_out)

if __name__ == "__main__":
    main(sys.argv)