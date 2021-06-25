
#""" Ejercicio 1 Estructuras selectivas simples """
class Tarea:
    def aprobar(self):

        calif = float(input("Ingrese la calificacion del estudiante : "))

        if calif >= 7 :
            print("Felicidades usted a aprobado con una calificacion de {}".format(calif))


#""" Ejercicio 2 Estructuras selectivas dobles """

        calif = float(input("Ingrese la calificacion del estudiante : "))

        if calif >= 7 :
            print("Felicidades usted a aprobado con una calificacion de {}".format(calif))
        else:
            print("Usted a reprobado")

# """ Ejercicio 3 """

    def aumento(self):

        sueldo_base = float(input("Ingrese el sueldo del trabajador : "))

        if sueldo_base <= 600:
            aumento = sueldo_base * 0.10
            nuevo_sueldo = sueldo_base + aumento
        else:
            nuevo_sueldo=sueldo_base
        print("El sueldo que el trabajador recibira es : {} USD".format(nuevo_sueldo))


#""" Ejercicio 4 Estructuras selectivas compuestas """

    def pago_hora(self):
        horas = int(input("Ingrese la cantidad de horas trabajadas : "))
        pago_hora= float(input("Ingrese el valor que se paga por hora trabajada : "))

        if horas > 40:
            horas_extras = horas - 40
            if horas_extras > 8:
                exceden_extras = horas_extras-8
                pago_hora_extra = ((pago_hora*2)*8)+((pago_hora*3)*horas_extras)
            else:
                pago_hora_extra = pago_hora*(horas_extras*2)
            pago_total = (pago_hora*40)+pago_hora_extra
        else:
            pago_total=pago_hora*horas
        print("Usted a trabajado {} horas , por lo tanto recibira el total de  {}".format(horas,pago_total))

#""" Ejercicio 5 """
    def mayor(self):
        n1 = float(input("Ingrese el primer numero : "))
        n2 = float(input("Ingrese el segundo numero : "))
        n3 = float(input("Ingrese el tercer numero : "))

        if n1 > n2 and n1 > n3:
            mayor = n1
        elif  n2>n3:
            mayor = n2
        else:
            mayor = n3
        print("De los 3 numeros ingresados {} , {} , {} el numero mayor es  {}".format(n1,n2,n3,mayor))

#""" Ejercicio 6 Estructuras selectivas múltiples """
    def seleccion(self):

        v= int(input("Ingrese un valor cualquiera: "))
        numero=int(input("Ingrese un numero del 1 al 3: "))

        if numero == 1:
            resp = 100 * v
        if numero ==2:
            resp = 100 ** v
        if numero == 3:
            resp = 100 / v
        if numero > 3 or numero < 1:
            resp = "error"
        print(resp)

#""" Ejercicio 7  Expresiones lógicas """
    def comprobar_calif(self):
        calif1 = float(input("Ingrese la calificacion obtenida en el primer examen: "))
        calif2 = float(input("Ingrese la calificacion obtenida en el segundo examen: "))

        if calif1 >= 80 and calif2 >=80:
            print("Usted a aprobado")
        else:
            print("Usted a reprobado")

    #""" Ejercicio 8  """  

        calif1 = float(input("Ingrese la calificacion obtenida en el primer examen: "))
        calif2 = float(input("Ingrese la calificacion obtenida en el segundo examen: "))

        if calif1 >= 90 or calif2 >=90:
            print("Usted a aprobado")
        else:
            print("Usted a reprobado")

ejercicios=Tarea()
# ejercicios.aprobar()
# ejercicios.aumento()
# ejercicios.pago_hora()
# ejercicios.mayor()
# ejercicios.seleccion()
# ejercicios.comprobar_calif
