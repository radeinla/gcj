#!/usr/bin/python
import sys
import math
import collections
import bisect

PROBLEM = 'a'

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

def get_d(p):
    return p[0]*2

def get_r(p):
    return p[0]

def get_h(p):
    return p[1]

# def get_exposed(p, p_after):
#     return p_after.

def get_top(p):
    return (get_r(p) ** 2)# * math.pi

def get_side(p):
    return 2 * get_r(p) * get_h(p) #* math.pi

def get_new(p_top, p_bottom):
    return get_top(p_bottom) - get_top(p_top) + get_side(p_bottom)

def get_in_between(p_top, p_bottom):
    return get_top(p_bottom) - get_top(p_top)

def get_exposed(N, K, P):#, i, j, k):
    mx = 0.0
    #if k == 1:
    #    mx += math.pi * (get_r(p) ** 2)
    # mx = get_top(P[0]) + get_side(P[0])
    # S = [[mx, 1]]
    mx_i = 0
    k_i = 1
    i_i = 2
    # first top
    S = [
        [{'e': get_top(P[0])+get_side(P[0]), 'k': 1, 'i': 0}]
    ]
    mx = get_top(P[0])+get_side(P[0])
    mm = len(S)
    for i in xrange(1, N):
        S.append([])
        t = get_top(P[i])
        s = get_side(P[i])
        if K == 1:
            mx = max(mx, t+s)
        else:
            S[i].append({'e': t+s, 'k': 1, 'i': i})
        # new_level = {}
        for j in xrange(0, len(S[i-1])):
            prev = S[i-1][j]
            prev_mx = prev['e']
            prev_k = prev['k']
            prev_i = prev['i']
            prev_t = get_top(P[prev_i])

            if prev_k == K:
                mx = max(mx, prev_mx)
            else:
                #dont use level
                S[i].append(prev)
                #use level
                # print get_new(P[prev_i], P[i])
                new_a = prev_mx + get_new(P[prev_i], P[i])
                new_k = prev_k + 1

                if new_k == K:
                    #print 'new_k==K', new_a
                    mx = max(mx, new_a)
                else:
                    S[i].append({'e': new_a, 'k':new_k, 'i':i})
        #S[i] = [new_level[i] for i in new_level]
        # mm = max(mm, len(S[i]))
        # print S
        # print 'sssss'
    # print K,mm

    # print '-------'
    return mx


def new_get_exposed(N, K, P):#, i, j, k):
    mx = 0.0
    #if k == 1:
    #    mx += math.pi * (get_r(p) ** 2)
    # mx = get_top(P[0]) + get_side(P[0])
    # S = [[mx, 1]]
    mx_i = 0
    k_i = 1
    i_i = 2
    # first top
    S = [
        [{'e': get_top(P[0])+get_side(P[0]), 'k': 1, 'i': 0}]
    ]
    mx = get_top(P[0])+get_side(P[0])
    mm = len(S)
    for i in xrange(1, N):
        S.append([])
        t = get_top(P[i])
        s = get_side(P[i])
        new_level = {}
        if K == 1:
            mx = max(mx, t+s)
        else:
            key = (1, get_r(P[i]))
            new_level[key] = {'e': t+s, 'k': 1, 'i': i}
            key = (1, 'min')
            new_level[key] = {'e': t+s, 'k': 1, 'i': i}
        for j in xrange(0, len(S[i-1])):
            prev = S[i-1][j]
            prev_mx = prev['e']
            prev_k = prev['k']
            prev_i = prev['i']
            prev_t = get_top(P[prev_i])

            if prev_k == K:
                mx = max(mx, prev_mx)
            else:
                #dont use level
                key = (prev_k, get_r(P[prev_i]))
                if key in new_level:
                    if prev['e'] > new_level[key]['e']:
                        new_level[key] = prev
                else:
                    new_level[key] = prev
                #use level
                new_a = prev_mx + get_new(P[prev_i], P[i])
                new_k = prev_k + 1

                if new_k == K:
                    #print 'new_k==K', new_a
                    mx = max(mx, new_a)
                else:
                    key = (new_k, get_r(P[i]))
                    if key in new_level:
                        if new_a > new_level[key]['e']:
                            new_level[key] = {'e': new_a, 'k':new_k, 'i':i}
                    else:
                        new_level[key] = {'e': new_a, 'k':new_k, 'i':i}
        S[i] = [new_level[j] for j in new_level]
        #mm = max(mm, len(S[i]))
        # print S[i]
    # print K,mm
    return mx

def best_get_exposed(N, K, P, i, j, k, e, last, MEMO):
    key = (i, k, e)
    if key in MEMO:
        return MEMO[key]
    if k == K:
        MEMO[key] = e
        return e
    if i >= N:
        MEMO[key] = 0
        return 0
    # print N, K, P, i, j, e
    # if i - j < K:
    #     return 0.0
    best = e
    # use
    use_e = 0
    p = P[i]
    if k == 0:
        use_e = get_top(p) + get_side(p)
    else:
        # print 'new', P[last], p
        use_e = get_new(P[last], p)
    best = max(best, best_get_exposed(N, K, P, i+1, j, k+1, e + use_e, i, MEMO))
    best = max(best, best_get_exposed(N, K, P, i+1, j, k, e, last, MEMO))
    MEMO[key] = best
    return best
    # not use
    # return max(best_get_exposed(N, K, P, i, j-1, k, e), best_get_exposed(N, K, P, i, j, k, e))
    # return best_get_exposed(N, K, P, i, j, k, e, last)
    

def visualize(S):
    print '--------'
    for i in xrange(0, len(S)):
        print '\t\t'.join(map(str, S[i]))
    print '--------'

def bottom_up(N, K, P):
    MEMO = collections.Counter()
    S = [[0.0 for i in xrange(0, K+1)] for j in xrange(0, N+1)]
    A = [[0.0 for i in xrange(0, K+1)] for j in xrange(0, N+1)]
    # MX = [0.0 for i in xrange(0, N+1)]
    # for i in xrange(N-1, 0, -1):
    #     for i2 in xrange(i-1, -1, -1):
    #         MX[i2] = max(MX[i2], get_in_between(P[i2], P[i]))
    #     # for j in xrange(i-1, -1, -1):
    #     #     print j, i
    #     #     # print i, j, get_in_between(P[j], P[i])
    #     #     MX[i] = max(MX[i], get_in_between(P[j], P[i]))
    # print MX

    for i in xrange(N-1, -1, -1):
        side = get_side(P[i])
        top = get_top(P[i])
        for j in xrange(K-1, -1, -1):
            candidates = [0.0]
            candidates.append(S[i+1][j])
            # print candidates

            # use
            if j == K-1 and j > 0:
                # print 'bottom'
                candidates.append(side)
            elif j == K-1 and j == 0:
                # print 'top and bottom'
                #bottom and top
                candidates.append(side + top)
            elif j == 0 and i + 1 < N:
                # print 'top and middle/bottom'
                candidates.append(A[i][j] + side + top)

                # for k in xrange(1, N-i):
                #     if i + k < N:
                #         # print 'top and middle/bottom, skipped previous'
                #         key = ('t/c,s', i+1, i+k, j+1)
                #         MEMO[key] += 1
                #         candidates.append(S[i+k][j+1] + get_in_between(P[i], P[i+k]) + side + top)


                # if i + 2 < N:
                #     print 'top and middle/bottom, skipped previous'
                #     candidates.append(S[i+2][j+1] + get_in_between(P[i], P[i+2]) + side + top)
            elif j > 0 and j + 1 < K and i + 1 < N:
                # print 'just middle's
                candidates.append(A[i][j] + side)
                # for k in xrange(1, N-i):
                #     if i + k < N:
                #         # print 'top and middle/bottom, skipped previous'
                #         key = ('m,s', i+1, i+k, j+1)
                #         MEMO[key] += 1
                #         candidates.append(S[i+k][j+1] + get_in_between(P[i], P[i+k]) + side)

            # skip
            if j > 0 and j < K-1:
                candidates.append(S[i+1][j+1])

            S[i][j] = max(candidates)
        # for j in xrange(1, K):
        #     A[i-1][j-1] = max(A[i][j-1], S[i][j] + MX[i])
        # mmmmm = 0.0
        for i2 in xrange(i-1, -1, -1):
            for j in xrange(1, K):
                # mmmmm = max(mmmmm, get_in_between(P[i2], P[i]))
                A[i2][j-1] = max(A[i2][j-1], S[i][j] + get_in_between(P[i2], P[i]))
        # print mmmmm, i, MX[0]
        # assert mmmmm == MX[0]
    return S[0][0]

def format(exposed):
    return "{0:.6f}".format(exposed)

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        N, K = map(int, f.readline().strip().split(' '))
        P = []
        for i in xrange(0, N):
            P.append(map(float, f.readline().strip().split(' ')))
        P.sort()
        b = bottom_up(N, K, P)
        # exposed = best_get_exposed(N, K, P, 0, N, 0, 0.0, None, {})
        # print t, b == exposed, b, exposed
        # assert b == exposed
        print_answer(t, "{0:.6f}".format(b*math.pi), f_out)


if __name__ == "__main__":
    main(sys.argv)
