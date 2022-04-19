#Ejercicio para encontrar la nota mas baja y la nota mas alta de una lista de calificaciones 


Calificacion= int(input("78, 65, 89, 86, 55, 91, 64, 89"))
Vec=[vars]
n=0

for i in range (1, Calificacion+1):
    nota=int(input("Calificacion: "))
    n=n+nota
    Vec.append(nota)

    promedio=n/len(Vec)

    npromedio=0
    for j in Vec:
        if j>promedio:
            npromedio=npromedio+1

    aprobado=0
    for h in Vec:
        if h>7:
            aprobado=aprobado+1

    reprobado=0
    for k in Vec:
        if k<8:
            reprobado=reprobado+1

print("Max nota:", max(Vec))
print("Min nota:", min(Vec))
print("promedio:", promedio)
print("superior al promedio:", npromedio)
print("aprobados:", aprobado)
print("desaprobado:", reprobado)