# 1 Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
# 2 Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
# 3 Mostrar la suma de los números desde el 1 hasta el 10.
# 4 Mostrar la suma de los números pares desde el 1 hasta el 10.
# 5 Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
# 6 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
# 7 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
# 8 Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# Anexo:
#  9 Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
# 10 Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

# ejercicio 1
# contador = 0
# while contador < 10 :
#     contador += 1
#     print (contador)

#ejercicio 2
# contador2 = 11
# while contador2 <= 11 and contador2 >= 1:
#     contador2 -= 1
#     print (contador2)

# ejercicio 3
# contador3 = 1
# suma = 0
# while contador3 <= 10: 
#     suma += contador3  
#     contador3 += 1 
#     print (suma)

# # ejercicio 4
# contador4 = 1
# suma2 = 0
# while contador4 <= 10:
#     contador4 += 1
#     if contador4 % 2 == 0:
#         suma2 += contador4 
# print (suma2)

# ejercicio 5
# contador5 = 1
# suma3 = 0
# while contador5 <= 5:
#     numero= int(input("ingrese un numero: "))
#     suma3 += numero
#     promedio = suma3 / 5
#     contador5 += 1
# print(f'''La suma de los numeros ingresados es {suma3}
#         El promedio de los numero ingresados es {promedio}
#     ''')

# # ejercicio 6
# contador6 = 1
# suma4 = 0
# seguir = True

# while seguir == True:
#     numero = int(input("ingrese un numero: "))
#     suma4 += numero 
#     promedio = suma4 / contador6
#     contador6 += 1
#     continuar = input("desea seguir ingresando numeros? (si/no)")
#     if continuar == "no":
#         seguir = False
# print(f'''
# la suma de los numeros ingresados es {suma4}
# el promedio de los numeros ingresados es {promedio}
# ''')


# # ejercicio 7
# contador6 = 1
# suma5 = 0
# seguir = True
# producto = 1

# while seguir == True:
#     numero = int(input("ingrese un numero: "))
#     if numero > 0:
#         suma5 += numero
#     elif numero < 0:
#         producto *= numero
#     continuar = input("desea seguir ingresando numeros? (si/no) ")
#     if continuar == "no":
#         seguir = False

# print(f"la suma de los numeros positivos ingresados es {suma5}")
# print(f"el producto de los numeros negativos ingresados es {producto}")

# # ejercicio 8 

# contador7 = 0
# maximo = 0
# minimo = 0
# while contador7 <= 10:
#     numero = int(input("ingrese un numero: "))

#     if contador7 == 0:
#         maximo = numero
#         minimo = numero
#     else:
#         if numero > maximo:
#             maximo = numero
#         elif numero < minimo:
#             minimo = numero
#     contador7 += 1

# print(f'''
# El maximo es {maximo}
# El minimo es {minimo} 
# ''')

# ejercicio 9 

# contador8 = 1
# continuar = True
# minimo = 0
# suma = 0
# while contador8 < 5 or continuar == True:
#     numero = int(input("ingrese un numero: "))
#     suma += numero
#     contador8 += 1
#     if contador8 >= 5:
#         cortar = input("desea seguir ingresando numeros? (si/no) ")
#         if cortar == "no":
#             continuar = False
# promedio = suma / contador8

# print(f'''
# La suma de los numeros ingresados {suma}
# El promedio de los numeros ingresados es {promedio}
# ''')

ejercicio 10

