#Input: The first and only line of input will contain at most 100 characters, uppercase and lowercase letters of the English alphabet and hyphen (‘-’ ASCII 45). The first character will always be an uppercase letter. Hyphens will always be followed by an uppercase letter. All other characters will be lowercase letters.

#Output: The first and only line of output should contain the appropriate short variation.

import sys

print( "".join([e[0] for e in sys.stdin.readline().split("-")]) )