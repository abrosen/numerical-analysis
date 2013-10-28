from math import *

def computeCoeffs(x, f):
    diffs = divDiffs(x,f)
    coeffs = []
    for diff in diffs:
        print diff
        coeffs.append(diff[0])
    return coeffs
    
def evalP(x, coeffs, target):
    terms = [1.0] * len(x)
    for i in range(1, len(terms)):
        terms[i] = terms[i-1] * (target - x[i-1])
    return  reduce(lambda a,b: a+b , map(lambda a, b: a*b, coeffs, terms))
"""
def divDiff(x, f):
    if len(x) == 1:
        return f(x[0])
    return  (divDiff(x[1:],f) - divDiff(x[: len(x)-1], f))/ (x[len(x)-1] - x[0])
"""
def divDiffs(x,f):
    diffs = []
    for i in range(0, len(x)):
        diffs.append([None] * (len(x)-i))
    for i, col in enumerate(diffs):
        if i == 0 :
            diffs[i] = map(f,x)
        else:
            for j in range(0, len(col)):
                col[j] = (diffs[i-1][j+1] - diffs[i-1][j])/(x[j+i] - x[j])
            diffs[i] =  col
    return diffs
    
def chebyZeros(num):
    zeros = []
    for k in range(1,num+1):
        zeros.append(cos(pi*((2*k - 1.0)/(2*num))))
    return zeros

arr=[]
for j in  range(0,21):
    arr.append(-1 + j * .1 )
f = lambda x: 1/(1 +( 25*x**2))
target = .985

coeffs = computeCoeffs(arr, f) 
p = evalP(arr, coeffs, target)
print f(target), p

