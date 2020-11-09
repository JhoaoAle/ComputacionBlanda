import numpy as np
import skfuzzy as sk 
import matplotlib  as plt

#==============================================================================================

#FUNCION DE MEMBRESIA TRIANGULAR

#Ejemplo 1
#'''
#Define un array para manejar el factor de calidad en un restaurante
x = np.arrange (0,11,1)

#Define un array para la función miembrod e tipo triangular
calidad = sk.trimf (x,[0,0,0])

#Grafica la función de membresía
plt-figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''


#Ejemplo 2
#'''

#Define un array para manejar el factor de calidad en un restaurante
x = np.arrange (0,11,1)

#Define un array para la función miembrod e tipo triangular
calidad = sk.trimf (x,[0,0,5])

#Grafica la función de membresía
plt-figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''


#Ejemplo 3
#'''

#Define un array para manejar el factor de calidad en un restaurante
x = np.arrange (0,11,1)

#Define un array para la función miembrod e tipo triangular
calidad = sk.trimf (x,[0,5,10])

#Grafica la función de membresía
plt-figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''


#Ejemplo 4
#'''

#Define un array para manejar el factor de calidad en un restaurante
x = np.arrange (0,11,1)

#Define un array para la función miembrod e tipo triangular
calidad = sk.trimf (x,[9,9,10])

#Grafica la función de membresía
plt-figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''


#Ejemplo 5
#'''

#Define un array para manejar el factor de calidad en un restaurante
x = np.arrange (0,11,1)

#Define un array para la función miembrod e tipo triangular
calidad = sk.trimf (x,[10,10,10])

#Grafica la función de membresía
plt-figure()
plt.plot(x, calidad, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''

#==============================================================================================

#FUNCION DE MEMBRESIA TRAPEZOIDAL

#Ejemplo 1
#'''

#Define la variable independiente
x = np.arrange (0,11,1)

#Define la variable dependiente trapezoidal de membresia
vd_trapezoidal = sk.trapmf(x, [0,0,5,5])

#Grafica la funcion de membresia
plt-figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''


#Ejemplo 2
#'''

#Define la variable independiente
x = np.arrange (0,11,1)

#Define la variable dependiente trapezoidal de membresia
vd_trapezoidal = sk.trapmf(x, [0,3,5,8])

#Grafica la funcion de membresia
plt-figure()
plt.plot(x, vd_trapezoidal, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#'''

#==============================================================================================

#FUNCION GAUSSIANA

#Ejemplo 1
#'''

#Define la variable independiente
x = np.arrange (0,11,0.1)

#Define la variable dependiente trapezoidal de membresia
vd_gaussiana = sk.gaussmf(x, np.mean(x), np.std(x))

#Grafica la funcion de membresia
plt-figure()
plt.plot(x, vd_gaussiana, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#''' 

#==============================================================================================

#CAMPANA GAUSSIANA

#Ejemplo 1
#'''

#Define la variable independiente
x = np.arrange (0,11,0.6)

#Define la variable dependiente trapezoidal de membresia
vd_gaussiana_bell = sk.gbellmf(x,2,3,5)

#Grafica la funcion de membresia
plt-figure()
plt.plot(x, vd_gaussiana_bell, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#''' 

#==============================================================================================

#FUNCION SIGMOIDE

#Ejemplo 1
#'''

#Define la variable independiente
x = np.arrange (-11,11,1)

#Define la variable dependiente trapezoidal de membresia
vd_sigmoide= sk.sigmf(x,0,1)

#Grafica la funcion de membresia
plt-figure()
plt.plot(x, vd_sigmoide, 'b', linewidth=1.5, label='Servicio')

plt.title('Calidad de servicio Restaurante')
plt.ylabel('Membresía')
plt.xlabel('Nivel de servicio')
plt.legend(loc='center right',bbox_to_anchor=(1.25,0.5), ncol=1, fancybox=True, shadow=true)
#''' 

#==============================================================================================

#APLICACION FUTBOL

#Paquetes requeridos

#'''

import matplotlib.pyplot as plt

%matplotlib inline

#Definiendo los rangos de velocidad de O a 80
x = np.arange(30, 80, 0.1)

#Definiendo las funciones miembro triangulares taller
lento = fuzz.trimf(x, (30, 30, 50])
medio = fuzz.trimf(x, [30, 50, 70])
medio_rapido = fuzz.trimf(x, [50, 60, 80])
rapido = fuzz.trimf(x, (60, 80, 80])

#Dibujando las funciones de membresia

plt.figure()
plt.plot(x, rapido, 'b', linewidth=1.5, label='Rápido')
plt.plot(x, medio rapido, 'k', linewidth=1.5, label='Medio-Rápido')
plt.plot(x, medio, 'm', linewidth=1.5, label='Medio')
plt.plot(x, lento, 'r', linewidth=1.5, label='Lento')
plt.title('Penalti Difuso')

plt.ylabel('Membresía')

plt.xlabel("Velocidad (Kilometros Por Hora)")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)

#'''

#==============================================================================================

#Union

import skfuzzy as sk
import matplotlib.pyplot as plt

#Definición de arreglo para calidad
x = np.arange(0, 11, 1)

#Definiendo funciones triangulares taller
bajo = sk.trimf(x, (0, 0, 5))
medio ? sk.trimf(x, (0, 5, 10])

#Graficación
plt.figure()
plt.plot(x, bajo, 'b', linewidth=1.5, label-'Bajo')
plt.plot(x, medio, 'r', linewidth=1.5, label='Medio')

#Ajustes gráfico

plt.title('Función Unión (máximo) ')
plt.ylabel('Membresia')

plt.xlabel("Velocidad (Kilometros Por Hora)")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1, fancybox=True, shadow=True)

plt.axvline(x=0, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=1, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=2, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=3, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=4, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=5, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=6, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=7, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=8, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=9, ymin=0, ymax=10, color="g", linestyle='-.')
plt.axvline(x=10, ymin=0, ymax=10, color="g", linestyle='-.')

plt.plot(0, 1, marker='o', markersize=10, color='g')
plt.plot(1, 0.8, marker='o', markersize=10, color='g')
plt.plot(2, 0.6, marker='o', markersize=10, color='g')
plt.plot(3, 0.6, marker='o', markersize=10, color='g')
plt.plot(4, 0.8, marker='o', markersize=10, color='g')
plt.plot(5, 1, marker='o', markersize=10, color='g')

plt.plot(6, 0.8, marker='o', markersize=10, color='g')
plt.plot(7, 0.6, marker='o', markersize=10, color='g')
plt.plot(8, 0.4, marker='o', markersize=10, color='g')
plt.plot(9, 0.2, marker='o', markersize=10, color='g')
plt.plot(10, 0, marker='o', markersize=10, color='g')

plt.show()

#Encontrando el máximo (Fuzzy OR)

sk.fuzzy_or(x, bajo, x, medio)
