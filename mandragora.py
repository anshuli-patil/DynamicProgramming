import sys


def tackle_mandragora(health):
    health.sort()
    # for all tipping points, where we change over from eating to defeating
    defeating = defeating_cost_precompute(health)

    opt = 0
    for i in range(0, len(health) + 1):
        opt = max(opt, defeating_cost(i, defeating))

    return opt


def defeating_cost(i, defeating):
    return (i + 1) * defeating[i]


def defeating_cost_precompute(health):
    n = len(health) + 1
    defeating = [0 for x in range(n)]

    # defeating[len(health)] = health[len(health) - 1]
    defeating[len(health)] = 0
    for i in range(len(health) - 1, -1, -1):
        defeating[i] = defeating[i + 1] + health[i]

    return defeating

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    health = []
    line = sys.stdin.readline().split()
    for health_val in line:
        health.append(int(health_val))
    print (tackle_mandragora(health))
