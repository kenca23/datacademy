def converter(value, conv_type):
    convertion_value = 1.609344
    if conv_type == 1: # From Miles to Km.
        result = value * convertion_value
        return round(result, 2)
    else:
        result = value / convertion_value
        return round(result, 2)


def print_result(value, result, conv_type):
    if conv_type ==1:
        print("El valor de ", value, " Millas es de ", result, " Km")
    else:
        print("El valor de ", value, " Km es de ", result, " Millas")

def request_data(conv_type):
    value = float(input("Digite el valor del que desea convertir = "))
    result = converter(value, conv_type)
    print_result(value, result, conv_type)


def menu():
    while(True):
        print("""
========== Menu ==========
1. Millas a Kilometros.
2. Kilometros a Millas.
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
    Projecto 1 | Python | Reto 3
    Conversor de Millas a Kilometros y viceversa""")

    menu()



if __name__ == '__main__':
    run()