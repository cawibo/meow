#Input: The first line of input contains an integer 1 \le n \le 100, the number of test cases. Each test case consists of two lines of input; each a pattern. Patterns consist of lowercase words, and placeholders containing lowercase words. No pattern exceeds 100 characters. Words contain at most 16 characters. A single space separates adjacent words and placeholders.

#Output: For each test case, output a phrase that matches both patterns. If several phrases match, any will do, but all words used in the phrase must obey the same constraints as the words in the input (i.e., they must be lowercase and of length at most 16). If no phrase matches, output a line containing “-” (a single minus sign).

import sys

# for every testcase...
for _ in range(int(sys.stdin.readline)):

    first = sys.stdin.readline().split()
    second = sys.stdin.readline().split()

    placeholders = {}

    for word1, word2 in zip(first, second):
        if word1[0] == "<" and word2[0] == "<":
            continue
        elif word1[0] == "<":
            placeholders[word1] = word2
        elif word2[0] == "<":
            placeholders[word2] = word1
        else:
            sys.exit(2)
    


