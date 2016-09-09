import numpy
import scipy.constants


datos=numpy.loadtxt('sun_AM0.dat')
x=datos[:,0]*10
y=datos[:,1]*100

Sum=0
for i in range(len(x)-1):
    Sum=Sum+(y[i+1]+y[i])*(x[i+1]-x[i])/2
Totalpower=Sum*4*scipy.constants.pi*scipy.constants.astronomical_unit*scipy.constants.astronomical_unit*10000
print Totalpower