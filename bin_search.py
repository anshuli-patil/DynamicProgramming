import sys


def get_icecream(a, m, n):
    icecreams = {}
    for i in range(len(a)):
        if a[i] in icecreams:
            icecreams[a[i]].append(i + 1)
        else:
            icecreams[a[i]] = [i + 1]

    for i in a:
        remaining = m - i
        if remaining in icecreams:
            i_id = icecreams[i][0]

            if remaining * 2 == m:
                if len(icecreams[remaining]) > 1:
                    #print(remaining, remaining * 2, m)
                    return (icecreams[remaining][0], icecreams[remaining][1])

                else:
                    continue
            id = icecreams[remaining][0]
            # return(([id, i_id]).sort())

            return(min(id, i_id, min(id, i_id)))


t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    ans = (get_icecream(a, m, n))
    print (str(ans[0]) + ' ' + str(ans[1]))
