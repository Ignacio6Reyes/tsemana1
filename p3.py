import numpy
import matplotlib.pyplot as grafico
import scipy.constants
import math


def exptan(x,n): #expansion de la exponencial a orden n
    e=0
    for i in range(1, n): e= e+ math.pow( math.tan( x) , i)/ math.factorial( i)
    return e

def integ(x,n): #valor del integrando en [0,pi/2]
    uval=math.pow(math.tan(x),3)
    dval=exptan(x,n)
    mval = uval/dval
    tval = mval / math.pow(math.cos(x),2)
    return tval

def intnum(step,n): #calculo integral para expansion orden n
    Sum=0
    step = 0.01
    for i in numpy.arange(step, (math.pi) / 2 - step, step):
        trp = (integ(i + step, n) + integ(i, n)) * step / 2
        Sum = Sum + trp
    return Sum


datos=numpy.loadtxt('sun_AM0.dat')
x=datos[:,0]*10
y=datos[:,1]*100

Sum2=0
for i in range(len(x)-1):
    Sum2=Sum2+(y[i+1]+y[i])*(x[i+1]-x[i])/2
Totalpower=Sum2*4*scipy.constants.pi*scipy.constants.astronomical_unit*scipy.constants.astronomical_unit*10000

res =math.pow(math.pi,4) / 15  # resultado analitico de la integral
n=12         # orden al cual se aproxima la exponencial
Sum=0
step=0.01   #dy
y=[]
for i in numpy.arange(step, (math.pi)/2-step, step):
    trp= (integ(i+step, n)+integ(i, n))*step/2
    y.append(trp)
    Sum = Sum + trp
print "resultado integral="+str(Sum), "diferencia="+str(Sum-res)
C0=scipy.constants.k*5778/scipy.constants.h
C1=(2*math.pi*scipy.constants.h/math.pow(scipy.constants.speed_of_light,2))*math.pow(C0,4)
Areapower=C1*10e7*Sum
print 'potencia por area='+str(Areapower)
Rsun= math.sqrt(Totalpower/(4*math.pi*Areapower))
print 'estimacion radio solar ='+str(Rsun)
grafico.plot(numpy.arange(len(y))*(step),y)
grafico.title('Funcion integrada para expansion orden 12')
grafico.xlabel('y=arctan(x) ; x='+ r'$\frac{h c}{\lambda k_B T}$')
grafico.ylabel('valor integrando')
grafico.show()