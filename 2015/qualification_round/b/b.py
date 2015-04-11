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

def min_steps(diners):
    steps = 0
    current = set([tuple(sorted(diners))])
    nexts = set()
    while current or nexts:
        if not current:
            current.update(nexts)
            nexts.clear()
            steps = steps + 1
        current_diners = current.pop()
        if not current_diners or current_diners[-1] <= 0:
            break
        regular = tuple([diner-1 for diner in current_diners if diner-1>0])
        nexts.add(regular)
        mx = current_diners[-1]
        for i in xrange(1, (mx/2)+1):
            special = [diner for diner in current_diners]
            special[-1] = i
            special.append(mx-i)
            special.sort()
            nexts.add(tuple(special))
    return steps

def main(argv):
    with open(get_file(argv), 'r') as f, open(get_file_out(argv), 'w') as f_out:
        T = int(f.readline())
        for t in xrange(1, T+1):
            N = int(f.readline())
            initial = [int(x) for x in f.readline().split(' ')]
            current_pancakes = max(initial)
            print_answer(t, "%d" % min_steps(initial), f_out)

if __name__ == "__main__":
    main(sys.argv)
