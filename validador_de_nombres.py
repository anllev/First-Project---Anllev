"""
Script: Validador de nombres
Autor: Anllev
Descripción: Este programa valida que un nombre de usuario cumpla con 
reglas de longitud y formato.

"""
nombre1 = input("Ingrese su primer nombre: ").strip()
while True:
    if nombre1[0] == " " or nombre1[-1] == " ":
        print("Hola " + nombre1 + "!!!")
        break
    elif not nombre1.isalpha():
        print("Error, el nombre solo puede contener letras y un solo nombre. Vuelva a intentarlo.")
        nombre1 = input("Ingrese su primer nombre: ")
    elif len(nombre1) < 2:
        print("Error")
        nombre1 = input("El nombre debe tener al menos 2 letras. Vuelva a intentarlo: ")
    elif len(nombre1) > 10:
        print("Error")
        nombre1 = input("El nombre no puede tener más de 10 letras. Vuelva a intentarlo: ")
    elif nombre1[0].islower():
        print("Error")
        nombre1 = input("Los nombres empiezan con mayúscula!!!. Vuelva a intentarlo: ")
    elif nombre1[1:10] != nombre1[1:10].lower():
        print("Error")
        nombre1 = input("El resto del nombre debe estar en minúscula!!!. Vuelva a intentarlo: ")
    else:
        print("Hola " + nombre1 + "!!!")
        break
