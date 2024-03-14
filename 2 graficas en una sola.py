import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(0,3*np.pi,200)
y1=np.sin(x1)
x2=np.linspace(0,2*np.pi,200)
y2=np.cos(x2)

fig,(ax1,ax2)= plt.subplots(2,1,figsize=(5,10))
ax1.plot(x1,y1, "s",label="grafica seno",color="red",linewidth=1, linestyle="----") #%% color para las lineas de la grafica linewidth es el grosor de la linea y el otro es para en que forma me la va amostrar 
ax2.plot(x2,y2,"v",label="grafica coseno",color="black",linewidth=3,linestyle=":") 
ax1.set_xlabel("Eje x") 
ax1.set_ylabel("eje y")
ax1.set_title("grafica de la funcion sen(x)")
ax1.legend()#%% para que me diga que linea es que linea y por eso las debo de nombrar
ax1.grid()
ax1.annotate ("local max",xy=(2,1)xytext=(3,1,5),arrowprops= dict(facecolor="blue",shrink=0.5))
ax1.text(3.5,0.50,"hola") #%% ponerle nombe dentro de la grafica 
ax2.set_xlabel("Eje x") 
ax2.set_ylabel("eje y")
ax2.set_title("grafica de la función cos (x)")
ax2.legend()
ax2.grid()#%% para ponerle la cuadricula a la grafica 
plt.show()



#%% para mirar el valor maximo
np.max(y1)
#%% en este caso se agrega la flecha