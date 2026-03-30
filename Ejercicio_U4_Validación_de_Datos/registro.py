# Ejercicio validación de usuarios

from email_validator import validate_email as v_email # Importa la función para verificar si un correo electrónico tiene un formato válido
from email_validator import EmailNotValidError 
import logging # # Importa el módulo, mensajes de información, advertencias y errores que ocurren.

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s") # Se configura el mensaje para las advertencias


def validar_datos(): # Definición de función
  
  print("\n===== INICIANDO =====")
  logging.info("Validando datos...\n") # Logging para validar datos

  while True: # ciclo para solicitar nombre hsta que sea valido
    try:
      Nombre = input("Ingresa tu nombre: ") # Solicitar dato de nombre

      if Nombre.strip() == "": # Validar si el nombre es vacio y elimina espacios con strip()
        raise TypeError("Entrada invalida, el nombre no puede estar vacío") # Error si el nombre es vacío
      for caracter in Nombre: # Ciclo para validar cada carácter del nombre
        if caracter.isdigit(): # Con isdigit() se valida si el nombre no tiene números
          raise ValueError("El nombre no debe contener números") # Mensaje de error si el nombre tiene número

    except ValueError as e: 
      logging.warning(f"Error en nombre: {e}") # Regisitro de advertencia
      print(f"{e}, favor de revisar") # Imprime error de tipo ValueError para el usuario
    except TypeError:
      logging.warning(f"Error en nombre: ")
      print("Hay algún error en el nombre, revisa por favor") # Imprime error de tipo TypeError para el usuario
    except Exception as e:
      logging.warning(f"Error en nombre: {e}") # Regisitro de advertencia
      print(type(e).__name__) # Imprime error de otro tipo para el usuario
    else: # Rompe el ciclo while si no hay errores
      break

  while True: # ciclo para solicitar edad hasta que sea valida
    try:
      Edad = int(input("Ahora ingresa tu edad: ")) # Solicitar el dato de edad, lo convierte a entero con int
      if Edad < 0: # Validar si número menor a 0
        print("---- Error: Ingrese un valor diferente ----") # Mensaje de error si numero menor a 0
        validar_datos() # Llama a la función validar, reinicia el proceso de captura
        if Edad.strip() == "": # Validar si el edad es vacia y elimina espacios con strip()
          raise ValueError("Entrada invalida")
      
      validar_edad = 1/Edad # Forza la validad en división con cero
      
    except ZeroDivisionError: # Excepción por división con cero -- Error
      logging.warning(f"Error en edad: ") # Regisitro de advertencia
      print("---- La edad no puede ser 0 ----")
    except ValueError:
      logging.warning(f"Error en edad: ") # Regisitro de advertencia
      print("---- Ingresa un numero por favor, la edad no puede estar vacía ----")
    except Exception as e:
      logging.warning(f"Error en edad: {e}")
      print(type(e).__name__) # Imprime error de otro tipo para el usuario
    else: # Rompe el ciclo while si no hay errores
      break

  while True: # ciclo para solicitar correo hsta que sea valido
    try:
      Correo = input("Ingresa tu correo: ") # Solicitar dato del correo
      v_email(Correo) # Valida el correo validate_email
    except EmailNotValidError: # Excepción si el dato ingresado no tiene un @
      logging.warning(f"Error en el correo: un correo debe tener el signo @") # Regisitro de advertencia
      print("El correo ingresado es invalido, revisa por favor")
    except Exception as e:
      logging.error(f"Error en el correo: {e}") # Regisitro de advertencia
      print(type(e).__name__) # Imprime error de otro tipo para el usuario
    else: # Rompe el ciclo while si no hay errores
      break

    finally:
        logging.info("---- Registro finalizado ----") # Logging para finalizar la validación

# Sección para imprimir en pantalla los DATOS CAPTURADOS
  print("\n========== DATOS CAPTURADOS ==========\n")
  print("Nombre del usuario: ", Nombre)
  print(f"Edad del usuario: {Edad} años")
  print("Correo del usuario: ", Correo)
  print("\n")

def probar_validaciones(): # Define la función para ejecutar validar_datos
  validar_datos() # Llama a la función validar

probar_validaciones() # Ejecuta la función de probar_validaciones