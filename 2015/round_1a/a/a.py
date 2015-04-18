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

def solve(N, m):
    mn1 = 0
    mn2 = 0
    mx1 = 0
    for i in xrange(1, N):
        if m[i] < m[i-1]:
            mx1 = max(mx1, m[i-1]-m[i])
    for i in xrange(1, N):
        a = 0
        b = 0
        if m[i] < m[i-1]:
            a = m[i-1] - m[i]
            b = min(mx1, m[i-1])
        else:
            b = min(mx1, m[i-1])
        mn1 += a
        mn2 += b

    return (mn1, mn2,)


def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        N = int(f.readline())
        m = map(int, f.readline().split(" "))
        mn1, mn2 = solve(N, m)
        print_answer(t, "%d %d" % (mn1, mn2), f_out)


if __name__ == "__main__":
    main(sys.argv)
