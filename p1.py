import numpy
import matplotlib.pyplot as grafico
datos=numpy.loadtxt('sun_AM0.dat')
x=datos[:,0]*10
y=datos[:,1]*100
#grafico.plot(x,y)
#grafico.xlim(0,20000)
#grafico.ylim(0,220)
grafico.loglog(x,y)
grafico.xlabel('longitud de onda ($ \AA $)')
grafico.title('espectro solar logaritmico')
grafico.ylabel('potencia ${ergs/s}/{cm^2} $')
grafico.show()

