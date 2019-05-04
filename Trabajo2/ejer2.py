#Edinson Gelvez
#Escriba un código que calcule la secuancia de Fibonacci hasta 1000.

f1=1
f2=2
f=0
while f <= 1000:

    f=f1+f2
    f1=f2
    f2=f2+1
    print(f)


