#Ejercicio de ciclo For
#debes realizar un sumatorio de todos los números desde 0 hasta ese numero (incluido) exceptuando los múltiples de 5 y 7, y almacenarlo en la variable sumatorio.
numero = int(input("Ingrese un valor numerico "))
sumatoria = 0
for n in range(numero):
    if n % 5 != 0 and n % 7 != 0:
        sumatoria += n
print(sumatoria)

    
