# Ejercicio_U1_LambdaDecoradoresGeneradores
from functools import reduce
import time

# Decorador personalizado
def auditar_funcion(func):
  cont = 0 # Iniciar contador

  def decorador(*args, **kwargs):
    nonlocal cont # Definir que no es una variable local
    cont += 1 # Incrementa el contador
    inicio = time.time() # Mide tiempo de inicio
    
    print("Se ejecuto la funcion: ", func.__name__) # fun.__name__ para poner nombre de la función
    print("Se ejecuto la funcion: ", cont)
    
    fun_orig = func(*args, **kwargs)

    fin = time.time() # Mide tiempo final
    print(f"Tiempo de ejecucion: {fin - inicio:.7f} segundos")

    return fun_orig
  return decorador


# Lista de Temperaturas --> Datos Sensores
datos_temp = [("CDMX", 26),
              ("MORELIA", 24),
              ("QUERETARO", 33),
              ("MONTERREY", 36),
              ("CANCUN", 35),
              ("LEON", 28),
              ("GUADALAJARA", 31),
              ("CELAYA", 21),
              ("SAN LUIS", 30)]

#Funcion generadora
def leer_temperaturas():
  for ciudad, temp in datos_temp:
    yield ciudad, temp

print("\nLista de Datos de Sensores - Ciudades y Temperaturas", list(leer_temperaturas()), "\n")

# Funcion para filtrar
def may_30():
  may_30c = lambda x: x [1] >= 30 # Ciudades mayores o iguales a 30°C
  return list(filter(may_30c, leer_temperaturas()))

@auditar_funcion # Llamas al decorador personalizado
def procesador_alertas():
  ciudades_calientes = may_30() # Asignación ciudades calientes
  print("\nLas Ciudades calientes son: ", ciudades_calientes, "\n")

  # Transformacion con map() y Lambda
  alerta_calor = lambda ciudad_caliente: ("Alerta de calor en", ciudad_caliente[0], "con temperatura de", ciudad_caliente[1])
  Alerta = list(map(alerta_calor, ciudades_calientes))
  print(Alerta)

  # Ordenamiento los datos filtrados, orden descendente
  ordenar_por_temp = lambda temp: temp[1]
  ciudad_ord = list(sorted(ciudades_calientes, key=ordenar_por_temp, reverse=True))
  print("\nLas ciudades con alerta son", ciudad_ord)

  #Promedio de temperatura de alerta
  tam= len(ciudad_ord)
  # print(tam)
  valores = list (map(lambda x: x[1], ciudad_ord))
  # print(valores)
  sum = reduce(lambda x, y: x + y, valores)
  # print(sum)
  prom = sum / tam
  print(f"Temperatura promedio de alertas: {prom:.2f}°C","\n")

procesador_alertas()