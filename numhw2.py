from math import *

def computeCoeffs(x, f):
    coeffs =[]
    for k in xrange(1, len(x)+1):
        coeffs.append(divDiff(x[0:k],f))
    return coeffs
    
def divDiff(x, f):
    if len(x) == 1:
        return f(x[0])
    return  (divDiff(x[1:],f) - divDiff(x[: len(x)-1], f))/ (x[len(x)-1] - x[0])

def chebyZeros(num):
    zeros = []
    for k in range(1,num+1):
        zeros.append(cos(pi*((2*k - 1.0)/(2*num))))
    return zeros

arr=[]
for j in  range(0,21):
    arr.append(-1 + j * .1 )

#print computeCoeffs(arr, lambda x: 1.0/(1 + 25*x**2)) 

