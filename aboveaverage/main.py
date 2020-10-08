#Input: The first line of standard input contains an integer 1 \le C \le 50, the number of test cases. C data sets follow. Each data set begins with an integer, N, the number of people in the class (1 \le N \le 1000). N integers follow, separated by spaces or newlines, each giving the final grade (an integer between 0 and 100) of a student in the class.

#Output: For each case you are to output a line giving the percentage of students whose grade is above average, rounded to exactly 3 decimal places.

import sys

n = int(sys.stdin.readline())

for _ in range(n):
    values = [int(e) for e in sys.stdin.readline().split()[1:]]
    avg = sum(values) / len(values)

    num_above_average = len([e for e in values if e > avg])

    print("{:10.3f}%".format( (num_above_average / len(values)) * 100 ))
