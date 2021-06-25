#""" Ejercicio #1 """
class Tarea:
    def descuento(self):
        total_compra=float(input("Ingrese el total de compra: " ))
        descuento = total_compra * 0.15
        cantidad_pagar = total_compra - descuento
        print("""El total de la compra es : {} USD , el descuento recibido es : {} USD , 
        la cantidad final a pagar es : {} USD """.format(total_compra,round(descuento,2),round(cantidad_pagar,2)))


#""" Ejercicio #2 """
    def comision(self):
        salario_base=float(input("Ingrese el salario base del trabajador : "))
        v1 = float(input("Ingrese el valor de la primera venta : "))
        v2 = float(input("Ingrese el valor de la segunda venta : "))
        v3 = float(input("Ingrese el valor de la tercera venta : "))

        total_venta = v1+v2+v3
        comision = total_venta * 0.1
        total_pagar = salario_base + comision

        print("La comision generada por el trabajador a sido de {} , por lo tanto el dinero que recibira como sueldo sera de {}".format(round(comision,2),total_pagar))

ejercicio=Tarea()
# ejercicio.descuento()
# ejercicio.comision()
