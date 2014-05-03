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

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        A, B, K = [int(tmp) for tmp in f.readline().split(' ')]
        if B < A:
            A, B = B, A
        n = 0
        for i in xrange(0, min(A, B)):
            if i&i < K:
                n = n + 1
        for i in xrange(0, A):
            for j in xrange(i+1, B):
                if i&j < K:
                    if i < A and j < B:
                        n = n + 1
                    if i < B and j < A:
                        n = n + 1
        print_answer(case, n, f_out)

if __name__ == "__main__":
    main(sys.argv)