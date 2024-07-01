'''
my_list = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]

############ 1 ###############

#A

try:
    print(my_list.index(85.7))
except ValueError:
    print("85.7 no se encuentra en la lista")

try:
    print(my_list.index(True))
except ValueError:
    print("True no se encuentra en la lista")

try:
    print(my_list.index([(0,0,1)]))
except ValueError:
    print("[(0,0,1)] no se encuentra en la lista")

try:
    print(my_list.index([1,2,3]))
except ValueError:
    print("[1,2,3] no se encuentra en la lista")

try:
    print(my_list.index(0))
except ValueError:
    print("0 no se encuentra en la lista")

try:
    print(my_list.index([True]))
except ValueError:
    print("[True] no se encuentra en la lista")

try:
    print(my_list.index(85))
except ValueError:
    print("85 no se encuentra en la lista")

try:
    print(my_list.index("a"))
except ValueError:
    print('"a" no se encuentra en la lista')




#B

print(my_list.index((0,0,1)))

#C

my_list.pop()
print(my_list)

#D

print(my_list.count("a"))

############ 2 ###############

def esPalindromo (string):
    string = string.replace(" ","").lower()
    if string == string[::-1]:
        return "Es palindromo"
    else:
        return "No es un palindromo"

print(esPalindromo(str(input("REVISA SI ES UN PALINDROMO => "))))

############ 3 ###############

my_list = [1,2,3,4,5,6,7,8,9,10]
my_list.reverse()
print(my_list)

############ 4 ###############

matematicas = int(input("Que nota has sacado en Matemáticas => "))
fisica = int(input("Que nota has sacado en Física => "))
quimica = int(input("Que nota has sacado en Química => "))
historia = int(input("Que nota has sacado en Historia => "))
lengua = int(input("Que nota has sacado en Lengua => "))

print(f"En matemáticas has sacado {matematicas}, en física has sacado {fisica}, en quimica has sacado {quimica}, en historia has sacado {historia}, y en lengua has sacado {lengua}")

############ 5 ###############

matriz_a = [[1,2,3],[4,5,6]]
matriz_b = [[-1,0],[0,1],[1,1]]

print(matriz_a, matriz_b)

############ 6 ###############

my_dict = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}

divisa = input("ingrese divisa a utilizar =>")
if my_dict.get(divisa) is not None:
    print(my_dict[divisa])
else:
    print("Divisa no se encuentra")
'''

############ 7 ###############

import datetime
import calendar

fecha = input("ingrese fecha en formato dd/mm/aaaa =>")
try:
    fecha = datetime.datetime.strptime(fecha, '%d/%m/%Y').date()
    print(f"{fecha.day} de {calendar.month_name[fecha.month]} de {fecha.year}")
except ValueError:
    print("Formato de fecha incorrecto. Debe ser dd/mm/aaaa.")


