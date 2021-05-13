import math

def print_result(result, option):
    options = {"1": "Cilindro", "2": "Cubo"}
    print("El volumen del ", options.get(str(option)), " es = ", round(result, 2), "mt3")


def calculate_volume_cube(side):
    return side**3


def calculate_volume_cylinder(radius, height):
    return (radius * radius * math.pi) * height


def request_data(option):
    if option == 1:
        radius = float(input("Ingrese el valor del radio (mt) = "))
        height = float(input("Ingrese el valor del altura (mt) = "))
        result = calculate_volume_cylinder(radius, height)
        print_result(result, option)
    else:
        side = float(input("Ingrese el valor del lado (mt) = "))
        result = calculate_volume_cube(side)
        print_result(result, option)


def menu():
    while(True):
        print("""
========== Menu ==========
1. Calcular volumen de cilindro.
2. Calcular volumen de cubo.
3. Salir
==========================
        """)
        option = int(input("Que opcion desea elegir ")) # Todavia no hago control de ingresos no enteros.
        while(option != 3):
            if option == 1 or option == 2:
                request_data(option)
                break
            else:
                option = int(input("Ingrese un numero valido "))
        if option == 3:
            print("Gracias por usar la aplicacion, nos vemos!")
            break

def run():
    print("""Datacademy | Kenneth Calvo
    Projecto 1 | Python | Reto 4
    Calculo de Volumen de un cilindro y del cubo""")

    menu()



if __name__ == '__main__':
    run()