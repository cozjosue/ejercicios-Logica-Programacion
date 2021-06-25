#""" Ejercicio 1 Arreglos en una dimensión """
class Tarea:
    def vectores(self):
        A=[]
        B=[]
        numeros = [2,-5,4,5,-10,3,-5,87,1,-1,3,7,-8,-9,10,-10,4,7,-80,10]

        for i in numeros:
            if i>0:
                B.append(i)
            else:
                A.append(i)

        print("El vector con los numeros negativos es : ",A)
        print("El vector con los numeros positivos es : ",B)



#""" Ejercicio 2 Arreglos en dos dimensiones """

    def calif_matriz(self):
        examenes= 6
        alumnos=30

        matriz=[]
        for i in range(alumnos):
            matriz.append([])
            for j in range(examenes):
                nota = int(input("Ingrese la nota para el alumno {} en el examen {}: ".format(i+1,j+1)))
                matriz[i].append(nota)

        for alu in matriz:
            print("[",end="")
            for elemento in alu:
                print("{:8.2f}".format(elemento),end="")
            print("]")

        c=0
        promediosex=[]
        for j in range(examenes):
            suma=0
            for i in range(alumnos):
                suma=suma+matriz[i][j]
            prom=suma/alumnos
            c+=1
            print("El examen {} obtuvo un promedio de {}".format(c,round(prom,3)))    
            promediosex.append(prom)

        print()

        cont=0
        for i in range(alumnos):
            suma=0
            for j in range(examenes):
                suma = suma + matriz[i][j]
            cont+=1
            prom = suma / examenes
            print("El alumno{} obtuvo un promedio de  {}".format(cont,round(prom,3)))

        ex = 1
        cont = 1
        promayor = promediosex[0]
        for i in promediosex:
            if i > promayor:
                promayor = i
                ex =  cont
            cont+=1
        print("El examen con mayor promedio es el {} con un promedio de {}".format(ex,promayor))

ejercicio=Tarea()
# ejercicio.vectores()
# ejercicio.calif_matriz()