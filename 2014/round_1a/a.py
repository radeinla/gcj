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

flip = {
    '0': '1',
    '1': '0'
}

def diff(outlet, device, L):
    d = []
    for i in xrange(0, L):
        if outlet[i] != device[i]:
            d.append(i)
    return d

def matches(outlets, reference, diff):
    new_outlets = []
    for outlet in outlets:
        new_outlet = list(outlet)
        for i in diff:
            new_outlet[i] = flip[new_outlet[i]]
        new_outlets.append(''.join(new_outlet))
    return set(new_outlets) == reference

def get_min(outlets, devices, L):
    dev = devices[0]
    min_flips = L + 1
    reference = set(devices)
    for outlet in outlets:
        d = diff(outlet, dev, L)
        if matches(outlets, reference, d):
            min_flips = min(min_flips, len(d))
    return min_flips

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        N, L = [int(d) for d in (f.readline().split(' '))]
        outlets = f.readline().replace('\n', '').split(' ')
        devices = f.readline().replace('\n', '').split(' ')
        min_flips = get_min(outlets, devices, L)
        if min_flips <= L:
            print_answer(case, min_flips, f_out)
        else:
            print_answer(case, 'NOT POSSIBLE', f_out)
            

if __name__ == "__main__":
    main(sys.argv)