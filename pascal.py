def pascal(k):
    line1 = [1]
    line2 = []
    for i in range(1,k+1):
        for j in range(i):
            part1 = 0
            part2 = 0
            if j-1 >= 0:
                part1 = line1[j-1]
            if j < len(line1):
                part2 = line1[j]
            line2.append(part1 + part2)
        line1 = line2
        line2 = []
        print line1

pascal(7)
