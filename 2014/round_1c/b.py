#!/usr/bin/python

import sys
import itertools
import math

def get_file(argv):
    if len(argv) == 1:
        return "b.in"
    else:
        return "b_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "b.out"
    else:
        return "b_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def arrange(N, cars, order, rem):
    ans = 0
    for perm in itertools.permutations(cars):
        print perm
        valid = True
        for i in xrange(0, N-1):
            if perm[i][-1] != perm[i+1][0]:
                valid = False
                break
        if valid:
            print 'valid!'
            ans = ans + 1
    return ans

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for case in xrange(1, T+1):
        N = int(f.readline())
        cars = f.readline().strip().split(' ')
        cars = sorted(cars)
        n_cars = []
        valid = True
        last = cars[0][0]
        for car in cars:
            if last > car[0]:
                valid = False
                break
            for i in xrange(0, len(car)-1):
                if car[i] > car[i+1]:
                    valid = False
                    break
            if valid:
                # print 'valid!'
                # print n_cars
                n_cars.append(car)
                # print n_cars
            else:
                break
            last = car[-1]
        cars = []
        for car in n_cars:
            carr = "%s%s" % (car[0], car[-1])
            cars.append(carr)
        cars = sorted(cars)
        if not valid:
            print_answer(case, 0, f_out)
        else:   
            ans = 1 
            for i in xrange(0, N):
                same = 1
                for j in xrange(i+1, N):
                    if cars[i] == cars[j]:
                        same += 1
                ans *= math.factorial(same)
            print_answer(case, ans, f_out)
            # if len(cars) == 1:
            #     print_answer(case, 1, f_out)
            # else:
        # for i in xrange(0, N-1):
            # if i in xrange()

        # print_answer(case, ans, f_out)

if __name__ == "__main__":
    main(sys.argv)