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


def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        a = int(f.readline())
        for i in xrange(0,4):
            line = f.readline()
            if i == a-1:
                A = [int(temp) for temp in line.split(" ")]
        b = int(f.readline())
        for i in xrange(0,4):
            line = f.readline()
            if i == b-1:
                B = [int(temp) for temp in line.split(" ")] 
        same = set(A).intersection(B)
        if len(same) == 0:
            print_answer(t, "Volunteer cheated!", f_out)
        elif len(same) == 1:
            print_answer(t, "%d" % same.pop(), f_out)
        else:
            print_answer(t, "Bad magician!", f_out)


if __name__ == "__main__":
    main(sys.argv)