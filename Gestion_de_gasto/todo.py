import sys
import os
import json
import time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from login_sgin_up import crear_cuenta
import matplotlib.pyplot as plt
from datetime import datetime
from collections import defaultdict


email = ""
password = ""

def main():
    print("Bienvenido al Gestor de Gastos")
    print("Por favor, inicie sesión para continuar.")
    
    iniciar_sesion()

def iniciar_sesion():
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    if crear_cuenta.Usuario.login(email, password):
        print("Sesión iniciada correctamente.")
        time.sleep(1)
        # leer su datos y saber si el usuario tine gastos o ingresos
        filename = os.path.join("data", f"{email}.json")
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    datos = json.load(file)
                    if "tipo" in datos and datos["tipo"] in ["gasto", "ingreso"]:
                        print(f"Tipo de movimiento encontrado: {datos['tipo']}")
                    else:
                        print("No se encontraron movimientos previos.")
                except json.JSONDecodeError:
                    print("Error al leer los datos. Asegúrate de que el archivo JSON esté bien formado.")
        else:
            print("No se encontraron datos para este usuario. Creando un nuevo archivo...")
            with open(filename, "w") as file:
                json.dump([], file)

        while True:
            print("\nMenú Principal:")
            time.sleep(0.3)
            print("1. Agregar Gasto o Ingreso")
            time.sleep(0.3)
            print("2. Clasificar Gastos e Ingresos")
            time.sleep(0.3)
            print("3. Calcular Gasto Total")
            time.sleep(0.3)
            print("4. Generar Gráfico de Gastos e Ingresos")
            time.sleep(0.3)
            print("5. Cerrar Sesión")
            time.sleep(0.3)
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                agregar_gasto_o_ingreso(email)
            elif opcion == "2":
                

                clasificar()
            elif opcion == "3":
                gasto_total()
            elif opcion == "4":
               grafico(email)
               """ # leer su datos y saber si el usuario tine gastos o ingresos
               filename = os.path.join("data", f"{email}.json")
               if os.path.exists(filename):
                    with open(filename, "r") as file:
                        try:
                            datos = json.load(file)
                            if "tipo" in datos and datos["tipo"] in ["gasto", "ingreso"]:
                                #print(f"Tipo de movimiento encontrado: {datos['tipo']}")
                                grafico()
                            else:
                                print("No se encontraron movimientos previos.")
                        except json.JSONDecodeError:
                            print("Error al leer los datos. Asegúrate de que has rellnado este formado.")
               else:
                    print("No se encontraron datos para este usuario. Creando un nuevo archivo...")
                    with open(filename, "w") as file:
                        json.dump([], file)"""
                #grafico()
            elif opcion == "5":
                print("Cerrando sesión...")
                time.sleep(1)
                break
            else:
                print("Opción no válida. Intente nuevamente.") 
        
         
        #agregar_gasto_o_ingreso(email)
    else:
        print("Error al iniciar sesión.")

def agregar_gasto_o_ingreso(email):
    filename = os.path.join("data", f"{email}_data.json")

    while True:
        tipo = input("¿Es un gasto o un ingreso? (gasto/ingreso): ").strip().lower()
        if tipo not in ["gasto", "ingreso"]:
            print("Tipo no válido. Debe ser 'gasto' o 'ingreso'.")
            continue

        try:
            monto = float(input(f"Ingrese el monto del {tipo}: "))
        except ValueError:
            print("Por favor, ingresa un número válido para el monto.")
            continue

        descripcion = input(f"Ingrese una descripción del {tipo}: ")

        # Leer movimientos anteriores
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    datos_anteriores = json.load(file)
                except json.JSONDecodeError:
                    datos_anteriores = []
        else:
            datos_anteriores = []

        nuevo_movimiento = {
            "tipo": tipo,
            "monto": monto,
            "descripcion": descripcion,
            "fecha": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        datos_anteriores.append(nuevo_movimiento)

        with open(filename, "w") as file:
            json.dump(datos_anteriores, file, indent=4)

        print(f"{tipo.capitalize()} agregado: {descripcion} por {monto}.")
        print("Operación completada.")

        continuar = input("¿Deseas agregar otro gasto o ingreso? (s/n): ").strip().lower()
        if continuar != "s":
            print("Regresando al menú principal o cerrando sesión...")
            break
        time.sleep(0.4)
        print("Volviendo al menú principal...")
        time.sleep(1)

def clasificar ():
    print("Clasificando gastos e ingresos...")
    # Aquí se puede implementar la lógica de clasificación si es necesario
    time.sleep(1)
    print("Clasificación completada.")        

def gasto_total(email):
    print("Calculando el gasto total...")
    filename = os.path.join("data", f"{email}.json")
    
    

    with open(filename, "r") as file:
        try:
            datos = json.load(file)
        except json.JSONDecodeError:
            print("Error al leer los datos. Asegúrate de que el archivo JSON esté bien formado.")
            return

    total_gasto = sum(item["monto"] for item in datos if item["tipo"] == "gasto")
    print(f"Gasto total: {total_gasto}")


def grafico(email):
    
    print("Generando gráficos...")

    filename = os.path.join("data", f"{email}_data.json")

    try:
        with open(filename, "r") as file:
            datos = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Error: No se pudo leer el archivo o está mal formado.")
        return

    if not datos:
        print("No hay datos disponibles para mostrar.")
        return

    print("\n Transacciones registradas:")
    for item in datos:
        print(f"- {item['fecha']} | {item['tipo'].capitalize()} | {item['monto']} | {item['descripcion']}")

    resumen = defaultdict(float)
    fechas = []
    montos = []
    colores_linea = []

    for item in datos:
        resumen[item["tipo"]] += item["monto"]
        fechas.append(datetime.strptime(item["fecha"], "%Y-%m-%d %H:%M:%S"))
        montos.append(item["monto"])
        colores_linea.append('#2ecc71' if item["tipo"] == 'ingreso' else '#e74c3c')

    tipos = list(resumen.keys())
    montos_resumen = list(resumen.values())
    colores_barras = ['#2ecc71' if tipo == 'ingreso' else '#e74c3c' for tipo in tipos]

    plt.figure(figsize=(15, 7))

    # Gráfico de barras (resumen)
    plt.subplot(1, 3, 1)
    plt.bar(tipos, montos_resumen, color=colores_barras)
    plt.title("Resumen de Ingresos y Gastos", fontsize=13)
    plt.ylabel("Monto")
    plt.grid(axis='y', linestyle='--', alpha=0.3)

    # Gráfico circular (porcentaje)
    plt.subplot(1, 3, 2)
    plt.pie(montos_resumen, labels=tipos, autopct='%1.1f%%', colors=colores_barras, startangle=140)
    plt.title("Distribución (%)", fontsize=13)
    plt.axis("equal")

    # Gráfico por tiempo o detalle
    if len(datos) > 5:
        plt.subplot(1, 3, 3)
        plt.plot(fechas, montos, marker='o', linestyle='-', color='#3498db')
        for i in range(len(fechas)):
            plt.scatter(fechas[i], montos[i], color=colores_linea[i], s=50)
        plt.title("Evolución de Transacciones", fontsize=13)
        plt.xlabel("Fecha")
        plt.ylabel("Monto")
        plt.xticks(rotation=45)
    else:
        plt.subplot(1, 3, 3)
        etiquetas = [f"{i+1}" for i in range(len(datos))]
        plt.bar(etiquetas, montos, color=colores_linea)
        plt.title("Detalle de Transacciones", fontsize=13)
        plt.xlabel("Transacción")
        plt.ylabel("Monto")

    plt.tight_layout()
    plt.show()

    print(" Gráficos generados correctamente.")
    time.sleep(1)
    print(" Volviendo al menú principal...")

"""def modificar_datos(email):
    filename = os.path.join("data", f"{email}.json")
    
    if not os.path.exists(filename):
        print("No se encontraron datos para modificar.")
        return

    with open(filename, "r") as file:
        # que datos se pueden modificar
        # gastos, ingresos

        try:
            datos = json.load(file)
        except json.JSONDecodeError:
            print("Error al leer los datos. Asegúrate de que el archivo JSON esté bien formado.")
            return

    # Aquí puedes implementar la lógica para modificar los datos
    # Por ejemplo, podrías permitir al usuario editar un gasto o ingreso específico

    print("Función de modificación de datos aún no implementada.")    """