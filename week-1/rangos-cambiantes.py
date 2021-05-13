def calculate_range():
    lower_limit = int(input("Ingrese el numero del limite inferior = "))
    upper_limit = int(input("Ingrese el numero del limite superior = "))
    value = int(input("Ingrese el numero que quiere evaluar = "))

    while value < lower_limit or value > upper_limit:
        value = int(input("El numero no esta dentro del rango, por favor digite otro numero = "))
    
    print("El numero ", value, " esta entre ", lower_limit, " y ", upper_limit)


def run():
    print("""Datacademy | Kenneth Calvo
    Projecto 1 | Python | Reto 5
    Rangos cambiantes""")

    calculate_range()



if __name__ == '__main__':
    run()