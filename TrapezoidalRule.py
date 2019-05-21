'''

Arlan Vincent Uy

2015-09385

CS 131 THU

'''



'''

Juico, Jules Gerard E.

2014-40314

CS 131 THU

'''

import math
import random

'''
Input: x
Output: f(x)
Method: The function will return the value when x is plugged into the function. This function is the function inside the integral
'''
def Function(x):

	y = (x ** 2) * (math.log(x))
	return y

'''
Input: n as number of intervals, a as the lowerbound of the integral, b as the upperbound of the integral
Output: Estimate of the integral when Composite Trapezoidal Rule is used
Method: The function just computes the approximation by directly applying Composite Trapezoidal Rule
'''
def CompositeTrapezoidalRule(n, a, b):

	h = (b - a) / n
	estimate = 0

	for i in range(0, n):
		x = a + (i * h)
		estimate = estimate + Function(x) + Function(x + h)
	estimate = (h * estimate) / 2

	return estimate

'''
Input: n as number of intervals, a as the lowerbound of the integral, b as the upperbound of the integral
Output: Estimate of the integral when Composite Simpson's Rule is used
Method: The function just computes the approximation by directly applying Composite Simpson's Rule
'''
def CompositeSimpsonsRule(n, a, b):

	h = (b - a) / n
	estimate = 0

	for i in range(0, n, 2):
		x = a + (i * h)
		estimate = estimate + Function(x) + (4 * Function(x + h)) + Function(x + (2 * h))
	estimate = (h * estimate) / 3

	return estimate

'''
Input: n as number of intervals, a as the lowerbound of the integral, b as the upperbound of the integral, c as a number between a and b
Output: The error rate of Composite Trapezoidal Rule
Method: Computes h using the upper and lower bounds and the number of intervals, then uses that to compute the error and the ratio which is error/h^2
'''
def CompositeTrapezoidalRuleError(n, c, a, b):

	h = (b - a) / n
	error = (-(h ** 3) * ((2 * math.log10(c)) + 3)) / 12
	ratio = error / (h ** 2)
	return (error, ratio)

'''
Input: n as number of intervals, a as the lowerbound of the integral, b as the upperbound of the integral, c as a number between a and b
Output: The error rate of Composite Trapezoidal Rule
Method: Computes h using the upper and lower bounds and the number of intervals, then uses that to compute the error and the ratio which is error/h^4
'''
def CompositeSimpsonsRuleError(n, c, a, b):

	h = (b - a) / n
	error = (-(h**5) * (-2 / (c ** 2))) / 180
	ratio = error / (h ** 4)
	return (error, ratio)

intervals = int(input("Enter number of intervals: "))
b = 1.5
a = 1

'''
for j in range(2, intervals, 2):
	print("h = {}".format(j))
	print(CompositeTrapezoidalRule(j, a, b))
	print(CompositeSimpsonsRule(j, a, b))
'''

print("Composite Trapezoidal Rule: {}".format(CompositeTrapezoidalRule(intervals, a, b)))
print("Composite Simpson's Rule {}".format(CompositeSimpsonsRule(intervals, a, b)))

h = (1.5 - 1)/intervals
#r = random.randint(0, 100)
#c = 1 + (h * r)
c = 1.25
print("h = {}".format(h))
print("Composite Trapezoidal rule error and ratio: {}".format(CompositeTrapezoidalRuleError(intervals, c, a, b)))
print("Composite Simpson's rule error and ratio: {}".format(CompositeSimpsonsRuleError(intervals, c, a, b)))


#Matthews. Mathfaculty.Fullerton.edu. 2003. PDF. 20 May. 2019