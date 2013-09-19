# Andrew 
from math import *
import sys
import scipy.misc.derivative as df
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

def newtons(f, guess):
    try:
        delta = f(guess)/drink(f,guess)
    except ZeroDivisionError:
        return guess
    if fabs(delta) < error:
        return guess
    else:
        return newtons(f, guess - delta)

def newton(f, guess):
    try:
        delta = f(guess)/df(f,guess)
    except ZeroDivisionError:
        return guess
    if fabs(delta) < error:
        return guess
    else:
        return newtons(f, guess - delta)

# the hackiest hack that ever hacked
# don't drink and (approximatly) derive
def drink(f, x):
    p0 = x - error
    p1 = x + error
    slope =  (f(p1)-f(p0))/(2*error)
    print p0,p1,(f(p1)-f(p0))
    return slope

#each of the 6 problems as tuple
problems= [(lambda x: 3 * x - exp(x), 1.0 , 2.0), 
(lambda x: x + 3 * cos(x) - exp(x), 0, 1),  
(lambda x : x**2 -4*x + 4 - log(x), 1, 2), (lambda x : x**2 -4*x + 4 - log(x), 2, 4),
(lambda x: x + 1 - 2*sin(pi*x), 0, 0.5), (lambda x: x + 1 - 2*sin(pi*x), 0.5, 1)]

#results =  map(lambda x: bisection(x[0],x[1],x[2]), problems)
#for result in results:
#    print result


print newtons(lambda x: x, 2000)
