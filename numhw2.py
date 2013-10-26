def computeCoeffs(x, f):
    pass
    
    
def divDiff(x, f):
    if len(x) == 1:
        return f(x[0])
    return  (divDiff(x[1:],f) - divDiff(x[: len(x)-1], f))/ (x[len(x)-1] - x[0])


arr = [1.0,2.0,3.0]

