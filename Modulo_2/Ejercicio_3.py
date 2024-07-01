'''
ancho = int(input("digite anchura del rectangulo => "))
alto = int(input("digite altura del rectangulo => "))

for i in range (0 , alto):
    print(ancho * '*')


año1 = int(input('ingrese primer año => '))
año2 = int(input('ingrese segundo año => '))
lista = []

if año1 < año2:
    for i in range (año1,año2 + 1):    
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    lista.append(i)    
            else:
                lista.append(i)
else:                
    for i in range (año2,año1 + 1):    
        if i % 4 == 0:
            if i % 100 == 0:
                if i % 400 == 0:
                    lista.append(i)    
            else:
                lista.append(i)
print(lista)


def mult_10 (n):
    return n*10

print(mult_10(int(input("digite numero para multiplicar por 10 => "))))

def espar (n):
    if n % 2 == 0:
        return True
    else:
        return False

print (espar(int(input("digite numero para saber si es par => "))))
'''


