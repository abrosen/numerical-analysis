#Andrew Rosen

from math import *

def computeCoeffs(x, y):
    diffs = divDiffs(x,y)
    coeffs = []
    for diff in diffs:
        coeffs.append(diff[0])
    return coeffs
    
    

def divDiffs(x,y):
    diffs = []
    for i in range(0, len(x)):
        diffs.append([None] * (len(x)-i))
    for i, col in enumerate(diffs):
        if i == 0 :
            diffs[i] = y
        else:
            for j in range(0, len(col)):
                col[j] = (diffs[i-1][j+1] - diffs[i-1][j])/(x[j+i] - x[j])
                col[j] = (diffs[i-1][j+1])/(x[j+i] - x[j]) - (diffs[i-1][j])/(x[j+i] - x[j])
            diffs[i] =  col
    return diffs
        
    
    
def dDiff(x,y):
    F=[[None for n in xrange(len(x))] for n in xrange(len(x))]
    for a in range(0,len(x)):
        F[a][0] = y[a]
    for i in range(1, len(x)):
        for j in range(1,i+1):
            F[i][j] = (F[i][j-1] - F[i-1][j-1])/(x[i] - x[i-j])
    ret = []
    for i in range(0, len(x)):
        ret.append(F[i][i])
    return ret    
    
    
def evalP(x, coeffs, target):
    terms = [1.0] * len(x)
    for i in range(1, len(terms)):
        terms[i] = terms[i-1] * (target - x[i-1])
    return   sum(map(lambda a, b: a*b, coeffs, terms))

def evalP2(x, coeffs, target):
    p = coeffs[0]
    for i in range(1,len(coeffs)):
        term = 1.0
        for j in range(0,i):
            term = term * (target - x[j])
        p = p + coeffs[i] * term
    return p

    
    
def chebyZeros(num):
    zeros = []
    for k in range(1,num+1):
        zeros.append(cos(pi*((2*k - 1.0)/(2*num))))
    return zeros



f = lambda x: (1 +( 25* x** 2))**(-1)
target = .985

x1 = []
for j in  range(0,21):
    x1.append(-1 +(j/10.0))
x2 = chebyZeros(21)    

y1 = map(f, x1)
y2 = map(f, x2)


ans = f(target)
calc1 = evalP(x1,computeCoeffs(x1,y1),target)
calc2 = evalP(x2,computeCoeffs(x2,y2),target)

print "f(x):       ", ans
print "Calculated: ", calc1, calc2
print "Error:     ", fabs(calc1 - ans), fabs(calc2 - ans) 
