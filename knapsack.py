import time
import sys


weights = []
values = []
subproblems = {}


def knapsack(n, w):
    if n < 0:
        return 0
    if n == 0:
        if w >= weights[0]:
            return values[0]
        else:
            return 0
    if str(n - 1) + ',' + str(w) in subproblems:
        opt_1 = subproblems[str(n - 1) + ',' + str(w)]
    else:
        opt_1 = knapsack(n - 1, w)

    if str(n - 1) + ',' + str(w - weights[n]) in subproblems:
        opt_2 = subproblems[str(n - 1) + ',' + str(w - weights[n])] + values[n]
    else:
        opt_2 = knapsack(n - 1, w - weights[n]) + values[n]

    opt = max(opt_1, opt_2)
    subproblems[str(n) + ',' + str(w)] = opt

    return opt


def knapsack_iterative():
    K = [[0 for x in range(W + 1)] for x in range(N + 1)]

    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
    # print (K)
    return K[N][W]


def knapsack_iterative_mem():
    K = [[0 for x in range(W + 1)] for x in range(2)]

    #ans = -1
    for i in range(N + 1):
        for w in range(W + 1):

            if i % 2 == 0:
                if weights[i - 1] <= w:
                    K[1][w] = max(values[i - 1] + K[0][w - weights[i - 1]], K[0][w])
                else:
                    K[1][w] = K[0][w]
            else:
                if weights[i - 1] <= w:
                    K[0][w] = max(values[i - 1] + K[1][w - weights[i - 1]], K[1][w])
                else:
                    K[0][w] = K[1][w]
        '''
        if i % 2 == 0:
            print (K[0])
            print (K[1])
        '''
    if N % 2 == 1:
        return K[0][W]
    else:
        return K[1][W]

    #return ans


def knapsack_iterative_mem_1():

    K = [0 for x in range(W + 1)]

    for i in range(N + 1):
        for w in range(W, -1, -1):
            if weights[i - 1] <= w:
                K[w] = max(values[i - 1] + K[w - weights[i - 1]], K[w])

        #print (K)
    return K[W]


i = 0
W = 0
N = 0
for line in open('knapsack.txt', 'r'):
    if i == 0:
        W = int(line.split()[0])
        N = int(line.split()[1])
    else:
        values.append(int(line.split()[0]))
        weights.append(int(line.split()[1]))
    i += 1
'''

values = [6, 10, 12]
weights = [1, 2, 3]
W = 5
N = 3
'''


def knapsack_fake(n1, k1, A1, limit):

    if k1 == 0:
        return 0

    if k1 < 0:
        return sys.maxint + 1

    approx_v = sys.maxint + 1
    min_add = 0
    for i1 in range(n1):
        opt1 = knapsack_fake(n1, k1 - A1[i1], A1, limit)
        if opt1 > approx_v:
            approx_v = opt1
            min_add = A1[i1]
    return approx_v + min_add


print(knapsack_fake(2, 8,[3,6], 3))

'''
T = int(sys.stdin.readline())
for i in range(T):
    input1 = sys.stdin.readline().split()
    n = int(input1[0])
    k = int(input1[1])
    health = []
    line = sys.stdin.readline().split()
    for health_val in line:
        health.append(int(health_val))
    print (knapsack_fake(n, k, health, min(health)))
'''
