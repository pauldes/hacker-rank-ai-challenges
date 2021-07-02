from statistics import mean
import numpy
from scipy.stats import linregress

x = numpy.array([15,12,8, 8, 7, 7, 7, 6, 5, 3])
y = numpy.array([10,25,17,11,13,17,20,13,9, 15])

r = linregress(x, y)
slope = r.slope
intercept = r.intercept

res = slope

print(f'{res:.3f}')