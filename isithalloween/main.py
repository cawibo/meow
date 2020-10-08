#Input: The input consists of a single line containing a date of the format FEB 9, with the month and date separated by a single space.

#Output: If the date is October 31 or December 25, output yup. Otherwise, output nope.

import sys

date = sys.stdin.readline().strip()

if date in ["OCT 31", "DEC 25"]:
    print("yup")
else:
    print("nope")