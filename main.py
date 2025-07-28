import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from login_sgin_up import crear_cuenta
from Gestion_de_gasto import todo

def main():
    print("Bienvenido al Gestor de Gastos")
    print("1. Crear cuenta")
    print("2. Iniciar sesión")
    
    choice = input("Elige número 1 o 2: ")
    
    if choice == "1":
        crear_cuenta.main()
    elif choice == "2":
        todo.iniciar_sesion()
    else:
        print("Introduce un número válido: 1 o 2.")

if __name__ == "__main__":
    main()        