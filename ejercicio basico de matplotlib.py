
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,2*np.pi,200)
#%%va desde 0 hasta 2 * pi , con doscientos puntos 
#%% es unn vector 
#%% para ver la cantidad de puntos
y=np.sin(x)
#%% seno va a multiplicar el valor de x y se me convierte en y
fig,ax=plt.subplots() #%% crea un objeto llamado fig y ax a los que se le van asignar los ejes 
ax.plot(x,y,label="grafica seno") 
        #%% va a graficar x, y, es decir asignar los ejes
plt.show()#%% para mostrar la figura 
ax.legend()


