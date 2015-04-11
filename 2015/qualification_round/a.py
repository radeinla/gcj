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
        line = f.readline()
        smax, audience = line.split(" ")
        smax = int(smax)
        min_friends = 0
        so_far = 0
        for shyness in xrange(0, smax+1):
            shy = int(audience[shyness])
            friends_to_invite = max(0, shyness - so_far)
            min_friends = min_friends + friends_to_invite
            so_far = so_far + shy + friends_to_invite
        print_answer(t, "%d" % min_friends, f_out)


if __name__ == "__main__":
    main(sys.argv)
