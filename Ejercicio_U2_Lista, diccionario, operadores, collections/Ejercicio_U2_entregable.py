from collections import OrderedDict # Importa subclase para usar OrderedDict
from collections import Counter # Importa clase para poder contar las repeteciones

#Datos de prueba
compras  = [
    "Pedro", "Cristina", "Luis", "Carlos", "Pedro", "Cristina","Marta", "Patricia", "Nathalia", "Sofia", "Elena", "Nathalia", "Luis", "Carlos", "Cristina", "Pedro"
    ] # lista de clientes que han comprado en los últimos 30 días
registrados = [
    "Ana", "Carlos", "Marta", "Elena","Luis", "Sofia"
    ] # lista de clientes registrados en la base total

# Filtrado de clientes nuevos
compras_set = set (compras) # Convertir a Set para eliminar duplicados
registrados_set = set (registrados) # Convertir a Set para eliminar duplicados

clientes_nuv = compras_set.difference(registrados_set) # Diferencia con conjuntos: toma elementos que están en compras_set y que no están en registrados_set
clientes_nuv_opera = compras_set-registrados_set # Diferencia con operadores: toma los elementos que están en compras_set y quita los que también están en registrados_set

# Eliminar duplicados y manter orden
#Lista de clientes de compras sin repetir y sin conservar el orden original
compras_unicas = set (compras) # Elimina duplicados, pero sin orden. Para mantener el orden se requiere usar -> sorted(compras_set, key=compras.index)
# Ahora con OrdereDirct == Lista de compras sin repetir y conservando el orden original
compras_unic_ORD = list(OrderedDict.fromkeys(compras)) # OrderedDict elimina duplicados y mantiene el orden original

# Contador
#Contar cuantas veces se repite cada nombre, cuantas veces compra un cliente
clientes_recompran = Counter(compras) # Diccionario  que cuenta el número de veces que un cliente hizo una compra

# Resumen personalizado
# Usando dict comprehension para mensaje final
resumen = {
    cliente: f"Ha comprado {contar} veces" for cliente, contar in clientes_recompran.items() if contar > 1
    # Con .items() obtienes los valores del diccionario clientes_recompran
    # clave = cliente, valor = contar, elemento = cliente, iterable = clientes_recompra, condición = if contar > 1
    }

# Formato Final
print("=================================================================================")
print("                                   FORMATO FINAL                                   ")
print("=================================================================================")
# Impresión de los 3 bloques finales
print("Clientes nuevos no registrados: ", clientes_nuv) # Imprime los clientes nuevos
print("Lista de clientes únicos: ", compras_unic_ORD) # Imprime lista de clientes únicos con OrderedDict
print("Resumen por cliente frecuente (más de 1 compra): ", resumen) # Imprime el resumen de clientes con más de 1 compra
print("=================================================================================")



print("\n\n=================================================================================")
print("                         LISTA DE CLIENTES QUE COMPRARON                         ")
print("=================================================================================")
print(compras) # Imprime la lista de clientes que compraron en los últimos 30 días
# print(compras_set)

print("\n=================================================================================")
print("                          LISTA DE CLIENTES REGISTRADOS                          ")
print("=================================================================================")
print(registrados) # Imprime la lista de clientes frecuentes o registrados
# print(registrados_set)

print("\n\n\n\n=================================================================================")
print("                              FILTRAR CLIENTES NUEVOS                              ")
print("=================================================================================")
print("Clientes nuevos: ",clientes_nuv) # Imprime la lista de clientes nuevos
print("Con operadores de diferencia: ", compras_set-registrados_set) # Diferencia con operadores: toma los elementos que están en compras_set y quita los que también están en registrados_set

print("\n=================================================================================")
print("                       ELIMINAR DUPLICADOS Y MANTENER ORDEN                        ")
print("=================================================================================")
print("Compras únicas: ",compras_unicas) # Imprime lista de compradores únicos
print("Con OrderedDict (conserva el orden): ", compras_unic_ORD) # Imprime compras únicas con OrderedDict para mantener el orden original

print("\n=================================================================================")
print("                             CONTADOR - CUANTAS VECES                              ")
print("=================================================================================")
print("Contador: ",clientes_recompran) # Imprime el diccionario conla key = nombre del cliente y valor = número de veces que compró

print("\n=================================================================================")
print("                          RESUMEN POR CLIENTES FRECUENTES                          ")
print("=================================================================================")
print(resumen) # Imprime el Resumen usando dict comprehension