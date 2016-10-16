import numpy


def compute_best_recursive(x, s):
    n = len(x)
    compute = numpy.full((n + 1, n + 1), -1)
    return compute_best_rec(x, s, 0, 0, compute)


def compute_best_rec(x, s, start, s_index, compute):
    if start == len(x):
        return 0
    else:
        option_continue = min(x[start], s[s_index])
        if compute[start + 1][s_index + 1] == -1:
            compute[start + 1][s_index + 1] = compute_best_rec(x, s, start + 1, s_index + 1, compute)
        option_continue += compute[start + 1][s_index + 1]

        option_reboot = 0
        if compute[start + 1][0] == -1:
            compute[start + 1][0] = compute_best_rec(x, s, start + 1, 0, compute)
        option_reboot += compute[start + 1][0]

        return max(option_continue, option_reboot)


def compute_best(x, s):
    n = len(x)
    compute = numpy.zeros(shape=(n, n))

    # initialize the solution matrix with the base cases
    for i in range(0, n):
        compute[n - 1][i] = min(x[n - 1], s[i])

    for j in range(0, n-1):
        compute[j][n - 1] = 0

    # compute for smaller subproblems
    for i in range(n - 2, -1, -1):
        for j in range(0, n - 1):
            option_continue = min(x[i], s[j]) + compute[i + 1][j + 1]

            option_reboot = compute[i + 1][0]
            compute[i][j] = max(option_continue, option_reboot)

    print (compute)
    return compute[0][0]


x1 = [10, 1, 7, 7]
s1 = [8, 4, 2, 1]

# print (compute_best_recursive(x1,s1))
print compute_best_recursive(x1, s1)
