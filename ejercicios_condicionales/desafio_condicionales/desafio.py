# Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
# Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
# Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.


mts_consumidos = int(input("Ingrese la cantidad de metros cubicos consumidos: "))


tipo_cliente = int(input('''
Ingrese que tipo de cliente es seleccionando el numero que aparece al costado:
Cliente Residencial [1]
Cliente Comercial [2]
Cliente Industrial [3]
'''))

cargo_fijo = 7000
precio_m3 = 200

costo_consumo = mts_consumidos * precio_m3
tarifa_base = cargo_fijo + costo_consumo

bonificacion = 0
recargo = 0
descuento_adicional = 0

if tipo_cliente == "1":
    if mts_consumidos < 30:
        bonificacion = costo_consumo * 0.10
    elif mts_consumidos > 80:
        recargo = costo_consumo * 0.15

elif tipo_cliente == "2":
    if mts_consumidos > 300:
        bonificacion = costo_consumo * 0.12
    elif mts_consumidos > 150:
        bonificacion = costo_consumo * 0.08
    elif mts_consumidos < 50:
        recargo = costo_consumo * 0.05

elif tipo_cliente == "3":
    if mts_consumidos > 1000:
        bonificacion = costo_consumo * 0.30
    elif mts_consumidos > 500:
        bonificacion = costo_consumo * 0.20
    elif mts_consumidos < 200:
        recargo = costo_consumo * 0.10

else:
    print("Tipo de cliente inválido")

subtotal = tarifa_base - bonificacion + recargo

if tipo_cliente == "1" and tarifa_base < 35000:
    descuento_adicional = subtotal * 0.05
    subtotal = subtotal - descuento_adicional

iva = subtotal * 0.21
total_final = subtotal + iva

print(f"Costo del consumo: ${costo_consumo:.2f}")
print(f"Cargo fijo: ${cargo_fijo:.2f}")
print(f"Bonificación: ${bonificacion:.2f}")
print(f"Recargo: ${recargo:.2f}")
print(f"Descuento adicional: ${descuento_adicional:.2f}")
print(f"Subtotal con ajustes: ${subtotal:.2f}")
print(f"IVA (21%): ${iva:.2f}")
print(f"Total final: ${total_final:.2f}")



