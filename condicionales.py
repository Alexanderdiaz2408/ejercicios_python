numero_como_cadena = input("Escribe un numero:")
numero = float(numero_como_cadena)
if numero == 0:
    print("neutro")
elif numero < 0:
    print("negativo")
else: 
    print("psitivo")



x = int(input("¿cual es el primer nuemero?"))
y = int(input("¿cual es el segundo numero?"))
if x>y:
    print("el primer numero es mayor.")
    print("el segundo numero es menor.")
elif x<y:
    print("el segundo numero es mayor.")
    print("el primer nuemr0 es menor.")
else:
    print("es el mismo numero.")


#mayor y menor de tres numeros
lista=[]
cant = int(input("¿cuantos numeros desea ingresar?"))
i=1
while i <= cant:
    n = int(input(f"{i} ingrese un numero:"))
    lista.append(n)
    i+=1

print("numero mayor ",max(lista))
print("numero menor: ",min(lista))


a = float(input("Introduce un número: ") )
b = float(input("Introduce otro número: ") )
opcion = 0
if a>b:
    print("la suma de", a,"+", b,"es", a+b)
else:
    print("la resta de", a,"-", b,"es", a-b)


def main():
    print("DIVISOR DE NÚMEROS")
    dividendo = int(input("Escriba el dividendo: "))
    divisor = int(input("Escriba el divisor: "))
    if divisor == 0:
        print("No se puede dividir por cero.")
    else:
        cociente = dividendo // divisor
        resto = dividendo % divisor
        if resto == 0:
            print(f"La división es exacta. Cociente: {cociente}")
        else:
            print(f"La división no es exacta. Cociente: {cociente} Resto: {resto}")


if _name_ == "_main_":
    main()




año = int(input('Introduce un año: '))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')