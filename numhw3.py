# Andrew Rosen
# performs Romberg Integration
# Usage python numhw3.py

from math import *



def extrapolate(f,a,b, depth):
    R = []
    h = b-a
    for i in range(0, depth):
        R.append([None]*(depth))
    R[0][0] = (h/2.0) * (f(a)+ f(b))
    for n in range(1, depth):
        h = (b-a)/(2.0**n)
        points = [0]
        for k in range(1,int(2**(n-1))):
            point = f(a + (2*k -1)*h) 
            points.append(point)
        #print R
        R[n][0] = .5*R[n-1][0]+h*sum(points)
    for m,col in enumerate(R):
        if m == 0:
            continue
        for n, row in enumerate(R[n]):
            R[n][m] =  (1.0/((4.0**m)-1))*(4**m *R[n][m-1] -R[n-1][m-1])
    print R[depth-1][depth-1]
    
    
#try increasing the last argument to increase accuracy
extrapolate(lambda x: (1/(sqrt(2.0*pi)))*exp(-0.5*x*x)  ,-1,1,5)
