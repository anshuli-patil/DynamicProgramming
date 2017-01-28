import sys


def anagram(word):
    if len(word) == 1:
        return [word]
    anagrams = []
    for i in range(len(word)):
        word_substring = word[:i] + word[i + 1:]
        iter_char = word[i]

        anagrams_substring = anagram(word_substring)
        for anagram_substring in anagrams_substring:
            anagrams.append(iter_char + anagram_substring)

    return anagrams

print(anagram('anshulip'))
