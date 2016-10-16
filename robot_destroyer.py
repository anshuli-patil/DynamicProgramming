def robot_calc(x, f, n):
    # kth index contains tuple of (max robots destroyed for x[1:k], index of penultimate strike)
    robots_destroyed = []

    # initialize base cases
    robots_destroyed.insert(0, (0, 0))
    robots_destroyed.insert(1, (min(x[1], f[1]), 1))

    # dynamic programming
    for i in range(2, len(x)):
        max_val = -1
        max_index = -1

        print ('max( ')
        for j in range(0, i):
            max_val_local = max(max_val, robots_destroyed[j][0] + min(x[i], f[i - j]))

            if max_val_local != max_val:
                max_index = j
            max_val = max_val_local

            print ('{0:s} + min( {1:s} , {2:s} )'.format(str(robots_destroyed[j][0]), str(x[i]), str(f[i - j])))
        print (') = %s' % str(max_val))
        robots_destroyed.insert(i, (max_val, max_index))

    print (robots_destroyed)

    # compute the times when EMP is used
    index = n
    sequence = [n]
    while index != 0:
        sequence.append(robots_destroyed[index][1])
        index = robots_destroyed[index][1]
    sequence = sequence[:len(sequence) - 1]

    print ("sequence:")
    print (sequence)

    # total robots destroyed is stored here
    return robots_destroyed[n][0]


x1 = [-1, 1, 10, 10, 1]
f1 = [-1, 1, 2, 4, 8]

print (robot_calc(x1, f1, 4))

x2 = [-1, 10, 2, 1, 7]
f2 = [-1, 1, 2, 4, 6]

print (robot_calc(x2, f2, 4))
