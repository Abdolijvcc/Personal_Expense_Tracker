import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#from Gestion_de_gasto import
import json
import hashlib



def encriptar(password):
    return hashlib.sha256(password.encode()).hexdigest()

class Usuario:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = encriptar(password)

    def create_account(self):

        if not os.path.exists("data"):
            os.makedirs("data")

        filename = os.path.join("data", f"{self.email}.json")
        if os.path.exists(filename):
            print("Este email ya existe. Por favor, utiliza otro.")
            return False
        data = {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Cuenta creada.")
        return True

    @staticmethod
    def login(email, password):
        filename = os.path.join("data", f"{email}.json")
        if not os.path.exists(filename):
            print("Email o contraseña incorrectos.")
            return False
        with open(filename, "r") as file:
            data = json.load(file)
        if data["password"] == encriptar(password):
            print(f"Bienvenido, {data['name']}")

            return True
        else:
            print("Contraseña incorrecta.")
            return False

def main():
    print("Hola")
    print("Binbenido a  Crear una cuenta")
    

    while True:
        name = input("Introduce tu nombre: ")
        email = input("Introduce tu correo: ")
        if email == "":
            print("El correo no puede estar vacío. Por favor, inténtalo de nuevo.")
            continue
        if "@" not in email or "." not in email:
            print("Correo inválido. Asegúrate de que contenga '@' y un dominio válido.")
            continue
        if len(email) < 5:
            print("El correo debe tener al menos 5 caracteres.")
            continue
        if len(name) < 3:
            print("El nombre debe tener al menos 3 caracteres.")
            continue
        if len(name) > 20:
            print("El nombre no puede tener más de 20 caracteres.")
            continue
        if not name.isalpha():
            print("El nombre solo puede contener letras.")
            continue
        if len(name) == 0:
            print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
            continue
        if len(email) == 0:
            print("El correo no puede estar vacío. Por favor, inténtalo de nuevo.")
            continue
        if len(email) > 50:
            print("El correo no puede tener más de 50 caracteres.")
            continue
        if len(name) > 20:
            print("El nombre no puede tener más de 20 caracteres.")
            continue
        if not name.isalpha():
            print("El nombre solo puede contener letras.")
            continue
        if len(name) == 0:
            print("El nombre no puede estar vacío. Por favor, inténtalo de nuevo.")
            continue
        password = input("Introduce tu contraseña: ")
        if len(password) < 6:
            print("La contraseña debe tener al menos 6 caracteres.")
            continue
        if len(password) > 20:
            print("La contraseña no puede tener más de 20 caracteres.")
            continue
        if not any(char.isdigit() for char in password):
            print("La contraseña debe contener al menos un número.")
            continue
        if not any(char.isalpha() for char in password):
            print("La contraseña debe contener al menos una letra.")
            continue
        if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in password):
            print("La contraseña debe contener al menos un carácter especial.")
            continue
        
        # Si todos los datos son válidos, crear la cuenta
        user = Usuario(name, email, password)
        if user.create_account():
            break

""" elif choice == "2":
        while True:
            email = input("Correo: ")
            password = input("Contraseña: ")
            if Usuario.login(email, password):
                break
    else:
        print("Introduce un número válido: 1 o 2.")"""

if __name__ == "__main__":
    main()
