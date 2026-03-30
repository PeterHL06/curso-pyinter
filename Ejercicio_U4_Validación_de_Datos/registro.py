# Ejercicio validación de usuarios

from email_validator import validate_email as v_email
from email_validator import EmailNotValidError
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def validar_datos():
  
  print("\n===== INICIANDO =====")
  logging.info("Validando datos...\n")

  while True:
    try:
      Nombre = input("Ingresa tu nombre: ")

      if Nombre.strip() == "":
        raise TypeError("Entrada invalida, el nombre no puede estar vacío")
      for caracter in Nombre:
        if caracter.isdigit():
          raise ValueError("El nombre no debe contener números")

    except ValueError as e:
      logging.warning(f"Error en nombre: {e}")
      print(f"{e}, favor de revisar")
    except TypeError:
      logging.warning(f"Error en nombre: ")
      print("Hay algún error en el nombre, revisa por favor")
    except Exception as e:
      logging.warning(f"Error en nombre: {e}")
      print(type(e).__name__)
    else:
      break

  while True:
    try:
      Edad = int(input("Ahora ingresa tu edad: "))
      if Edad < 0:
        print("---- Error: Ingrese un valor diferente ----")
        validar_datos()
      
      validar_edad = 1/Edad

    except ZeroDivisionError:
      logging.warning(f"Error en edad: ")
      print("---- La edad no puede ser 0 ----")
    except ValueError:
      logging.warning(f"Error en edad: {e}")
      print("---- Ingresa un numero por favor ----")
    except Exception as e:
      logging.warning(f"Error en edad: {e}")
      print(type(e).__name__)
    else:
      break

  while True:
    try:
      Correo = input("Ingresa tu correo: ")
      v_email(Correo)
    except EmailNotValidError:
      logging.warning(f"Error en el correo: un correo debe tener el signo @")
      print("El correo ingresado es invalido, revisa por favor")
    except Exception as e:
      logging.error(f"Error en el correo: {e}")
      print(type(e).__name__)
    else:
      break

  print("\n")
  logging.info("---- Registro finalizado ----")

  print("\n========== DATOS CAPTURADOS ==========\n")
  print("Nombre del usuario: ", Nombre)
  print(f"Edad del usuario: {Edad} años")
  print("Correo del usuario: ", Correo)
  print("\n")

def probar_validaciones():
  validar_datos()

probar_validaciones()