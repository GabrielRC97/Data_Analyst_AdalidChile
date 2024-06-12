'''
Hola_mundo = "¡Hola Mundo!"

print(Hola_mundo)

usuario = input("Ingrese nombre de usuario => ")
print(f"¡Hola {usuario}!")

horasT = int(input("Ingrese cantidad de horas trabajadas => "))
costeH = int(input("Ingrese el valor de hora trabajada => "))

print(f"La paga que le corresponde es de ${horasT * costeH}")

precio = 1200
descuento = 0.6
kilos_vendidos_da = 5

print(f"Se vendieron {kilos_vendidos_da} Kg de pan del dia anterior, el precio del kilo de pan es de ${precio}, dando un subtotal de {precio * kilos_vendidos_da} con un descuento de {precio*kilos_vendidos_da*descuento} da un total de {precio * kilos_vendidos_da - precio * kilos_vendidos_da * descuento}") 

sueldo = 200000
if sueldo < 200000:
    sueldo = sueldo * 1.15
print (sueldo)

año = 2300
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(f"el año {año} es bisiesto")
        else:
            print(f"el año {año} no es bisiesto")
    else:
        print(f"el año {año} es bisiesto")
else:
    print(f"el año {año} no es bisiesto")

a = int(input("ingrese su primer variable =>"))

b = int(input("ingrese su segunda variable =>"))

if a > b:
    print(b, a)
else:
    print(a,b)
'''
'''
C = 222
I = 10
M = 2
'''
sumatoria = 0
continuar = True
while continuar:
    divisor = int(input("ingresa valor a sumar, en caso de que sea negativo se cerrada la suma => "))
    if divisor >= 0: 
        sumatoria += divisor
    else:
        print(sumatoria)
        continuar = False



