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

def str_to_num(S):
    return int(''.join(S).lstrip('0'))

def is_tidy(S):
    for i in xrange(1, len(S)):
        if int(S[i]) < int(S[i-1]):
            return i
    return None

def make_tidy(S, bad, N):
    d1 = int(S[bad])
    d2 = int(S[bad-1])
    S2 = list(S)
    borrow = bad-1
    for i in xrange(bad-1, -1, -1):
        if int(S[i]) > 0:
            borrow = i
            break
    S2[borrow] = str(int(S[borrow]) - 1)
    for i in xrange(borrow+1, len(S)):
        S2[i] = '9'
    return S2

def get_nearest_tidy(S, N, current):
    first_bad = is_tidy(current)
    if first_bad is None:
        return str_to_num(current)
    tidy = make_tidy(current, first_bad, N)
    return get_nearest_tidy(S, N, tidy)

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        S = list(f.readline().strip())
        tidy = get_nearest_tidy(S, str_to_num(S), S)
        print_answer(t, tidy, f_out)


if __name__ == "__main__":
    main(sys.argv)
