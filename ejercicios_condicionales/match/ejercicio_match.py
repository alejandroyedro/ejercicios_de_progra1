# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

#no tengo la enie en el teclado, tuve que usar el teclado de windows
print('''
Las opciones son 

invierno
verano
otoño
primavera 
''')

estacion = input("ingrese la estacion del año en miniscula, porfavor : ")
match estacion:
    case 'invierno':
        print('Solo se viaja a Bariloche')
    case 'verano':
        print('Solo se viaja a Mar de plata y Cataratas')
    case 'otonio'|'otoño':
        print('Se viaja a todos los lugares') 
    case 'primavera':
        print('Se viaja a todos los lugares menos Bariloche')
    case _:
        print('No se viaja a ningun lado')

