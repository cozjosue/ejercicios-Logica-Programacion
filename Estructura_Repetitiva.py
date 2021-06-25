#""" Ejercicio 1 Estructura FOR """
class Tarea:
    def suma_cuadrados(self):
        suma=0
        for i in range(1,101):
            suma = suma+(i*i)
        print("La suma de los cuadrados de los primeros 100 enteros es : {}".format(suma))

        #""" Ejercicio 2 Estructura While """
    def primeros_primos(self):
        i = 1
        while i <= 100:
            print ("presentacion de los 100 primeros numeros: ",i)
            i+=1

#""" Ejercicio 3 """
    def suma_multiplicacion(self):
        suma = 0
        producto = 1
        respuesta = input("Desea continuar? (Presione N para salir) ")

        while respuesta.lower() != "n":

            num = int(input("Ingrese un numero entero : "))
            suma = suma + num
            producto = producto * num
            respuesta = input("Desea continuar? (Presione N para salir) ")
            
        print("El total de la suma es : {} y el total de la multiplicacion : {}".format(suma,producto))


#""" Ejercicio 4 """
    def suma_multi(self):
        suma = 0
        producto = 1
        num = int(input("Ingrese un numero entero (Digite -1 para salir): "))

        while num != -1:
            suma = suma + num
            producto = producto * num
            num = int(input("Ingrese un numero entero (Digite -1 para salir): "))
            
        print("El total de la suma es : {} y el total de la multiplicacion : {}".format(suma,producto))


#""" Ejercicio 5 """
    def num_primo(self):

        num = int(input("Ingrese un numero entero : "))
        primo = True
        divisor = 2

        while (divisor < num ) and primo == True:
            res = num % divisor
            if res == 0:
                primo = False
            divisor +=1
        if primo == True:
            print("El numero {} es un numero primo".format(num))
        else:
            print("El numero {} no es un numero primo".format(num))

#""" Ejercicio 6 """
    def factorial(self):
        num = int(input("Ingrese el numero de veces a repetir el bucle : "))

        i=1
        for i in range(num):
            n = int(input("Ingrese el numero a calcular el factorial : "))
            factorial=1
            for j in range(n):
                factorial=factorial*(j+1)
            print("El factorial del numero {} , es : {}".format(n,factorial))

ejercicio=Tarea()
# ejercicio.suma_cuadrados()
# ejercicio.primeros_primos()
# ejercicio.suma_multiplicacion()
# ejercicio.suma_multi()
# ejercicio.num_primo()
# ejercicio.factorial()