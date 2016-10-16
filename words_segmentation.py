import sys

dict_words = {}


def create_dict():
    f = open('words.txt', 'r')
    for line in f:
        line = line.rstrip()
        #line = line.lower()
        dict_words[line] = 1
    f.close()


def quality(word):
    if len(dict_words) == 0:
        create_dict()
    if word in dict_words and (len(word) > 1 or word == 'a' or word == 'i'):
        print word +' is a word in the dictionary'
        return 1
    else:
        return -100000


segments = []


def max(start, end, y):

    max_quality = quality(y[start:end])
    max_index_list = []
    for i in range((start+1), end):
        if quality(y[start:i]) > 0:
            print y[start:i]
            max_local, max_indices = max(i, end, y)

            max_local += quality(y[start:i])
            if max_local > max_quality:

                max_quality = max_local
                max_index_list = [i,max_indices]

    return max_quality, max_index_list


# Run
segment_string = "meetateight"
segments_len = len(segment_string) - 1
print max(0, len(segment_string), segment_string)
