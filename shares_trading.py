def trading(shares):
    if len(shares) < 2:
        return -1
    profit = -1
    min_buy = shares[0]
    if shares[1] >= shares[0]:
        profit = shares[1] - shares[0]
        min_buy = shares[0]
        # print (profit),
    for i in range(2, len(shares)):
        opt1 = shares[i] - shares[i-1]
        opt2 = shares[i] - min_buy
        if opt1 > profit:
            profit = opt1
            min_buy = shares[i-1]
        if opt2 > profit:
            profit = opt2
        # print (profit),
    print (min_buy)
    return profit

shares1 = [12, 3, 10, 2, 4, 11, 1]
print (trading(shares1))
