"""
Script: Validador de nombres
Autor: Anllev
Descripción: Este programa valida que un nombre de usuario cumpla con 
reglas de longitud y formato.

- - -

Intenta escribir código en inglés más tarde.
Nada te impide escribir en tu propio idioma,
pero generalmente es mejor que todos escriban
en un solo idioma (inglés) para que todos
puedan entender tu código. Es un consenso, no
una regla.
"""

def validar(nombre: str) -> bool:
    if nombre[0] == " " or nombre[-1] == " ": # ¿Por qué eso?
        return True
    
    if not nombre.isalpha():
        print("Error, el nombre solo puede contener letras y un solo nombre!!! Vuelva a intentarlo.")
        return False
    
    if len(nombre) < 2:
        print("Error, El nombre debe tener al menos 2 letras!!! Vuelva a intentarlo.")
        return False
    
    if len(nombre) > 10:
        print("Error, El nombre no puede tener más de 10 letras!!! Vuelva a intentarlo.")
        return False
    
    if nombre[0].islower():
        print("Error, Los nombres empiezan con mayúscula!!! Vuelva a intentarlo.")
        return False
    
    if not nombre[1:].islower():
        print("Error, El resto del nombre debe estar en minúscula!!! Vuelva a intentarlo.")
        return False
    
    return True

def validador_de_nombres() -> None:
    print("- - - validador_de_nombres - - -")
    
    while True:
        nombre: str = input("Ingrese su primer nombre: ")
        
        if validar(nombre):
            print(f"Hola {nombre}!!!")
            break
        
        print()
    
    print("- " * 18 + "\n")

"""
Si desea escribir con mayúscula la primera
letra del nombre sin necesidad de validarlo,
utilice la siguiente función en lugar de
name_validator(). ↓
"""

def poner_nombres_en_mayuscula() -> None:
    print("- - poner_nombres_en_mayuscula - -")
    nombre: str = input("Ingrese su primer nombre: ").capitalize()
    print(f"Hola {nombre}!!!")
    print("- " * 18 + "\n")

# Aquí se ejecutan ambas funciones. ↓
# Ambas tienen el mismo resultado.
# La diferencia es que una expone los errores al usuario.
if __name__ == "__main__":
    validador_de_nombres()
    poner_nombres_en_mayuscula()