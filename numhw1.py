# Andrew Rosen
# Numerical Analysis Programming Project 1
# Tested on python 2.7.3
# Usage: python hw1.py

from math import *
import sys
error =  sys.float_info.epsilon * 10    # close enough that errors won't be my fault

def bisection(func, a, b):
    p = (a+b)/2.0
    fp = func(p)
    if fabs(fp) < error :
        return p
    else:
        fa = func(a) 
        if (fa > 0 and fp > 0) or (fa < 0 and fp < 0):
            #signs are same
            return bisection(func, p, b)
        else:
            #signs are different
            return bisection(func, a, p)

def newton(f,df,guess):
    try:
        delta = float(f(guess))/float(df(guess))
    except ZeroDivisionError:
        return guess
    if fabs(delta) < error:
        return guess
    else:
        return newton(f, df, guess - delta)

#each of the 6 problems as tuple
#exp(x) ~ e**x
#log(x) with no base defaults to natural log
problems= [(lambda x: 3 * x - exp(x), 1.0 , 2.0), 
(lambda x: x + 3 * cos(x) - exp(x), 0, 1),  
(lambda x : x**2 -4*x + 4 - log(x), 1, 2), (lambda x : x**2 -4*x + 4 - log(x), 2, 4),
(lambda x: x + 1 - 2*sin(pi*x), 0, 0.5), (lambda x: x + 1 - 2*sin(pi*x), 0.5, 1)]

problems_2 = [
(lambda x: x**3  - 2*(x**2) - 5, lambda x: 3*(x**2) - 4*x, 1,4),
(lambda x: x**3 + 3*(x**2) - 1 , lambda x: 3*(x**2) + 6*x,-3, -2),
(lambda x: x - cos(x)          , lambda x: 1 + sin(x), 0, pi/2 ),
(lambda x: x - 0.8 - 0.2*sin(x), lambda x: 1 - 0.2*cos(x), 0,pi/2)]


results =  map(lambda x: bisection(x[0],x[1],x[2]), problems)
print "System epsilon is ", sys.float_info.epsilon
print "bisection examples:"
for result in results:
    print result

print "\n\n"

print "Newton's examples:"
blahs = map(lambda x: newton(x[0], x[1],(x[2]+x[3])/2) , problems_2)
for blah in blahs:
    print blah
