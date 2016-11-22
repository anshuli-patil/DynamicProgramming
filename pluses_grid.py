# https://www.hackerrank.com/challenges/two-pluses
import sys
import operator


def largest_plus_area(a, m, n):
    # return(find_largest_plus(2,4,a,m,n))
    pluses = {}
    for i in range(m):
        for j in range(n):
            pluses.update({(i, j): find_largest_plus(i, j, a, m, n)})
    # print(pluses)
    sorted_pluses = sorted(pluses.items(), key=operator.itemgetter(1))

    max_area = 0
    for i in range(len(pluses)):
        indices_i = sorted_pluses[i][0]
        max_range_i = sorted_pluses[i][1]
        for j in range(i):
            indices_j = sorted_pluses[j][0]
            max_range_j = sorted_pluses[j][1]
            # print(indices_i, max_range_i, indices_j, max_range_j)
            for k_i in range(max_range_i, -1, -1):
                for k_j in range(max_range_j, -1, -1):
                    if check_overlapping(pluses, indices_i[0], indices_i[1], k_i, indices_j[0], indices_j[1], k_j):
                        max_area = max(max_area, area(k_i, k_j))
    return max_area


def area(k1, k2):
    area1 = (k1 - 1) * 4 + 1
    area2 = (k2 - 1) * 4 + 1

    if area1 > 0 and area2 > 0:
        total = area1 * area2
        return total
    return 0


def check_overlapping(pluses, i1, j1, range_len1, i2, j2, range_len2):
    # range_len1 = pluses[i1][j1]
    # range_len2 = pluses[i2][j2]

    range1 = {}

    for i in range(range_len1):
        range1.update({(i1 + i, j1 + i)})
    for i in range(range_len2):
        if (i2 + i, j2 + i) in range1:
            return False
    return True


def find_largest_plus(i, j, a, m, n):
    if a[i][j] == 'B':
        return 0
    k = 1
    while in_range(i + k, j, m, n, a) and in_range(i - k, j, m, n, a) \
            and in_range(i, j + k, m, n, a) and in_range(i, j - k, m, n, a):

        if a[i + k][j] == 'G' and a[i - k][j] == 'G' \
                and a[i][j + k] == 'G' and a[i][j - k] == 'G':
            k += 1
    return k


def in_range(i, j, m, n, a):
    if i >= 0 and i < m and j >= 0 and j < n and a[i][j] == 'G':
        return True
    return False


nm = sys.stdin.readline().split()
m = int(nm[0])
n = int(nm[1])
grid = []
for j in range(m):
    line = sys.stdin.readline().split()[0]
    grid.append(list(line[0:len(line)]))
print (largest_plus_area(grid, m, n))
