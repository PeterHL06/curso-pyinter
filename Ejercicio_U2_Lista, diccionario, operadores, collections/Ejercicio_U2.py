from collections import OrderedDict # Importa subclase para usar OrderedDict
from collections import Counter # Importa una clase para contar

#Datos de prueba
compras  = [
    "Pedro", "Cristina", "Luis", "Carlos", "Pedro", "Cristina","Marta", "Patricia", "Nathalia", "Sofia", "Elena", "Nathalia", "Luis", "Carlos", "Cristina", "Pedro"
    ] # lista de clientes que han comprado en los últimos 30 días
registrados = [
    "Ana", "Carlos", "Marta", "Elena","Luis", "Sofia"
    ] # lista de clientes registrados en la base total

compras_set = set (compras) #set no repite pero no mantiene orden original
registrados_set = set (registrados) #set no repite pero no mantiene orden original

print("=================================================================================")
print("                         LISTA DE CLIENTES QUE COMPRARON                         ")
print("=================================================================================")
print(compras) # Solo impime la lista de compradores original
# print(compras_set)
print("=================================================================================")
print("                          LISTA DE CLIENTES REGISTRADOS                          ")
print("=================================================================================")
print(registrados) # Solo impime la lista de registros original
# print(registrados_set)

# Filtrado de clientes nuevos
print("\n=================================================================================")
print("                              FILTRAR CLIENTES NUEVOS                              ")
print("=================================================================================")
clientes_nuv = compras_set.difference(registrados_set) # Nombres de compras que no aparecen en registrados usando conjuntos
clientes_nuv_opera = compras_set-registrados_set # Diferencia entre compras y registrados usando operador
print("Clientes nuevos: ",clientes_nuv) # Imprime clientes nuevos (únicos), usando diferencia de conjuntos
print("Con operadores de diferencia: ", clientes_nuv_opera) # Imprime clientes nuevos (únicos), usando operador de diferencia

#Eliminación de repetidos y ordenamiento
print("\n=================================================================================")
print("                       ELIMINAR DUPLICADOS Y MANTENER ORDEN                        ")
print("=================================================================================")
#Lista de clientes de compras sin repetir y sin conservar el orden original
compras_unicas = set (compras) # SET elimina duplicados pero no respeta el orden, para ellos se tendría que aplcicar --> sorted(compras_set, key=compras.index)
print("Compras únicas: ",compras_unicas) # Imprime compras unicas sin respetar el orden original

# Ahora con OrdereDirct == Lista de compras sin repetir y conservando el orden original
compras_unic_ORD = list(OrderedDict.fromkeys(compras)) # 
print("Con OrdereDict (no conserva el orden): ", compras_unic_ORD) # Imprime compras 

#Contar cuantas veces se repite cada nombre, cuantas veces compra un cliente
print("\n=================================================================================")
print("                             CONTADOR - CUANTAS VECES                              ")
print("=================================================================================")
clientes_recompran = Counter(compras)
print("Contador: ",clientes_recompran)

print("\n=================================================================================")
print("                          RESUMEN POR CLIENTES FRECUENTES                          ")
print("=================================================================================")
resumen = {
    cliente: f"Ha comprado {contar} veces" for cliente, contar in clientes_recompran.items() if contar > 1
    }
print(resumen)

