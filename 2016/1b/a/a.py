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

def get_number(S):
    L = list(S)
    M = {}
    for c in S:
        if c in M:
            M[c] = M[c] + 1
        else:
            M[c] = 1
    O = ['Z', 'W', 'U', 'X', 'G', 'F', 'V', 'R', 'O', 'N']
    uniques = {
        'Z': ['Z', 'E', 'R', 'O'],
        'W': ['T', 'W', 'O'],
        'U': ['F', 'O', 'U', 'R'],
        'X': ['S', 'I', 'X'],
        'G': ['E', 'I', 'G', 'H', 'T'],
        'F': ['F', 'I', 'V', 'E'],
        'V': ['S', 'E', 'V', 'E', 'N'],
        'R': ['T', 'H', 'R', 'E', 'E'],
        'O': ['O', 'N', 'E'],
        'N': ['N', 'I', 'N', 'E'],
    }
    assert len(uniques) == 10
    mapping = {
        'Z': 0,
        'W': 2,
        'U': 4,
        'X': 6,
        'G': 8,
        'F': 5,
        'V': 7,
        'R': 3,
        'O': 1,
        'N': 9,
    }
    assert len(mapping) == 10
    done = 0
    numbers = []
    for u in O:
        uc = uniques[u]
        if u in M and M[u] > 0:
            to_remove = M[u]
            for i in xrange(0, to_remove):
                numbers.append(str(mapping[u]))
                for c in uc:
                    M[c] = M[c] - 1
                    done = done + 1
    numbers.sort()
    return ''.join(numbers)

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        S = f.readline().strip()
        number = get_number(S)
        print_answer(t, number, f_out)


if __name__ == "__main__":
    main(sys.argv)
