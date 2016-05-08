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

def get_arrangement(N, P):
    ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    B = [[i, 0] for i in xrange(0, len(P))]
    total = sum([p[1] for p in P])
    c = 2
    B[0][1] = 1
    B[1][1] = 1
    plan = ["AB"]
    while c < total:
        half = (sum([b[1] for b in B]) + 1)/2
        B.sort(key=lambda b: b[1])
        cplan = ""
        for i in xrange(0, len(B)):
            j, b = B[i]
            if b < P[j][1] and b <= half:
                B[i][1] = B[i][1] + 1
                c = c + 1
                cplan = cplan + ALPHA[j]
                break
        if not verify(B):
            half = (sum([b[1] for b in B]) + 1)/2
            B.sort(key=lambda b: b[1])
            for i in xrange(0, len(B)):
                j, b = B[i]
                if b < P[j][1] and b <= half:
                    B[i][1] = B[i][1] + 1
                    c = c + 1
                    cplan = cplan + ALPHA[j]
                    break
        assert verify(B)
        plan.append(cplan)
    plan.reverse()
    return ' '.join(plan)

def verify(B):
    for i in xrange(0, len(B)):
        s = 0
        for j in xrange(0, len(B)):
            if i != j:
                s = s + B[j][1]
        if B[i][1] > s:
            return False
    return True

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        N = int(f.readline())
        P = [(p[0], int(p[1])) for p in enumerate(f.readline().rstrip('\n').split(' '))]
        arrangement = get_arrangement(N, P)
        print_answer(t, arrangement, f_out)


if __name__ == "__main__":
    main(sys.argv)
