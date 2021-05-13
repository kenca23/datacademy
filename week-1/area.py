def calculate_area(base, height):
    area = (base * height) / 2
    print("El area del triangulo es = ", area)


def area_option():
    base = int(input("Digite el valor de la base del triangulo = "))
    height = int(input("Digite el valor de la altura del triangulo = "))
    calculate_area(base, height)


def type_triangle(side1, side2, side3):
    if side1 == side2 and side1 == side3:
        print("Tipo de triangulo - Equilatero")
    if (side1 == side2 and side1 != side3) or (side1 != side2 and side1 == side3) or (side1 != side2 and side2 == side3):
        print("Tipo de triangulo - Isosceles")
    if side1 != side2 and side1 != side3 and side2 != side3:
        print("Tipo de triangulo - Escaleno")


def type_option():
    side1 = int(input("Digite el valor del lado 1 = "))
    side2 = int(input("Digite el valor del lado 2 = "))
    side3 = int(input("Digite el valor del lado 3 = "))
    type_triangle(side1, side2, side3)


def menu():
    while(True):
        print("""
========== Menu ==========
1. Calculo de area.
2. Tipo de triangulo.
3. Salir
==========================
        """)
        option = int(input("Que opcion desea elegir ")) # Todavia no hago control de ingresos no enteros.
        while(option != 3):
            if option == 1:
                area_option()
                break
            elif option == 2:
                type_option()
                break
            else:
                option = int(input("Ingrese un numero valido "))
        if option == 3:
            print("Gracias por usar la aplicacion, nos vemos!")
            break


def run():
    print("""
Datacademy | Kenneth Calvo
Projecto 1 | Python | Reto 1
Calculo de Area de triangulo""")

    menu()
    


if __name__ == '__main__':
    run()