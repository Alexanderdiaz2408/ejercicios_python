print ("programa para calcular el area de un triangulo")
base= float(input("escriba la base del triangulo :"))
altura= float(input("escriba la altura del triangulo:"))
area = base * altura/2
print (f"el area del triangulo es: {area}")

print ("programa para sumar dos numero ")
numero1= float(input("escriba un numero:"))
numero2= float(input("escriba un segundo numero:"))
suma = numero1 + numero2
print (f"la suma de los dos numeros es: {suma}") 


print ("programa para vizualizar un numero en cuadrado")
numero= float(input("escriba un numero :"))
cuadrado = numero * numero
print (f"el cuadrado del numero es:{cuadrado}")


print ("programa para convertir de euros a dolares ")
euros= float(input("escriba la cantidad de euros :"))
conversion = euros * 1.08
print (f"dolares: {conversion}")


print ("programa para area y perimetro de un cuadrado")
lado= float(input("escriba el numero de un lado del cuadrado :"))
areacuadrado= lado * lado
perimetrocuadrado= lado + lado + lado + lado
print (f"el area del cuadrado es: {perimetrocuadrado}")
print (f"el perimetro del cuadrado es:{perimetrocuadrado}")


print ("programa para hallar el area y el volumen de cilindro")
radiocilindro= float(input("escriba el radio del cilindro :"))
alturacilindro = float(input("escriba la altura del cilindro :"))
volumencilindro= 3.141592 * (radiocilindro * radiocilindro) * alturacilindro
areacilindro= 2.0 * 3.141592 * radiocilindro * (radiocilindro + altura)
print (f"valor de areacilindro: {areacilindro}")
print (f"valor de volumen: {volumencilindro}")


print ("programa para el area de un ciculo y  la longitud")
radiocirculo = float(input("escriba el radio de un circulo :"))
longitud= 2 * 3.1416 * radiocirculo
areabase= 3.1416 * (radiocirculo * radiocirculo)
print (f"el area del cuadrado es: {longitud}")
print (f"el perimetro del cuadrado es:{areabase}")


print ("programa calcular el promedio de 3 numeros")
num1= float (input("escriba el primer numero:"))
num2= float (input("escriba el segundo numero:"))
num3= float (input("escriba el tercer numero:"))
promedio = (num1 + num2 + num3) /3
print (f"el promedio es {promedio} ")