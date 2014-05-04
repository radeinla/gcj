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

def get_min_ops(strs):
    n = 0
    sequence = []
    sample = strs[0]
    prev = None
    for i in xrange(0, len(sample)):
        if sample[i] != prev:
            sequence.append(sample[i])
        prev = sample[i]
    for i in xrange(0, len(sequence)):
        mn = 101
        mx = 0
        for s in strs:
            sub = 0
            if len(s) == 0:
                return None
            while len(s) and s[0] == sequence[i]:
                s.pop(0)
                sub = sub + 1
            if sub == 0:
                return None
            else:
                mx = max(mx, sub)
                mn = min(mn, sub)
        n = n + mx - mn
    for s in strs:
        if len(s) > 0:
            return None
    return n

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        N = int(f.readline())
        strs = []
        for i in xrange(0, N):
            strs.append(list(f.readline().strip()))
        min_ops = get_min_ops(strs)
        if min_ops is not None:
            print_answer(case, min_ops, f_out)
        else:
            print_answer(case, 'Fegla Won', f_out)

if __name__ == "__main__":
    main(sys.argv)