# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas
import math

n = int(input())
numbers = [int(number) for number in input().split()]
series = pandas.Series(numbers)

def bounds(series):
    #95% : Z=1.96
    z = 1.96
    mean = series.mean()
    stdev = series.std(ddof=0)
    delta = z*stdev/math.sqrt(len(series))
    return mean-delta, mean+delta

mean = series.mean()
median = series.median()
mode = series.mode().min()
stdev = series.std(ddof=0)
lower_bound, upper_bound = bounds(series)

print(f'{mean:.1f}')
print(f'{median:.1f}')
print(mode)
print(f'{stdev:.1f}')
print(f'{lower_bound:.1f}', f'{upper_bound:.1f}')

#ddof=0 for sample, ddof=1 for population