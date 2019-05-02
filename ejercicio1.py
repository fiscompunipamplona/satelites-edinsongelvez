
print("Escriba un código que calcule la posición en J para un objeto en caida libre, luego de un tiempo t y una altura inicial h; ambos valores ingresados por consola.")


h=float(input("digite el valor de h:"))
t=float(input("digite el tiempo que se demora en caer:"))
g=9.8
y=h+0.5*g*t**2
print("la altura es:",y)


T=float(input("digite el periodo:"))
G=6.67e-11
M=5.97e24
R=6371e3
pi=3.1416


r=((G*M*T**2)/(4*pi**2))**1/3-R


print("la altura es:" ,r)

print("Escribe h que estime h a partir de un periodo dado")


T=float(input("digite el periodo:"))
G=6.67e-11
M=5.97e24
R=6371e3
pi=3.1416


r=((G*M*T**2)/(4*pi**2))**1/3-R


print("la altura es:" ,r)

print("estime la altura para un T de un día (geosincrónico), 90min y 45min")
G=6.67e-11
M=5.97E24
R=6371e3
pi=3.1416

T1=float(input("escriba el periodo para un día geosincrónico 90 min"))
T2=float(input("escriba el periodo para un día geosincrónico 40 min"))


r1=(((G*M*T1**2)/(4*pi**2)))**1/3-R
r2=(((G*M*T2**2)/(4*pi**2)))**1/3-R



print("la altura para un día geosincrónico 90 min es:" ,r1*(1e-3))
print("la altura para un día geosincrónico 40 min es:" ,r2*(1e-3))

G=6.67e-11
M=5.97E24
R=6371e3
pi=3.1416

Td=float(input("escriba el periodo (segundos) para un día 24h"))
Ts=float(input("escriba el periodo (segundos) para un día sideral 23.93h"))


rd=(((G*M*Td**2)/(4*pi**2)))**1/3-R
rs=(((G*M*Ts**2)/(4*pi**2)))**1/3-R



print("la altura para un día de 24h es:" ,rd*(1e-3))
print("la altura para un día sideral 23.93h es:" ,rs*(1e-3))




