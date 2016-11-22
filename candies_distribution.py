import operator
from collections import defaultdict


def distribute(ratings):
    ratings_dict = {i: ratings[i] for i in range(len(ratings))}
    candies = {}
    sorted_ratings = sorted(ratings_dict.items(), key = operator.itemgetter(1))

    for i in range(len(ratings)):
        sindex = sorted_ratings[i][0]
        rating = sorted_ratings[i][1]

        candies_n1 = 0
        candies_n2 = 0

        if index + 1 < len(ratings) and rating > ratings[index + 1]:
            candies_n1 = candies.get(index + 1, 0) # defaults to 0 if not found

        if index - 1 >= 0 and rating > ratings[index - 1]:
            candies_n2 = candies.get(index - 1, 0)

        candies[index] = max(candies_n1 + 1, candies_n2 + 1)
    print (candies)

    total_candies = 0
    for i in candies:
        total_candies += candies[i]

    return total_candies


print (distribute([2,
4,
2,
6,
1,
7,
8,
9,
2,
1]))
