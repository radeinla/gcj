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

def count_happies(S):
    count = 0
    for p in S:
        if p % 2 == 1:
            count += 1
    return count

def find_sads(S):
    sads = []
    for i in xrange(0, len(S)):
        if S[i] == 0:
            sads.append(i)
    return sads

def flip(S, i, K):
    if i > len(S)-K+1:
        return S
    new_S = [state for state in S]
    new_S = tuple((p + 1) % 2 if (j>=i and j<i+K) else p for j, p in enumerate(S))
    return new_S

def trim(S, N, K):
    for first_sad in xrange(0, len(S)):
        if S[first_sad] == 0:
            break
    if N-first_sad < K*2+1:
        return S
    return tuple(S[first_sad:len(S)])

def get_min_flips(S, K, N, done, queue, queued):
    while len(queue) > 0:
        test, depth = queue.pop(0)
        sads = find_sads(test)
        if len(sads) == 0:
            return depth
        done[test] = True
        N = len(test)
        if sads[0] > N-K:
            return None
        else:
            new_S = flip(test, sads[0], K)
            queued.add(new_S)
            queue.append((new_S, depth+1))
    return None

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        S, K = f.readline().split(" ")
        S = tuple(1 if c == '+' else 0 for c in S)
        K = int(K)
        N = len(S)
        flips = get_min_flips(S, K, N, {}, [(S,0)], set(S))
        if flips is None:
            flips = "IMPOSSIBLE"
        print_answer(t, flips, f_out)


if __name__ == "__main__":
    main(sys.argv)
