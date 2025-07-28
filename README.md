# Personal Expense Tracker

Gestor personal de gastos e ingresos en Python. Permite a los usuarios crear cuentas, iniciar sesión, registrar gastos e ingresos, clasificarlos, calcular totales y visualizar gráficos de sus finanzas personales.

---

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Instalación](#instalación)
- [Uso](#uso)
- [Detalles de los Módulos](#detalles-de-los-módulos)
- [Formato de Archivos](#formato-de-archivos)
- [Notas de Seguridad](#notas-de-seguridad)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción

**Personal Expense Tracker** es una aplicación de consola escrita en Python que permite a los usuarios gestionar sus finanzas personales de manera sencilla. Los datos se almacenan en archivos JSON, uno por usuario, y los movimientos (gastos/ingresos) se guardan en archivos separados para facilitar la gestión y visualización.

---

## Características

- Registro y autenticación de usuarios.
- Almacenamiento seguro de contraseñas (hash).
- Registro de gastos e ingresos.
- Clasificación de movimientos.
- Cálculo de gasto total.
- Visualización de gráficos de gastos e ingresos.
- Persistencia de datos en archivos JSON.
- Interfaz de línea de comandos amigable.

---

## Estructura del Proyecto

```
Personal_Expense_Tracker/
│
├── data/                         # Archivos JSON de usuarios y movimientos
│   ├── usuario1.json
│   ├── usuario1_data.json
│   └── ...
│
├── Gestion_de_gasto/
│   └── todo.py
│
├── login_sgin_up/
│   ├── crear_cuenta.py
│   └── __init__.py
│
├── main.py
└── README.md
```

---

## Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/tu_usuario/Personal_Expense_Tracker.git
   cd Personal_Expense_Tracker
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
   > Si no tienes `requirements.txt`, instala manualmente:
   > ```bash
   > pip install matplotlib
   > ```

---

## Uso

1. **Ejecuta la aplicación principal:**
   ```bash
   python main.py
   ```

2. **Sigue las instrucciones en pantalla:**
   - Crea una cuenta o inicia sesión.
   - Agrega gastos o ingresos.
   - Visualiza y clasifica tus movimientos.
   - Genera gráficos de tus finanzas.

---

## Detalles de los Módulos

### `main.py`

- Punto de entrada de la aplicación.
- Muestra el menú principal y redirige a las funciones de registro, login y gestión de gastos.

### `login_sgin_up/crear_cuenta.py`

- Clase `Usuario` para crear cuentas y autenticar usuarios.
- Almacena datos de usuario en archivos JSON individuales.
- Contraseñas almacenadas como hash.

### `Gestion_de_gasto/todo.py`

- Funciones para agregar, clasificar y calcular gastos/ingresos.
- Generación de gráficos usando `matplotlib`.
- Cada usuario tiene su propio archivo de movimientos: `data/<email>_data.json`.

---

## Formato de Archivos

### Datos de usuario (`data/<email>.json`):

```json
{
  "name": "Juan",
  "email": "juan@email.com",
  "password": "<hash>"
}
```

### Movimientos (`data/<email>_data.json`):

```json
[
  {
    "tipo": "gasto",
    "monto": 100.0,
    "descripcion": "Supermercado",
    "fecha": "2025-07-28 14:34:07"
  },
  {
    "tipo": "ingreso",
    "monto": 1200.0,
    "descripcion": "Sueldo",
    "fecha": "2025-07-28 15:00:00"
  }
]
```

---

## Notas de Seguridad

- Las contraseñas se almacenan como hash, pero **no uses este sistema en producción** sin mejoras de seguridad.
- Los archivos JSON no están cifrados.
- No compartas tu carpeta `data/` si contiene datos reales.

---

## Contribuciones

¡Las contribuciones son bienvenidas!  
Puedes abrir issues o pull requests para sugerir mejoras, reportar bugs o agregar nuevas funcionalidades.

---

## Licencia

Este proyecto está bajo la licencia MIT.  
Consulta el archivo `LICENSE` para más detalles.

---

## Créditos

Desarrollado por [Tu Nombre o Equipo].  
Inspirado en la necesidad de gestionar gastos personales de forma sencilla y visual.

---

## Contacto

Para dudas o sugerencias, contacta a: [tu_email@ejemplo.com]

---

¡Gracias por usar **Personal Expense Tracker**!