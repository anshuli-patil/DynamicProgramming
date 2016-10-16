import numpy


def alice(tips):
    n = len(tips)

    # alice_total[row][col] is the max tips Alice can make if she has to choose from sublist - tips[col..row]
    alice_total = numpy.zeros(shape=(n, n))

    for i in range(0, n):
        alice_total[i][i] = tips[i]

    for i in range(1, n):
        alice_total[i][i - 1] = max(tips[i - 1], tips[i])

    for i in range(2, n):
        for j in range(0, n - i):
            # iterating diagonally
            end = j + i
            start = j

            # Case1: if Alice picks the first bill
            opt_first = tips[start]
            # Bill picks the best of the two extremes in his turn
            if tips[start + 1] > tips[end]:
                # the list of bills left for Alice is tips[start+2..end]
                opt_first += alice_total[end, start + 2]
            else:
                # Alice chooses from extreme of tips[start+1..end-1]
                opt_first += alice_total[end - 1, start + 1]

            # Case2: Alice picks the last bill
            opt_last = tips[end]
            if tips[start] > tips[end - 1]:
                opt_last += alice_total[end - 1][start + 1]
            else:
                opt_last += alice_total[end - 2][start]
            alice_total[end][start] = max(opt_first, opt_last)

    print alice_total
    return alice_total[n-1][0]


tips1 = [5, 10, 1, 5]
print (alice(tips1))
