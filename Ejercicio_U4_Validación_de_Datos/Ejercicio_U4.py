# Ejercicio validación de usuarios

from email_validator import validate_email as v_email
from email_validator import EmailNotValidError

Nombre = str(input("Ingresa tu nombre: "))
Edad = int(input("Ahora ingresa tu edad: "))
Correo = str(input("Ingresa tu correo: "))
# Contraseña = str(input("Ingresa tu contraseña: "))

def validar_datos():
  try:
    if not Nombre:
      raise TypeError("Entrada invalida")

    Edad
    validar_edad = 1/Edad

    valid_correo = v_email(Correo)


  except TypeError:
    print("Hay algún error en el nombre, revisa por favor")

  except ZeroDivisionError:
    print("Hay algún error en la edad, revisa por favor")

  except EmailNotValidError:
    print("El correo ingresado es invalido, revisa por favor")

  finally:
    print("Registro finalizado")

def probar_validaciones():
  validar_datos()

probar_validaciones()
