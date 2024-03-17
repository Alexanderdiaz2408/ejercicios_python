print("multiplos") 
a = 3
while a < 101:
    print(a)
    a += 3


print("impares")
x = 1
while x <= 100:
     x +=1
     if x % 2 == 1:
        print(x)
    

print("pares")
p = 2
while p < 101:
    print(p)
    p += 2


print("suma de cuadrados")
x = 1
suma = 0 
while x <= 100:
    suma = suma + x
    x += 1
print("la suma de los cuadrados es:", {suma})


print("suma de los primeros numeros")
x = 1 
suma = 0
while x <= 100:
    suma = suma + x 
    x += 1 
print("la suma de los primeros numeros es:", suma)



print(" suma de de todos los numeros")
n = 1
suma = 0 
while n != 0:
    n = int(input("ingresa un numero:"))
    suma += n
print(f"la suma de los numeros es: {suma}")

