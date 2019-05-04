#Edinson Gelvez
#Escriba un código que transforme de coordenadas polares a coordenadas cartesianas.

import math as mt

r=float(input("digite el valor de r"))
angulo=float(input("digite el valor del ángulo"))
x=r*mt.cos(angulo/180*mt.pi)
y=r*mt.sin(angulo/180*mt.pi)
print("el resultado de x es ",x)
print("el resultado de y es ",y)

