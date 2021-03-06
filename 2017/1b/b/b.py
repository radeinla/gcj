#!/usr/bin/python
import sys

PROBLEM = 'b'

dataset = ''

if len(sys.argv) == 2:
    dataset = sys.argv[1]


def get_file(argv):
    if len(argv) == 1:
        return "{}.in".format(PROBLEM)
    else:
        return "{}_{}.in".format(PROBLEM, dataset)

def get_file_out(argv):
    if len(argv) == 1:
        return "{}.out".format(PROBLEM)
    else:
        return "{}_{}.out".format(PROBLEM, dataset)

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def get_last_number(N):
    past_numbers = set()
    goal = set([i for i in xrange(1, 10)])
    found = set()
    multiplier = 1
    current_number = N
    while current_number not in past_numbers:
        digits = [int(d) for d in str(current_number)]
        found.update(digits)
        if len(found) == 10:
            return current_number
        past_numbers.add(N)
        multiplier = multiplier + 1
        current_number = N * multiplier
    return None

def gcdIter(a, b):
    if b == 0:
        return a
    else:
        return gcdIter(b, a % b)

# Z ?? = (K + St - Y) / t ??
def get_best_speed(Y, k, s, t):
    print k, Y, s, t
    return (k + (s*t) - Y)/t

def time_to_same(D, N, k, s, Y, Z):
    #t = (K-Y)/(Z-S)
    return (float(k)-Y) / (Z-s)


def simulate(D, N, K, S, Z):
    starting_point = 0
    KS = zip(K, S)
    while True:
        best = KS.sort(lambda ks: time_to_same())



def get_max(D, N, K, S, KS):
    best = D/((D-K[0])/S[0])
    # print best
    for i in xrange(0, N):
        cand = D/((D-K[i])/S[i])
        # print cand
        best = min(best, cand)
    return best

RED = 0
BLUE = 1
YELLOW = 2

R, O, Y, G, B, V = list(xrange(0, 6))

MAPPING = {
    (R): (1,0,0),
    (O): (1,0,1),
    (Y): (0,0,1),#{(RED): 0, (BLUE): 0, YELLOW:1},
    (G): (0,1,1),#{(RED): 0, (BLUE): 1, YELLOW:1},
    (B): (0,1,0),#{(RED): 0, (BLUE): 1, YELLOW:0},
    (V): (1,1,0),#{(RED): 1, (BLUE): 1, YELLOW:0},
}

LABEL_MAPPING = {
    R: 'R',
    O: 'O',
    Y: 'Y',
    G: 'G',
    B: 'B',
    V: 'V',
}

import collections

def get_arrangement(N, U):
    counter = collections.Counter()
    for i, n in enumerate(U):
        counter[i] += n

    with_items = 0
    for k, v in counter.iteritems():
        if v > 0:
            with_items += 1

    for n in U:
        if n > 0 and n > N/2:
            return 'IMPOSSIBLE'

    arrangement = [None] * N

    all_items = sum(counter.values())
    i = 0
    for color, count in counter.most_common():
        for j in xrange(0, count):
            arrangement[i] = LABEL_MAPPING[color]
            i = i + 2
            if i > N-1:
                i = (i % 2) + 1


    return ''.join(arrangement)


def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        # ROYGBIV
        U = map(int, f.readline().strip().split())
        N, U = U[0], U[1:]
        print_answer(t, "{}".format(get_arrangement(N, U)), f_out)


if __name__ == "__main__":
    main(sys.argv)
