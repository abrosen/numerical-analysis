# Andrew Rosen
# performs Romberg Integration
# Usage python numhw3.py

from math import *



def extrapolate(f,a,b, depth):
    R = []
    for i in range(0, depth):
        R.append([None]*(depth))
    R[0][0] = ((b-a)*.5)*(f(a)+ f(b))
    for n in range(1, depth):
        h_n = (b-a)/(2.0**(n))
        points = [0]
        for k in range(1,int(2**(n-1)) +1):
            point = f(a + (2*k -1)*h_n) 
            points.append(point)
        R[n][0] = .5*R[n-1][0]+h_n*sum(points)
    for m in range(1,depth):
        for n in range(m,depth):
            #R[n][m] =  (1.0/((4.0**m)-1))*(4**m *R[n][m-1] -R[n-1][m-1])
            R[n][m] = R[n][m-1] + (1.0/((4.0**m) - 1.0)) * (R[n][m-1] - R[n-1][m-1]) 
    #for row in R:
    #    print row
    print R[depth-2][depth-2]
    
    
#try increasing the last argument to increase accuracy
extrapolate(lambda x: (1.0/(sqrt(2.0*pi)))*exp(-0.5*x*x)  ,-1.0,1.0,5)
